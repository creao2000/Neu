# app.py (Improved version with better conversation handling)
#cloudflared tunnel --url http://localhost:5173
#cloudflared tunnel --url http://localhost:5000

import asyncio
import concurrent.futures
import json
import re
import sqlite3
import random
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

# Import helpers
from helpers import get_intent_response

# Import conversation memory
from conversation_memory import get_session, cleanup_expired_sessions

# ================================
# Config
# ================================
try:
    from config import (
        EMBED_MODEL,
        GGUF_MODEL,
        LLAMA_THREADS,
        DB_LOGGING_ENABLED,
    )
except ImportError:
    # EMBED_MODEL = "all-MiniLM-L6-v2"
    EMBED_MODEL = "all-mpnet-base-v2"

    GGUF_MODEL = Path("models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf")

    LLAMA_THREADS = 30
    DB_LOGGING_ENABLED = True

# ================================
# FastAPI app
# ================================
app = FastAPI(title="NEU University AI", version="2.0.0")

app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

# ================================
# Models
# ================================
class ChatPayload(BaseModel):
    message: Optional[str] = None
    session_id: Optional[str] = None

class ReactionPayload(BaseModel):
    session_id: str
    log_id: int
    reaction: str  # 'like', 'dislike', or ''

# ================================
# Globals
# ================================
_embedder = SentenceTransformer(EMBED_MODEL)
_model_path = GGUF_MODEL
_llm = None
_executor = concurrent.futures.ThreadPoolExecutor(max_workers=28)
_training_in_progress = False

# ================================
# Database
# ================================
def init_db():
    conn = sqlite3.connect("conversations.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversation_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT,
            user_message TEXT,
            bot_response TEXT,
            user_reaction TEXT DEFAULT '',
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def log_conversation(session_id: str, user_message: str, bot_response: str) -> int:
    if not DB_LOGGING_ENABLED:
        return -1
    try:
        conn = sqlite3.connect("conversations.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO conversation_logs (session_id, user_message, bot_response) VALUES (?, ?, ?)",
            (session_id, user_message, bot_response),
        )
        log_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return log_id
    except Exception as e:
        print(f"DB log error: {e}")
        return -1

def get_conversation_logs(session_id: str):
    """Get all conversation logs for a session"""
    try:
        conn = sqlite3.connect("conversations.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, user_message, bot_response, user_reaction, timestamp FROM conversation_logs WHERE session_id = ? ORDER BY timestamp ASC",
            (session_id,)
        )
        logs = cursor.fetchall()
        conn.close()
        
        return [
            {
                "id": log[0],
                "user_message": log[1],
                "bot_response": log[2],
                "user_reaction": log[3],
                "timestamp": log[4]
            }
            for log in logs
        ]
    except Exception as e:
        print(f"DB fetch error: {e}")
        return []

# ================================
# Helpers
# ================================
def response_with_log(response: str, session_id: str, log_id: int, context_used: bool, start_time: float):
    return {
        "response": response,
        "session_id": session_id,
        "log_id": log_id,
        "context_used": context_used,
        "status": "success",
        "response_time_ms": int((time.time() - start_time) * 1000),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

def error_response(session_id: str):
    return JSONResponse(
        status_code=200,
        content={
            "response": "I'm here to help! Could you please rephrase your question about Near East University?",
            "session_id": session_id or "error",
            "log_id": -1,
            "context_used": False,
            # "confidence_score": 0.0,
            "status": "success",
            "response_time_ms": 0,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        },
    )

# ================================
# Health Check Endpoint
# ================================
@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy" if _llm is not None else "degraded",
        "message": "NEU AI Chatbot is running",
        "llm_available": _llm is not None,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

@app.get("/health")
async def health_check_alt():
    return await health_check()

# ================================
# Chat Endpoint (Improved)
# ================================
# In your app.py chat_endpoint function, add this at the beginning:
# ================================
# Chat Endpoint (Improved)
# ================================
@app.post("/api/chat")
async def chat_endpoint(payload: ChatPayload):
    start_time = time.time()
    
    print(f"🔍 DEBUG: Using API mode - _llm flag: {_llm}")
    
    user_message = (payload.message or "").strip()
    
    # Handle empty message for session creation
    if not user_message:
        session = get_session(payload.session_id)
        # Let API generate welcome message
        from helpers import safe_llm_complete, build_universal_prompt
        messages = build_universal_prompt("welcome", "Welcome to Near East University")
        welcome_response = safe_llm_complete(messages) or "Welcome to Near East University AI! How can I help you today?"
        
        session.append_assistant(welcome_response)
        log_id = log_conversation(session.session_id, "", welcome_response)
        
        return response_with_log(
            welcome_response, 
            session.session_id, 
            log_id, 
            False, 
            start_time
        )

    # If API is not available
    if not _llm:
        print("❌ API is not available - using fallback response")
        session = get_session(payload.session_id)
        session.append_user(user_message)
        
        fallback_response = "I'm here to help with Near East University questions! What would you like to know? 😊"
        session.append_assistant(fallback_response)
        log_id = log_conversation(session.session_id, user_message, fallback_response)
        
        return response_with_log(
            fallback_response,
            session.session_id,
            log_id,
            False,
            start_time
        )
    
    # Continue with API processing
    try:
        session = get_session(payload.session_id)
        session.append_user(user_message)
        
        print(f"🤖 Processing message via API: '{user_message}'")
        
        # Get response using API
        from helpers import get_intent_response
        response_text = get_intent_response(
            query=user_message,
            analysis={},
            llm=_llm,  # This is now just a flag
            conversation_history=session.get_conversation_summary(),
            session=session
        )
        
        session.append_assistant(response_text)
        log_id = log_conversation(session.session_id, user_message, response_text)
        
        print(f"✅ API Response generated: {response_text[:100]}...")
        
        return response_with_log(
            response_text,
            session.session_id,
            log_id,
            True,
            start_time
        )
        
    except Exception as e:
        print(f"❌ Error in chat endpoint: {e}")
        import traceback
        traceback.print_exc()
        
        # Fallback error response
        session = get_session(payload.session_id)
        error_response_text = "I'm here to help with Near East University questions! What would you like to know? 😊"
        session.append_assistant(error_response_text)
        log_id = log_conversation(session.session_id, user_message, error_response_text)
        
        return response_with_log(
            error_response_text,
            session.session_id,
            log_id,
            False,
            start_time
        )
# ================================
# Session Management Endpoints
# ================================
@app.post("/api/session")
async def create_session():
    """Create a new session"""
    session = get_session(None)
    return {
        "session_id": session.session_id,
        "status": "created",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

@app.get("/api/session/{session_id}")
async def get_session_info(session_id: str):
    """Get session information"""
    session = get_session(session_id)
    return {
        "session_id": session.session_id,
        "message_count": len(session.messages),
        "created_at": getattr(session, 'created_at', datetime.now(timezone.utc).isoformat()),
        "last_activity": getattr(session, 'last_activity', datetime.now(timezone.utc).isoformat())
    }

# ================================
# Conversation Logs Endpoint
# ================================
@app.get("/api/conversation_logs/{session_id}")
async def get_conversation_logs_endpoint(session_id: str):
    """Get all conversation logs for a session"""
    logs = get_conversation_logs(session_id)
    return {
        "session_id": session_id,
        "logs": logs,
        "count": len(logs),
        "status": "success"
    }

# ================================
# Reactions Endpoint
# ================================
@app.post("/api/log_reaction")
async def log_reaction(payload: ReactionPayload):
    try:
        conn = sqlite3.connect("conversations.db")
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE conversation_logs SET user_reaction = ? WHERE id = ? AND session_id = ?",
            (payload.reaction, payload.log_id, payload.session_id),
        )
        conn.commit()
        conn.close()
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# ================================
# Status Endpoint
# ================================
@app.get("/api/status")
async def get_api_status():
    """API status endpoint"""
    try:
        from conversation_memory import active_sessions
        session_count = len(active_sessions)
    except:
        session_count = 0
    
    # Get collection count
    try:
        from helpers import get_all_collections
        collections = get_all_collections()
        collection_count = len(collections)
        collection_names = [col.name for col in collections]
    except:
        collection_count = 0
        collection_names = []
    
    return {
        "status": "running",
        "llm_available": _llm is not None,
        "session_count": session_count,
        "collection_count": collection_count,
        "collections": collection_names,
        "training_in_progress": _training_in_progress,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

@app.get("/status")
async def get_status():
    """Legacy status endpoint"""
    return await get_api_status()

# ================================
# Startup
# ================================
# In your app.py startup_event, add more detailed logging:
@app.on_event("startup")
async def startup_event():
    global _llm
    print("🔄 Initializing chatbot with API endpoints...")

    Path("./sessions").mkdir(exist_ok=True)
    init_db()

    # Test API connection
    try:
        from helpers import get_available_models
        models = get_available_models()
        if models:
            print(f"✅ API connected successfully. Available models: {models}")
            _llm = "api"  # Set a flag that API is available
        else:
            print("❌ API connection failed")
            _llm = None
    except Exception as e:
        print(f"❌ API test error: {e}")
        _llm = None

    # Show available collections
    try:
        from helpers import get_all_collections
        collections = get_all_collections()
        print(f"📚 Available collections: {[col.name for col in collections]}")
    except Exception as e:
        print(f"❌ Collection discovery error: {e}")
# ================================
# Run
# ================================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")