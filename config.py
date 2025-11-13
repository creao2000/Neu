# config.py - Enhanced configuration for NEU Chatbot
from pathlib import Path

# Base paths
ROOT = Path(__file__).resolve().parent
MODEL_DIR = ROOT / "models"                 # model files stored here
VECTORSTORE_DIR = ROOT / "vectorstore"     # chroma persistent store
DATA_DIR = ROOT / "data"                   # where your JSON/Excel/Word outputs land

# Embedding model (Sentence-Transformers)
EMBED_MODEL = "all-MiniLM-L6-v2"           # CPU-friendly, fast, accurate

# Primary local GGUF model file (quantized) - for 8GB RAM PCs
GGUF_MODEL = MODEL_DIR / "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"


# RAG and LLM settings
MAX_HISTORY_TURNS = 6                       # keep last N turns
N_RESULTS = 6                               # how many doc chunks to return after rerank

# Model inference controls - optimized for 8GB RAM
LLAMA_THREADS = 30                         # adjust to CPU cores (6 is good for most)
                   # increased for better responses
TEMPERATURE = 0.6                           # balanced creativity and accuracy
TOP_K = 30                                 # top-k sampling
TOP_P = 0.8                             # nucleus sampling

# Retrieval / maintenance
RERANK_CANDIDATES = 10                      # fetch this many, then rerank to N_RESULTS
DATA_WATCH_SECS = 15                        # auto-reindex polling interval

# LoRA adapter for llama.cpp (same base GGUF model)
LORA_ENABLED = False

LORA_ADAPTER = MODEL_DIR / "neu_lora_adapter.gguf"   # set to your LoRA adapter filename

# Advanced Reranking Weights
RERANK_WEIGHTS = {
    "semantic": 0.35,                       # semantic similarity (highest)
    "cross_encoder": 0.25,                  # cross-encoder reranking
    "bm25": 0.20,                           # BM25 keyword matching
    "tfidf": 0.15,                          # TF-IDF cosine similarity
    "jaccard": 0.05                          # Jaccard similarity
}

# Confidence and Validation
CONFIDENCE_THRESHOLD = 0.7                  # minimum confidence for responses
VALIDATION_STRICTNESS = "medium"             # low, medium, high

# Tool Integration
ENABLE_TOOLS = True                          # enable GPA calculator, timetable lookup
TOOL_TIMEOUT_MS = 5000                      # maximum tool execution time

# Learning and Adaptation
LEARNING_ENABLED = True                      # enable continuous learning
FEEDBACK_THRESHOLD = 5                      # minimum feedback score for learning
CORRECTION_THRESHOLD = 10                   # corrections needed before retraining

# Database Settings
DB_PATH = ROOT / "neu_chatbot.db"           # SQLite database path
DB_BACKUP_INTERVAL = 24                     # backup database every N hours

# Security and Rate Limiting
RATE_LIMIT_PER_MINUTE = 90                  # requests per minute per IP
MAX_SESSION_DURATION = 3600                 # maximum session duration in seconds
ABUSE_DETECTION_ENABLED = True              # enable abuse detection

# Language Support
SUPPORTED_LANGUAGES = ["en", "tr"]          # English and Turkish
DEFAULT_LANGUAGE = "en"                     # default language

# Performance Tuning
CACHE_ENABLED = True                        # enable response caching
CACHE_TTL = 300                             # cache TTL in seconds
MAX_CONCURRENT_REQUESTS = 10                # maximum concurrent requests

# Monitoring and Analytics
ANALYTICS_ENABLED = True                    # enable usage analytics
METRICS_INTERVAL = 60                       # metrics collection interval in seconds
LOG_LEVEL = "INFO"                          # logging level

# File Processing
MAX_FILE_SIZE_MB = 50                       # maximum file size for processing
SUPPORTED_FORMATS = [".json", ".txt", ".pdf"]  # supported file formats
CHUNK_SIZE = 500                            # text chunk size for processing
CHUNK_OVERLAP = 50                          # overlap between chunks

# WebSocket Settings
WS_ENABLED = True                           # enable WebSocket support
WS_HEARTBEAT_INTERVAL = 30                  # WebSocket heartbeat interval

# Development and Debug
DEBUG_MODE = False                           # enable debug mode
VERBOSE_LOGGING = True                       # enable verbose logging
PROFILE_PERFORMANCE = False                  # enable performance profiling

# Add to config.py
SESSION_TIMEOUT_MINUTES = 30  # Session expires after 30 minutes of inactivity
DB_LOGGING_ENABLED = True

