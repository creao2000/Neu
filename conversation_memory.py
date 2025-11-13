# conversation_memory.py
import json
import uuid
import time
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any

# ================================
# Default config (fallback values)
# ================================
try:
    from config import ROOT, MAX_HISTORY_TURNS, SESSION_TIMEOUT_MINUTES
except ImportError:
    ROOT = Path(".")
    MAX_HISTORY_TURNS = 10
    SESSION_TIMEOUT_MINUTES = 30

# ================================
# Storage path
# ================================
SESSIONS_DIR = ROOT / "sessions"
SESSIONS_DIR.mkdir(exist_ok=True)

# ================================
# Conversation Memory Class
# ================================
class ConversationMemory:
    def __init__(self, session_id: Optional[str] = None, persisted: bool = True, max_turns: int = MAX_HISTORY_TURNS):
        self.session_id = session_id or str(uuid.uuid4())
        self.persisted = persisted
        self.max_turns = max_turns
        self.history: List[Dict] = []
        self.created_at = datetime.now()
        self.last_accessed_ts = time.time()  # float timestamp

        # Flexible memory store
        self.state: Dict[str, Any] = {"has_greeted": False}

        # Load existing session
        if self.persisted and self._get_memory_file().exists():
            self._load()


# Add this method to the ConversationMemory class in conversation_memory.py


# --------------------------
# Conversation summary methods
# --------------------------

    # --------------------------
    # Conversation history
    # --------------------------
    def append_user(self, text: str) -> None:
        """Add a user message to history"""
        self.history.append({
            "role": "user",
            "content": text,
            "timestamp": datetime.now().isoformat()
        })
        self.last_accessed_ts = time.time()
        self._trim()
        self._save()

    def append_assistant(self, text: str) -> None:
        """Add an assistant message to history"""
        self.history.append({
            "role": "assistant",
            "content": text,
            "timestamp": datetime.now().isoformat()
        })
        self.last_accessed_ts = time.time()
        self._trim()
        self._save()

    def get_recent(self, n: Optional[int] = None) -> List[Dict]:
        """Get recent messages (n messages total, not pairs)"""
        n = n or self.max_turns
        return self.history[-n:]

    def get_recent_pairs(self, n_pairs: int = 3) -> List[Dict]:
        """Get recent conversation pairs (user + assistant)"""
        recent = self.get_recent(n_pairs * 2)
        return recent

    # --------------------------
    # Conversation summary methods
    # --------------------------
    def get_conversation_summary(self, max_turns: int = 3) -> str:
        """Get recent conversation history as formatted text"""
        if not self.history:
            return ""
        
        # Get recent pairs (user + assistant messages)
        recent = self.get_recent_pairs(max_turns)
        
        summary_lines = []
        for msg in recent:
            role = "Student" if msg['role'] == 'user' else "Assistant"
            summary_lines.append(f"{role}: {msg['content']}")
        
        return "\n".join(summary_lines)

    def get_last_user_message(self) -> Optional[str]:
        """Get the last user message"""
        for msg in reversed(self.history):
            if msg['role'] == 'user':
                return msg['content']
        return None

    def get_last_assistant_message(self) -> Optional[str]:
        """Get the last assistant message"""
        for msg in reversed(self.history):
            if msg['role'] == 'assistant':
                return msg['content']
        return None

    # --------------------------
    # Memory state management
    # --------------------------
    def remember(self, key: str, value: Any) -> None:
        """Store a key-value pair in memory"""
        self.state[key] = value
        self._save()

    def recall(self, key: str, default: Any = None) -> Any:
        """Retrieve a value from memory"""
        return self.state.get(key, default)

    def forget(self, key: str) -> None:
        """Remove a key from memory"""
        if key in self.state:
            del self.state[key]
            self._save()

    def clear_history(self) -> None:
        """Clear conversation history but keep session alive"""
        self.history = []
        self._save()

    def update_user_context(self, key: str, value: Any) -> None:
        """Update user-specific context that persists across conversations"""
        if 'user_context' not in self.state:
            self.state['user_context'] = {}
        self.state['user_context'][key] = value
        self._save()

    def get_user_context(self, key: str, default: Any = None) -> Any:
        """Get user-specific context"""
        return self.state.get('user_context', {}).get(key, default)

    # --------------------------
    # Persistence methods
    # --------------------------
    def _save(self) -> None:
        """Save session to disk"""
        if not self.persisted:
            return
        try:
            data = {
                "history": self.history,
                "created_at": self.created_at.isoformat(),
                "last_accessed_ts": self.last_accessed_ts,
                "state": self.state
            }
            self._get_memory_file().write_text(
                json.dumps(data, ensure_ascii=False, indent=2),
                encoding="utf-8"
            )
        except Exception as e:
            print(f"Error saving session {self.session_id}: {e}")

    def _load(self) -> None:
        """Load session from disk"""
        try:
            data = json.loads(self._get_memory_file().read_text(encoding="utf-8"))
            self.history = data.get("history", [])
            self.created_at = datetime.fromisoformat(data.get("created_at", datetime.now().isoformat()))
            self.last_accessed_ts = data.get("last_accessed_ts", time.time())
            self.state = data.get("state", {"has_greeted": False})
        except Exception as e:
            print(f"Error loading session {self.session_id}: {e}")

    def _trim(self) -> None:
        """Trim history to maximum size"""
        max_items = self.max_turns * 2  # user+assistant pairs
        if len(self.history) > max_items:
            self.history = self.history[-max_items:]

    def _get_memory_file(self) -> Path:
        """Get the file path for this session"""
        return SESSIONS_DIR / f"session_{self.session_id}.json"

    # --------------------------
    # Session expiration
    # --------------------------
    def is_expired(self) -> bool:
        """Check if session has expired"""
        expiration_seconds = SESSION_TIMEOUT_MINUTES * 60
        return (time.time() - self.last_accessed_ts) > expiration_seconds

    def get_time_until_expiration(self) -> int:
        """Get seconds until session expiration"""
        expiration_seconds = SESSION_TIMEOUT_MINUTES * 60
        time_elapsed = time.time() - self.last_accessed_ts
        return max(0, int(expiration_seconds - time_elapsed))

    # --------------------------
    # Session information
    # --------------------------
    def get_session_info(self) -> Dict[str, Any]:
        """Get session metadata"""
        return {
            "session_id": self.session_id,
            "created_at": self.created_at.isoformat(),
            "last_accessed": datetime.fromtimestamp(self.last_accessed_ts).isoformat(),
            "message_count": len(self.history),
            "user_messages": len([msg for msg in self.history if msg['role'] == 'user']),
            "assistant_messages": len([msg for msg in self.history if msg['role'] == 'assistant']),
            "expires_in_seconds": self.get_time_until_expiration(),
            "is_expired": self.is_expired(),
            "user_context": self.state.get('user_context', {})
        }

    def __str__(self) -> str:
        """String representation of session"""
        info = self.get_session_info()
        return f"Session({info['session_id']}, messages: {info['message_count']}, expires_in: {info['expires_in_seconds']}s)"

    def __repr__(self) -> str:
        return self.__str__()

def get_conversation_summary(self, max_turns: int = 3) -> str:
    """Get recent conversation history as formatted text"""
    if not self.history:
        return ""
    
    # Get recent pairs (user + assistant messages)
    recent = self.get_recent_pairs(max_turns)
    
    summary_lines = []
    for msg in recent:
        role = "Student" if msg['role'] == 'user' else "Assistant"
        summary_lines.append(f"{role}: {msg['content']}")
    
    return "\n".join(summary_lines)

def get_conversation_history(self) -> str:
    """Alias for get_conversation_summary for backward compatibility"""
    return self.get_conversation_summary()
# ================================
# Session Management Functions
# ================================
active_sessions: Dict[str, ConversationMemory] = {}

def get_session(session_id: Optional[str] = None) -> ConversationMemory:
    """Get or create a session."""
    if session_id and session_id in active_sessions:
        session = active_sessions[session_id]
        if not session.is_expired():
            # Update last accessed time
            session.last_accessed_ts = time.time()
            return session
        else:
            # Expired → remove from active sessions
            print(f"🗑️ Removing expired session: {session_id}")
            del active_sessions[session_id]

    # Create new session
    session = ConversationMemory(session_id=session_id)
    active_sessions[session.session_id] = session
    print(f"🆕 Created new session: {session.session_id}")
    return session

def get_session_by_id(session_id: str) -> Optional[ConversationMemory]:
    """Get session by ID without creating a new one"""
    session = active_sessions.get(session_id)
    if session and not session.is_expired():
        session.last_accessed_ts = time.time()  # Update access time
        return session
    return None

def cleanup_expired_sessions() -> None:
    """Remove expired sessions from memory."""
    expired_ids = []
    for sid, session in active_sessions.items():
        if session.is_expired():
            expired_ids.append(sid)
    
    for sid in expired_ids:
        print(f"🗑️ Cleaning up expired session: {sid}")
        del active_sessions[sid]

def get_active_sessions_info() -> List[Dict[str, Any]]:
    """Get information about all active sessions"""
    cleanup_expired_sessions()  # Clean up first
    return [session.get_session_info() for session in active_sessions.values()]

def delete_session(session_id: str) -> bool:
    """Delete a session completely (from memory and disk)"""
    try:
        # Remove from active sessions
        if session_id in active_sessions:
            del active_sessions[session_id]
        
        # Delete session file
        session_file = SESSIONS_DIR / f"session_{session_id}.json"
        if session_file.exists():
            session_file.unlink()
        
        print(f"🗑️ Deleted session: {session_id}")
        return True
    except Exception as e:
        print(f"Error deleting session {session_id}: {e}")
        return False

def get_total_active_sessions() -> int:
    """Get number of active sessions"""
    cleanup_expired_sessions()
    return len(active_sessions)

# ================================
# Utility Functions
# ================================
def cleanup_old_session_files(max_age_hours: int = 24) -> int:
    """Clean up session files older than specified hours"""
    deleted_count = 0
    try:
        for session_file in SESSIONS_DIR.glob("session_*.json"):
            if session_file.stat().st_mtime < time.time() - (max_age_hours * 3600):
                session_file.unlink()
                deleted_count += 1
        print(f"🗑️ Cleaned up {deleted_count} old session files")
    except Exception as e:
        print(f"Error cleaning up session files: {e}")
    
    return deleted_count

def get_session_statistics() -> Dict[str, Any]:
    """Get overall session statistics"""
    cleanup_expired_sessions()
    
    total_messages = 0
    total_users = 0
    total_assistants = 0
    
    for session in active_sessions.values():
        total_messages += len(session.history)
        total_users += len([msg for msg in session.history if msg['role'] == 'user'])
        total_assistants += len([msg for msg in session.history if msg['role'] == 'assistant'])
    
    return {
        "active_sessions": len(active_sessions),
        "total_messages": total_messages,
        "user_messages": total_users,
        "assistant_messages": total_assistants,
        "average_messages_per_session": total_messages / max(len(active_sessions), 1),
        "session_directory": str(SESSIONS_DIR),
        "session_files_count": len(list(SESSIONS_DIR.glob("session_*.json")))
    }