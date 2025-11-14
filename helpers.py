# ===============================
# NEU Chatbot - AI-Driven Dynamic System with Natural Memory
# ===============================

import re
import chromadb
from chromadb.utils import embedding_functions
from typing import List, Dict, Any, Optional, Tuple
from sentence_transformers import SentenceTransformer
import numpy as np

# ==========================================
# Initialize ChromaDB
# ==========================================
chroma_client = chromadb.PersistentClient(path="./chroma_db")
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# ==========================================
# Collection Management
# ==========================================
def get_all_collections():
    """Dynamically discover and load all available collections"""
    collections = []
    try:
        collection_list = chroma_client.list_collections()
        print(f"🔍 Discovered {len(collection_list)} collections")
        
        for col_info in collection_list:
            try:
                collection = chroma_client.get_collection(
                    name=col_info.name,
                    embedding_function=sentence_transformer_ef
                )
                collections.append(collection)
                print(f"✅ Loaded collection: {col_info.name}")
            except Exception as e:
                print(f"❌ Error loading collection {col_info.name}: {e}")
                continue
    except Exception as e:
        print(f"❌ Error discovering collections: {e}")
    
    return collections

# ==========================================
# Text Processing
# ==========================================
def normalize_text(text: str) -> str:
    """Normalize text with Turkish character support"""
    if not text:
        return ""
    text = text.lower()
    
    # Turkish character mapping
    replacements = {
        "ı": "i", "İ": "i", "ş": "s", "Ş": "s",
        "ç": "c", "Ç": "c", "ğ": "g", "Ğ": "g",
        "ö": "o", "Ö": "o", "ü": "u", "Ü": "u"
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text

# ==========================================
# AI-Driven Smart Query System
# ==========================================




# ==========================================
# LLM Response Handling
# ==========================================
def get_intent_response(query: str, analysis: Dict[str, Any], llm=None, conversation_history: str = "", session=None) -> str:
    """
    Pure LLM-driven response with user context tracking
    """
    print(f"🤖 Processing: '{query}'")

    if not llm:
        return "How can I help you today?"

    # Extract and store user context (program/department)
    user_context = ""
    if session:
        # Check if user mentions their program
        query_lower = query.lower()
        program_keywords = {
            'cis': 'Computer Information Systems',
            'computer information': 'Computer Information Systems',
            'cs': 'Computer Science',
            'engineering': 'Engineering',
            'business': 'Business Administration'
        }

        for keyword, full_name in program_keywords.items():
            if keyword in query_lower:
                session.update_user_context('program', full_name)
                print(f"📚 Stored user program: {full_name}")
                break

        # Get stored program context
        stored_program = session.get_user_context('program')
        if stored_program:
            user_context = f"\nStudent's program: {stored_program}"

    try:
        # Single-step: Let LLM decide everything
        main_prompt = f"""<s>[INST] You are NEU AI for Near East University.

Conversation so far:
{conversation_history if conversation_history else "No previous conversation"}{user_context}

Current question: "{query}"

Task: Respond with ONE word only:
- FETCH_DATA (if asking about courses, schedules, programs, university data)
- CHAT (if greeting, asking about you, or general chat)

Reply with ONE word: FETCH_DATA or CHAT
[/INST]"""

        decision = llm(
            main_prompt,
            max_tokens=10,
            temperature=0.1,
            echo=False,
            stop=["</s>", "[INST]", "\n"]
        )

        decision_text = extract_llm_text(decision).strip().upper()
        print(f"🎯 Decision: {decision_text}")

        if "FETCH" in decision_text:
            # Build enhanced query with context
            enhanced_query = query
            if session and session.get_user_context('program'):
                enhanced_query = f"{session.get_user_context('program')} {query}"

            # Get data from ChromaDB
            context, sources = get_smart_context_with_relevance_filter(enhanced_query, max_results=3, max_total_length=1200)
            
            # Let LLM generate response with data
            response_prompt = f"""<s>[INST] You are NEU AI for Near East University.

Conversation:
{conversation_history if conversation_history else "No previous conversation"}{user_context}

Student asks: "{query}"

University data:
{context}

Instructions:
- Answer directly using the data above
- Keep response concise and focused
- Use bullet points for lists
- Use tables for courses (| Column | Column |)
- Add relevant emojis (📚 🎓 🚌)
- Never use hashtags (#)

Answer:
[/INST]"""

            response = llm(
                response_prompt,
                max_tokens=250,
                temperature=0.7,
                top_p=0.9,
                echo=False,
                stop=["</s>", "[INST]"]
            )
            
            return clean_llm_response(extract_llm_text(response))
        
        else:
            # General chat response
            chat_prompt = f"""<s>[INST] You are NEU AI for Near East University students.

Previous chat:
{conversation_history if conversation_history else "No previous conversation"}

Student says: "{query}"

Respond briefly and friendly. If asked about yourself, explain you're an AI assistant for NEU. Use 1-2 sentences only.
[/INST]"""

            response = llm(
                chat_prompt,
                max_tokens=80,
                temperature=0.7,
                top_p=0.9,
                echo=False,
                stop=["</s>", "[INST]"]
            )

            return clean_llm_response(extract_llm_text(response))
    
    except Exception as e:
        print(f"❌ Error: {e}")
        return "I'm here to help with Near East University questions. What would you like to know?"


def validate_semester_year_match(query: str, content: str) -> bool:
    """
    Validate that the content matches the semester/year mentioned in query
    """
    query_lower = query.lower()
    content_lower = content.lower()

    # Extract semester/year from query
    semester_patterns = {
        'first semester': ['first semester', 'semester 1', 'semester i', 'fall semester'],
        'second semester': ['second semester', 'semester 2', 'semester ii', 'spring semester'],
        'third semester': ['third semester', 'semester 3', 'semester iii'],
        'fourth semester': ['fourth semester', 'semester 4', 'semester iv']
    }

    year_patterns = {
        'first year': ['first year', 'year 1', 'year one', 'freshman'],
        'second year': ['second year', 'year 2', 'year two', 'sophomore'],
        'third year': ['third year', 'year 3', 'year three', 'junior'],
        'fourth year': ['fourth year', 'year 4', 'year four', 'senior']
    }

    # Check if query mentions specific semester/year
    query_semester = None
    query_year = None

    for key, patterns in semester_patterns.items():
        if any(p in query_lower for p in patterns):
            query_semester = key
            break

    for key, patterns in year_patterns.items():
        if any(p in query_lower for p in patterns):
            query_year = key
            break

    # If no specific semester/year mentioned, accept any content
    if not query_semester and not query_year:
        return True

    # Check if content matches
    if query_semester:
        # Content must mention the same semester
        if not any(p in content_lower for p in semester_patterns[query_semester]):
            # Content mentions a different semester - reject
            for other_sem, other_patterns in semester_patterns.items():
                if other_sem != query_semester:
                    if any(p in content_lower for p in other_patterns):
                        print(f"❌ Rejecting: Query wants {query_semester}, content has {other_sem}")
                        return False

    if query_year:
        # Content must mention the same year
        if not any(p in content_lower for p in year_patterns[query_year]):
            # Content mentions a different year - reject
            for other_year, other_patterns in year_patterns.items():
                if other_year != query_year:
                    if any(p in content_lower for p in other_patterns):
                        print(f"❌ Rejecting: Query wants {query_year}, content has {other_year}")
                        return False

    return True


def get_smart_context_with_relevance_filter(query: str, max_results: int = 5, max_total_length: int = 1500) -> Tuple[str, List[str]]:
    """
    Semantic search with semester/year validation
    """
    collections = get_all_collections()
    if not collections:
        return "No data available.", []

    print(f"🔍 Searching {len(collections)} collections")

    all_results = []

    for collection in collections:
        try:
            results = smart_query_collection(collection, query, n_results=max_results * 2)

            if results['documents']:
                for i, doc in enumerate(results['documents']):
                    if doc and doc.strip():
                        # Validate semester/year match
                        if not validate_semester_year_match(query, doc):
                            continue

                        relevance = results['relevance_scores'][i] if i < len(results['relevance_scores']) else 0

                        all_results.append({
                            'content': doc.strip(),
                            'collection': collection.name,
                            'relevance': relevance
                        })
        except Exception as e:
            print(f"❌ Error querying {collection.name}: {e}")

    # Sort by relevance
    all_results.sort(key=lambda x: x['relevance'], reverse=True)

    # Build context
    context_parts = []
    total_length = 0
    sources = []

    for result in all_results[:max_results]:
        content = result['content']
        if total_length + len(content) <= max_total_length:
            context_parts.append(content)
            total_length += len(content)
            if result['collection'] not in sources:
                sources.append(result['collection'])

    final_context = "\n\n".join(context_parts) if context_parts else "No data found."
    print(f"✅ Retrieved {len(context_parts)} items from {len(sources)} sources")

    return final_context, sources


def smart_query_collection(collection, query: str, n_results: int = 5) -> Dict[str, Any]:
    """
    Pure semantic querying
    """
    results = {'documents': [], 'metadatas': [], 'distances': [], 'relevance_scores': []}
    
    try:
        semantic_results = collection.query(
            query_texts=[query],
            n_results=n_results * 2,
            include=['documents', 'metadatas', 'distances']
        )
        
        if semantic_results and semantic_results.get('documents') and semantic_results['documents'][0]:
            for i, doc in enumerate(semantic_results['documents'][0]):
                if doc and doc.strip():
                    distance = semantic_results['distances'][0][i] if semantic_results.get('distances') else 1.0
                    similarity = 1.0 / (1.0 + distance)
                    
                    results['documents'].append(doc)
                    results['metadatas'].append(semantic_results['metadatas'][0][i] if semantic_results.get('metadatas') else {})
                    results['distances'].append(distance)
                    results['relevance_scores'].append(similarity)
        
        # Sort by relevance
        if results['documents']:
            sorted_idx = sorted(range(len(results['relevance_scores'])), 
                              key=lambda i: results['relevance_scores'][i], reverse=True)
            for key in results:
                results[key] = [results[key][i] for i in sorted_idx][:n_results]
    
    except Exception as e:
        print(f"Error: {e}")
    
    return results


def clean_llm_response(text: str) -> str:
    """Clean LLM output"""
    if not text:
        return ""
    
    text = re.sub(r'\[/INST\].*', '', text, flags=re.DOTALL)
    text = re.sub(r'<s>|</s>', '', text)
    text = re.sub(r'\n\s*\n\s*\n', '\n\n', text)
    
    return text.strip()


def extract_llm_text(response) -> str:
    """Extract text from LLM response"""
    try:
        if isinstance(response, dict):
            if 'choices' in response and response['choices']:
                return response['choices'][0].get('text', '').strip()
            elif 'text' in response:
                return response['text'].strip()
        elif hasattr(response, 'choices') and response.choices:
            return response.choices[0].text.strip()
        elif hasattr(response, 'text'):
            return response.text.strip()
        return str(response).strip()
    except:
        return ""

# ==========================================
# Main Response Function with Natural Memory
# ==========================================

# ==========================================
# Completely Generic Smart Context Retrieval
# ==========================================
def get_smart_context(query: str, max_results: int = 4, max_total_length: int = 1500) -> Tuple[str, List[str]]:
    """Retrieve context using pure semantic matching - NO HARCODED PATTERNS"""
    collections = get_all_collections()
    if not collections:
        return "No data sources available.", []
    
    print(f"🔍 Searching {len(collections)} collections for: '{query}'")
    
    all_results = []
    source_collections = []
    
    # Query ALL collections with pure semantic search
    for collection in collections:
        try:
            results = smart_query_collection(collection, query, n_results=max_results)
            
            if results['documents']:
                for i, doc in enumerate(results['documents']):
                    if doc and doc.strip():
                        # Pure semantic relevance - no hardcoded rules
                        relevance_score = results['relevance_scores'][i] if i < len(results['relevance_scores']) else 0
                        
                        result_item = {
                            'content': doc.strip(),
                            'collection': collection.name,
                            'relevance_score': relevance_score
                        }
                        all_results.append(result_item)
                        
                        if collection.name not in source_collections:
                            source_collections.append(collection.name)
        except Exception as e:
            print(f"❌ Error querying collection {collection.name}: {e}")
            continue
    
    # Sort by pure semantic relevance
    all_results.sort(key=lambda x: x['relevance_score'], reverse=True)
    
    # Build context from most relevant results
    context_parts = []
    total_length = 0
    
    for result in all_results[:max_results]:
        content = result['content']
        if total_length + len(content) <= max_total_length:
            context_parts.append(content)
            total_length += len(content)
        else:
            break
    
    if context_parts:
        final_context = "\n\n".join(context_parts).strip()
        print(f"✅ Context from {len(source_collections)} collections ({total_length} chars)")
        return final_context, source_collections
    
    return "No relevant information found in available databases.", []

# ==========================================
# Completely Generic AI Response Function
# ==========================================


# def get_university_response(query: str, conversation_history: str = "", llm=None) -> str:
#     """Handle university-related questions with context"""
#     print(f"🎓 University question: '{query}'")
    
#     context, source_collections = get_smart_context_with_relevance_filter(query, max_results=3, max_total_length=1200)
    
#     if llm:
#         try:
#             history_section = ""
#             if conversation_history and len(conversation_history) > 20:
#                 history_section = f"Previous conversation:\n{conversation_history}\n\n"
            
#             prompt = f"""<s>[INST] You are NEU AI, a helpful assistant for Near East University.

# {history_section}Student: "{query}"

# University information:
# {context}

# Provide a helpful answer using the information above.

# [/INST]"""

#             response = llm(
#                 prompt,
#                 max_tokens=400,
#                 temperature=0.7,
#                 top_p=0.9,
#                 echo=False,
#                 stop=["</s>", "[INST]"]
#             )
            
#             text = extract_llm_text(response)
#             return clean_llm_response(text) if text else "I don't have that information."
        
#         except Exception as e:
#             print(f"❌ LLM error: {e}")
    
#     return "I'm here to help with Near East University questions."





def calculate_content_relevance(query: str, content: str) -> float:
    """
    Calculate how relevant the content is to the query using simple text analysis
    """
    query_lower = query.lower()
    content_lower = content.lower()
    
    # Simple keyword overlap scoring
    query_words = set(query_lower.split())
    content_words = set(content_lower.split())
    
    # Remove common words that don't indicate relevance
    common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can'}
    
    query_words = query_words - common_words
    content_words = content_words - common_words
    
    if not query_words:
        return 0.5  # Neutral score for very short queries
    
    # Calculate overlap
    overlap = len(query_words.intersection(content_words))
    overlap_ratio = overlap / len(query_words)
    
    # Boost score if query terms appear multiple times in content
    term_frequency_bonus = 0
    for word in query_words:
        term_frequency_bonus += min(content_lower.count(word) * 0.1, 0.3)
    
    final_relevance = min(overlap_ratio + term_frequency_bonus, 1.0)
    
    return final_relevance




# Updated get_intent_response function for helpers.py
# Replace the existing get_intent_response function with this improved version



def get_contextual_fallback(query: str, conversation_history: str, llm) -> str:
    """
    Fallback that checks conversation context for academic indicators
    """
    # Check if recent conversation mentions academic topics
    academic_indicators = [
        'course', 'semester', 'year', 'study', 'program', 'major',
        'department', 'class', 'schedule', 'engineering', 'university',
        'student', 'enroll', 'curriculum', 'credit', 'ects'
    ]
    
    query_lower = query.lower()
    history_lower = conversation_history.lower() if conversation_history else ""
    
    # If query OR recent history contains academic terms, use university response
    query_has_academic = any(indicator in query_lower for indicator in academic_indicators)
    history_has_academic = any(indicator in history_lower for indicator in academic_indicators)
    
    if query_has_academic or history_has_academic:
        print("📚 Context suggests academic topic - using university response")
        return get_university_response(query, conversation_history, llm)
    else:
        print("💬 Context suggests general chat")
        return get_general_response(query, conversation_history, llm)


def get_university_response(query: str, conversation_history: str = "", llm=None) -> str:
    """Handle university-related questions with context"""
    print(f"🎓 University question: '{query}'")
    
    # Get context from ChromaDB using pure semantic search
    context, source_collections = get_smart_context_with_relevance_filter(
        query, max_results=5, max_total_length=1500
    )
    
    if llm:
        try:
            history_section = ""
            if conversation_history and len(conversation_history) > 20:
                history_section = f"Previous conversation:\n{conversation_history}\n\n"
            
            prompt = f"""<s>[INST] You are NEU University AI, a helpful assistant for Near East University.

{history_section}Student: "{query}"

University information:
{context}

Guidelines:
- Answer naturally and conversationally
- Pay attention to specific years/semesters in the data
- If student asked about a program earlier in conversation, use that context

- Use appropriate emojis (📚 courses, 🎓 programs, 🚌 bus, ⏰ times, 💰 fees)

**Formatting:**
- Use Markdown tables for course lists
- Use bullet points for lists
- Use **bold** for emphasis
- Never use hashtags (#)

Provide a helpful answer:
[/INST]"""

            response = llm(
                prompt,
                max_tokens=400,
                temperature=0.7,
                top_p=0.9,
                echo=False,
                stop=["</s>", "[INST]"]
            )
            
            text = extract_llm_text(response)
            return clean_llm_response(text) if text else "I don't have that information."
        
        except Exception as e:
            print(f"❌ LLM error: {e}")
    
    return "I'm here to help with Near East University questions."


def get_general_response(query: str, conversation_history: str = "", llm=None) -> str:
    """Handle general conversation"""
    print(f"💬 General conversation: '{query}'")
    
    if llm:
        try:
            history_section = ""
            if conversation_history and len(conversation_history) > 20:
                history_section = f"Previous conversation:\n{conversation_history}\n\n"
            
            prompt = f"""<s>[INST] You are NEU AI, a friendly assistant for Near East University.

{history_section}Student: "{query}"

Guidelines:
- Be natural and conversational
- For questions about yourself, explain you're an AI assistant for NEU students
- Don't make up university data
- Keep responses brief and friendly
- Use appropriate emojis naturally

Respond naturally:
[/INST]"""

            response = llm(
                prompt,
                max_tokens=150,
                temperature=0.7,
                top_p=0.9,
                echo=False,
                stop=["</s>", "[INST]"]
            )
            
            text = extract_llm_text(response)
            return clean_llm_response(text) if text else "I'm here to help!"
        
        except Exception as e:
            print(f"❌ LLM error: {e}")
    
    return "I'm NEU AI, your assistant for Near East University. How can I help you today?"



def get_fallback_classification(query: str, conversation_history: str, llm) -> str:
    """
    Fallback classification using content analysis
    """
    # Check if query seems to be about university topics using semantic similarity
    query_lower = query.lower()
    
    # Use embeddings to check similarity with university-related concepts
    try:
        # Generate a simple relevance check
        university_check = f"""<s>[INST] Rate from 0-10 how much this question relates to university services, courses, or campus information:

Question: "{query}"

Just respond with a number 0-10.
[/INST]"""
        
        if llm:
            response = llm(
                university_check,
                max_tokens=5,
                temperature=0.1,
                echo=False
            )
            
            score_text = extract_llm_text(response).strip()
            try:
                score = float(''.join(c for c in score_text if c.isdigit() or c == '.'))
                
                if score >= 6:
                    return get_university_response(query, conversation_history, llm)
                else:
                    return get_general_response(query, conversation_history, llm)
            except:
                pass
    except:
        pass
    
    # Default to general for safety
    return get_general_response(query, conversation_history, llm)



def calculate_semantic_relevance(query: str, content: str) -> float:
    """
    Calculate semantic relevance using embeddings instead of keyword matching
    """
    try:
        # Use sentence embeddings for semantic similarity
        query_embedding = embedder.encode([query])[0]
        content_embedding = embedder.encode([content[:500]])[0]  # Limit content length for performance
        
        # Calculate cosine similarity
        similarity = np.dot(query_embedding, content_embedding) / (
            np.linalg.norm(query_embedding) * np.linalg.norm(content_embedding)
        )
        
        # Normalize to 0-1 range
        return max(0, min(1, similarity))
    except Exception as e:
        print(f"Error calculating semantic relevance: {e}")
        return 0.0




# Remove all these hardcoded functions - they're not needed
# - remove_all_excess_content()
# - balance_response_length() 
# - remove_repetitive_phrases()
# - All the if/else hardcoded logic

# ==========================================
# Enhanced Smart Query (Pure Semantic)
# ==========================================
def smart_query_collection(collection, query: str, n_results: int = 5) -> Dict[str, Any]:
    """Pure semantic querying - NO HARCODED LOGIC"""
    results = {'documents': [], 'metadatas': [], 'distances': [], 'relevance_scores': []}
    
    try:
        # Simple semantic search - let embeddings handle everything
        semantic_results = collection.query(
            query_texts=[query],
            n_results=n_results * 3,  # Get more results for better selection
            include=['documents', 'metadatas', 'distances']
        )
        
        if semantic_results and semantic_results.get('documents') and semantic_results['documents'][0]:
            for i, doc in enumerate(semantic_results['documents'][0]):
                if doc and doc.strip():
                    # Pure distance-based similarity
                    distance = semantic_results['distances'][0][i] if semantic_results.get('distances') else 1.0
                    similarity_score = 1.0 / (1.0 + distance)
                    
                    # Content quality bonus (longer, more structured content)
                    content_quality = min(len(doc) / 500, 0.3)  # Small bonus for good content
                    final_score = similarity_score + content_quality
                    
                    results['documents'].append(doc)
                    results['metadatas'].append(semantic_results['metadatas'][0][i] if semantic_results.get('metadatas') else {})
                    results['distances'].append(distance)
                    results['relevance_scores'].append(final_score)
        
        # Sort by relevance
        if results['documents']:
            sorted_indices = sorted(range(len(results['relevance_scores'])), 
                                  key=lambda i: results['relevance_scores'][i], reverse=True)
            for key in results:
                results[key] = [results[key][i] for i in sorted_indices]
        
        # Keep top results
        for key in results:
            results[key] = results[key][:n_results]
        
    except Exception as e:
        print(f"Error querying collection {collection.name}: {e}")
    
    return results
