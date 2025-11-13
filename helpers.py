# helpers.py
# Updated to use OpenAI-compatible API endpoints

import re
import requests
import chromadb
from chromadb.utils import embedding_functions
from typing import List, Dict, Any, Optional, Tuple
import numpy as np
from sentence_transformers import SentenceTransformer

# API Configuration
API_BASE_URL = "http://127.0.0.1:1234"
HEADERS = {
    "Content-Type": "application/json"
}

# ---------------------------
# ChromaDB init
# ---------------------------
chroma_client = chromadb.PersistentClient(path="./chroma_db")
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# ---------------------------
# API Client Functions
# ---------------------------
def get_available_models():
    """Get available models from the API"""
    try:
        response = requests.get(f"{API_BASE_URL}/v1/models", timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Models endpoint error: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Error getting models: {e}")
        return None

def api_chat_completion(messages: List[Dict], max_tokens: int = 4096, temperature: float = 0.7) -> str:
    """Use chat completions endpoint"""
    try:
        payload = {
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "stop": ["\n\n", "###", "Student:", "User:"],
            "stream": False
        }
        
        response = requests.post(
            f"{API_BASE_URL}/v1/chat/completions",
            json=payload,
            headers=HEADERS,
            timeout=120
        )
        
        if response.status_code == 200:
            result = response.json()
            if 'choices' in result and result['choices']:
                return result['choices'][0]['message']['content'].strip()
        else:
            print(f"❌ Chat completion error: {response.status_code} - {response.text}")
            
    except Exception as e:
        print(f"❌ API chat completion error: {e}")
    
    return ""

def api_completion(prompt: str, max_tokens: int = 4096, temperature: float = 0.7) -> str:
    """Use completions endpoint"""
    try:
        payload = {
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "stop": ["\n\n", "###", "Student:", "User:"],
            "stream": False
        }
        
        response = requests.post(
            f"{API_BASE_URL}/v1/completions",
            json=payload,
            headers=HEADERS,
            timeout=120
        )
        
        if response.status_code == 200:
            result = response.json()
            if 'choices' in result and result['choices']:
                return result['choices'][0]['text'].strip()
        else:
            print(f"❌ Completion error: {response.status_code} - {response.text}")
            
    except Exception as e:
        print(f"❌ API completion error: {e}")
    
    return ""

def api_embeddings(text: str) -> List[float]:
    """Get embeddings for text"""
    try:
        payload = {
            "input": text
        }
        
        response = requests.post(
            f"{API_BASE_URL}/v1/embeddings",
            json=payload,
            headers=HEADERS,
            timeout=15
        )
        
        if response.status_code == 200:
            result = response.json()
            if 'data' in result and result['data']:
                return result['data'][0]['embedding']
        else:
            print(f"❌ Embeddings error: {response.status_code} - {response.text}")
            
    except Exception as e:
        print(f"❌ API embeddings error: {e}")
    
    return []

# ---------------------------
# Collection Management
# ---------------------------
def get_all_collections():
    """Get all collections"""
    try:
        collections = []
        collection_list = chroma_client.list_collections()
        
        for col_info in collection_list:
            try:
                collection = chroma_client.get_collection(
                    name=col_info.name,
                    embedding_function=sentence_transformer_ef
                )
                collections.append(collection)
            except Exception:
                continue
                
        return collections
    except Exception:
        return []

def get_relevant_collections(query: str) -> List:
    """Get collections relevant to the query"""
    collections = get_all_collections()
    if not collections:
        return []

    # For bus queries, prioritize bus timetable collection
    bus_keywords = ["bus", "timetable", "schedule", "shuttle", "transport"]
    if any(keyword in query.lower() for keyword in bus_keywords):
        bus_collections = [col for col in collections if "bus" in col.name.lower()]
        if bus_collections:
            return bus_collections

    # Use API embeddings for similarity for other queries
    query_embedding = api_embeddings(query)
    if not query_embedding:
        return collections[:3]

    scored = []
    for col in collections:
        try:
            col_embedding = api_embeddings(col.name)
            if not col_embedding:
                continue
            
            sim = float(np.dot(query_embedding, col_embedding) /
                        (np.linalg.norm(query_embedding) * np.linalg.norm(col_embedding)))
            scored.append((col, sim))
        except Exception:
            continue

    if not scored:
        return collections[:3]

    scored.sort(key=lambda x: x[1], reverse=True)
    return [col for col, score in scored if score > 0.2][:3]

# ---------------------------
# Clean LLM output
# ---------------------------
def clean_llm_response(text: str) -> str:
    """Clean LLM output but preserve content"""
    if not text:
        return ""
    
    text = re.sub(r'\n\s*\n\s*\n', '\n\n', text).strip()
    return text

# ---------------------------
# Safe LLM completion
# ---------------------------
def safe_llm_complete(messages: List[Dict], max_tokens: int = 4096, temperature: float = 0.7) -> str:
    """Safe LLM completion using API endpoints"""
    
    # Try chat completions first
    response = api_chat_completion(messages, max_tokens, temperature)
    if response:
        return clean_llm_response(response)
    
    # Fallback to completions endpoint
    if messages:
        prompt_parts = []
        for m in messages:
            role = m.get("role", "user")
            content = m.get("content", "")
            if role == "system":
                prompt_parts.append(f"SYSTEM: {content}")
            else:
                prompt_parts.append(f"{role.upper()}: {content}")
        prompt = "\n\n".join(prompt_parts) + "\n\nASSISTANT:"
        
        response = api_completion(prompt, max_tokens, temperature)
        if response:
            return clean_llm_response(response)
    
    return ""

# ---------------------------
# Semantic search with optimized context
# ---------------------------
def get_semantic_context(query: str) -> Tuple[str, List[str]]:
    """Get relevant context from ChromaDB"""
    collections = get_relevant_collections(query)
    if not collections:
        return "No university data available.", []

    all_results = []
    
    for collection in collections:
        try:
            results = collection.query(
                query_texts=[query],
                n_results=3,
                include=["documents", "metadatas", "distances"]
            )
            
            if results and results.get("documents") and results["documents"][0]:
                for i, doc in enumerate(results["documents"][0]):
                    distance = results["distances"][0][i] if results.get("distances") else 1.0
                    if distance < 1.5:
                        all_results.append({
                            "collection": collection.name,
                            "document": doc.strip(),
                            "distance": distance
                        })
        except Exception:
            continue

    if not all_results:
        return "No relevant information found.", []

    # Sort by distance
    all_results.sort(key=lambda x: x["distance"])
    
    # Build comprehensive context text
    context_parts = []
    used_collections = set()
    total_length = 0
    max_context_length = 3000  # Increased limit
    
    for result in all_results:
        if result["collection"] not in used_collections:
            header = f"--- {result['collection']} ---"
            if total_length + len(header) < max_context_length:
                context_parts.append(header)
                total_length += len(header)
                used_collections.add(result["collection"])
        
        doc_text = result["document"]
        if total_length + len(doc_text) < max_context_length:
            context_parts.append(doc_text)
            total_length += len(doc_text)
        else:
            # Add partial document if space allows
            remaining_space = max_context_length - total_length
            if remaining_space > 100:
                context_parts.append(doc_text[:remaining_space] + "...")
            break

    context_text = "\n\n".join(context_parts)
    
    return context_text, list(used_collections)

# ---------------------------
# Universal Prompt Builder
# ---------------------------
def build_universal_prompt(query: str, context: str) -> List[Dict]:
    """Build a universal prompt for API"""
    
    system_message = """You are a helpful assistant for Near East University. 
Answer questions based on the provided university information.
Be natural, comprehensive, and accurate. Provide complete, detailed answers.
If the information isn't available, respond naturally without mentioning the database."""

    user_message = f"""Question: {query}

University Information:
{context}

Please provide a comprehensive, complete answer based on the available information. Include all relevant details and ensure the response is not cut off."""

    return [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]

# ---------------------------
# Main integration: get_intent_response
# ---------------------------
def get_intent_response(query: str, analysis: Dict[str, Any], llm=None, conversation_history: str = "", session=None) -> str:
    """Process query using API endpoints"""
    
    try:
        current_query = query.strip()
        if not current_query:
            return "How can I help you with Near East University today?"

        # Get comprehensive context from ChromaDB
        context, sources = get_semantic_context(current_query)
        
        print(f"📚 Context retrieved: {len(context)} characters from {sources}")
        
        # Build universal prompt
        messages = build_universal_prompt(current_query, context)
        
        # Generate response using API with high token limit
        response = safe_llm_complete(messages, max_tokens=4096, temperature=0.7)
        
        print(f"📝 Response generated: {len(response)} characters")
        
        if not response:
            return "I'm here to help with Near East University questions! What would you like to know?"
        
        return response

    except Exception as e:
        print(f"❌ Error in get_intent_response: {e}")
        import traceback
        traceback.print_exc()
        return "I'm here to help with Near East University questions! What would you like to know?"