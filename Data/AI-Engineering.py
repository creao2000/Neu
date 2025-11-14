import chromadb
from chromadb.utils import embedding_functions

def add_ai_engineering_curriculum_to_chromadb():
    """Add Artificial Intelligence Engineering curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_ai_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_ai_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_ai_engineering")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """Near East University Faculty of Artificial Intelligence and Informatics
Department of Artificial Intelligence Engineering Bachelor's Degree
Main website link: https://aif.neu.edu.tr/
Academic Program link: https://aif.neu.edu.tr/""",

        # First Year First Semester
        """First Year - First Semester Courses (Year One or 1 First Semester - Fall):
MTH113, Linear Algebra, Credit 3, ECTS 5
AII102, Programming and Problem Solving, Credit 4, ECTS 5
ENG101, English I, Credit 2, ECTS 3
MTH101, Calculus I, Credit 4, ECTS 5
PHY101, General Physics I, Credit 4, ECTS 5
CAM100, Campus Orientation, Credit 0, ECTS 2
CHM101, General Chemistry I, Credit 4, ECTS 5""",

        # First Year Second Semester
        """First Year - Second Semester Courses (Year One or 1 Second Semester - Spring):
AII104, Discrete Structures, Credit 3, ECTS 5
ENG102, English II, Credit 2, ECTS 3
MTH102, Calculus II, Credit 4, ECTS 6
PHY102, General Physics II, Credit 4, ECTS 6
AII108, Object Oriented Programming, Credit 3, ECTS 6
CAR100, Career Planning, Credit 0, ECTS 2
GEC351, 21st Century Skills, Credit 0, ECTS 2""",

        # Second Year First Semester
        """Second Year - First Semester Courses (Year Two or 2 First Semester - Fall):
AII001, Logic Design, Credit 4, ECTS 6
AII201, Data Structures & Algorithms, Credit 4, ECTS 6
AIE201, AI Principles and Techniques, Credit 3, ECTS 3
MTH201, Differential Equations, Credit 4, ECTS 6
AII007, Multimedia Systems, Credit 3, ECTS 5
AIT103, Atatürk Principles and Reforms I, Credit 2, ECTS 2
YIT101, Turkish for Foreigners I, Credit 2, ECTS 2""",

        # Second Year Second Semester
        """Second Year - Second Semester Courses (Year Two or 2 Second Semester - Spring):
AII202, Database Management Systems, Credit 4, ECTS 5
AIE206, Reasoning and Agents in AI, Credit 4, ECTS 7
MTH251, Probability and Statistics, Credit 3, ECTS 6
AIT104, Atatürk Principles and Reforms II, Credit 2, ECTS 2
AIE299, Summer Training I, Credit 0, ECTS 6
CHC100, Cyprus History and Culture, Credit 0, ECTS 2
YIT102, Turkish for Foreigners II, Credit 2, ECTS 2""",

        # Third Year First Semester
        """Third Year - First Semester Courses (Year Three or 3 First Semester - Fall):
AII302, Operating Systems, Credit 3, ECTS 6
AIE301, Pattern Recognition, Credit 3, ECTS 5
ENG201, Oral Communication Skills, Credit 3, ECTS 4
AIE303, Natural Language Processing, Credit 3, ECTS 3
AII439, Occupational Health and Safety I, Credit 2, ECTS 4
AII427, Management for Engineers, Credit 3, ECTS 5
AIE204, Neural Computation, Credit 3, ECTS 3""",

        # Third Year Second Semester
        """Third Year - Second Semester Courses (Year Three or 3 Second Semester - Spring):
AIE302, Introduction to Machine Learning, Credit 4, ECTS 7
AII303, Data Communications and Networking, Credit 4, ECTS 5
AIE304, Learning in Humans, Credit 3, ECTS 5
AIE306, Deep Learning, Credit 3, ECTS 5
AII440, Occupational Health and Safety II, Credit 3, ECTS 2
AIE399, Summer Training II, Credit 0, ECTS 6""",

        # Fourth Year First Semester
        """Fourth Year - First Semester Courses (Year Four or 4 First Semester - Final Year First Semester - Fall):
AIE401, Introduction to Robotics, Credit 3, ECTS 7
AIE403, Computer Vision, Credit 3, ECTS 7
AIE491, Senior Project I, Credit 3, ECTS 6
Technical Elective, Credit 3, ECTS 5
Technical Elective, Credit 3, ECTS 5""",

        # Fourth Year Second Semester
        """Fourth Year - Second Semester Courses (Year Four or 4 Second Semester - Final Year Second Semester - Spring):
AII429, Engineering Ethics, Credit 3, ECTS 6
AIE492, Senior Project II, Credit 4, ECTS 7
AIE402, Speech Processing, Credit 3, ECTS 7
Technical Elective, Credit 3, ECTS 5
Technical Elective, Credit 3, ECTS 5""",

        # Technical Elective Courses
        """Sample Technical Elective Courses:
AII419, Image Processing, Credit 3, ECTS 5
AII415, Decision Making, Credit 3, ECTS 5
AIE411, Advanced Data Analysis, Credit 3, ECTS 5
AIE412, Information Retrieval and Web Search, Credit 3, ECTS 5
AIE413, Human-Robot Interaction, Credit 3, ECTS 5
AIE414, Deep Reinforcement Learning and Control, Credit 3, ECTS 5
AIE415, Mobile Robot Programming, Credit 3, ECTS 5
AIE416, Autonomous Agents, Credit 3, ECTS 5
AIE417, Introduction to Quantum Computing, Credit 3, ECTS 5
AIE418, Computer Animation & Visualization, Credit 3, ECTS 5
AIE419, Algorithmic Game Theory and its Applications, Credit 3, ECTS 5
AIE420, Fuzzy Systems, Credit 3, ECTS 5
AIE458, Artificial Intelligence and Internet of Things, Credit 3, ECTS 5
AIE457, AI and Cloud Computing, Credit 3, ECTS 5""",

        # Course Descriptions - Core AI Courses
        """Core Artificial Intelligence Engineering Courses:

AIE201, AI Principles and Techniques
Introduction to fundamental concepts and techniques in artificial intelligence.

AIE206, Reasoning and Agents in AI
Study of reasoning methods and intelligent agents in AI systems.

AIE301, Pattern Recognition
Techniques for pattern recognition and classification in data.

AIE303, Natural Language Processing
Processing and understanding human language using computational methods.

AIE302, Introduction to Machine Learning
Fundamental concepts and algorithms in machine learning.

AIE306, Deep Learning
Advanced neural networks and deep learning architectures.

AIE401, Introduction to Robotics
Principles and applications of robotics systems.

AIE403, Computer Vision
Image processing and computer vision techniques.

AIE402, Speech Processing
Methods for speech recognition and processing.""",

        # Program Overview
        """Artificial Intelligence Engineering Program Overview:
Bachelor's Degree program focusing on AI technologies, machine learning, robotics, and intelligent systems.
Combines computer science fundamentals with specialized AI courses.
Includes practical training and senior projects.
Prepares students for careers in AI development, research, and implementation.""",

        # Career Opportunities
        """Career Opportunities for AI Engineering Graduates:
AI Engineer
Machine Learning Engineer
Data Scientist
Robotics Engineer
Computer Vision Engineer
Natural Language Processing Specialist
AI Researcher
Intelligent Systems Developer"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "department": "AI Engineering",
            "faculty": "Artificial Intelligence and Informatics",
            "document_type": "program_info",
            "content_type": "general_info"
        },
        {
            "year": "1",
            "semester": "1",
            "season": "Fall",
            "document_type": "course_list",
            "content_type": "first_year_first_semester"
        },
        {
            "year": "1",
            "semester": "2",
            "season": "Spring",
            "document_type": "course_list",
            "content_type": "first_year_second_semester"
        },
        {
            "year": "2",
            "semester": "1",
            "season": "Fall",
            "document_type": "course_list",
            "content_type": "second_year_first_semester"
        },
        {
            "year": "2",
            "semester": "2",
            "season": "Spring",
            "document_type": "course_list",
            "content_type": "second_year_second_semester"
        },
        {
            "year": "3",
            "semester": "1",
            "season": "Fall",
            "document_type": "course_list",
            "content_type": "third_year_first_semester"
        },
        {
            "year": "3",
            "semester": "2",
            "season": "Spring",
            "document_type": "course_list",
            "content_type": "third_year_second_semester"
        },
        {
            "year": "4",
            "semester": "1",
            "season": "Fall",
            "document_type": "course_list",
            "content_type": "fourth_year_first_semester"
        },
        {
            "year": "4",
            "semester": "2",
            "season": "Spring",
            "document_type": "course_list",
            "content_type": "fourth_year_second_semester"
        },
        {
            "course_type": "elective",
            "document_type": "course_list",
            "content_type": "technical_electives"
        },
        {
            "course_type": "core",
            "document_type": "course_description",
            "content_type": "ai_core_courses"
        },
        {
            "document_type": "program_info",
            "content_type": "program_overview"
        },
        {
            "document_type": "program_info", 
            "content_type": "career_opportunities"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"ai_engineering_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} AI Engineering curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["artificial intelligence courses"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_ai_engineering_curriculum_to_chromadb()