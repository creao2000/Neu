import chromadb
from chromadb.utils import embedding_functions

def add_landscape_architecture_english_to_chromadb():
    """Add Landscape Architecture English Program curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_landscape_architecture_english",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_landscape_architecture_english",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_landscape_architecture_english")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """Near East University Faculty of Architecture
Department of Landscape Architecture (English Program)
Main website link: https://neu.edu.tr/academic/faculties/
Academic Program link: https://ziraat.neu.edu.tr/academic/academic-programmes/landscape-architecture-english-program/courses/""",

        # 1st Semester
        """First Year - First Semester Courses (Year One or 1 First Semester):
INAR 101, Basic Design, Credit: 6
INAR 104, Basic Art Education, Credit: 3
INAR 105, Drawing, Credit: 3
INAR 111, Design Methods in Interior Architecture, Credit: 3
INAR 121, Introduction to Interior Architecture, Credit: 3
ENG 101, Development of Reading and Writing Skills I, Credit: 3
TUR 101, Turkish, Credit: 2""",

        # 2nd Semester
        """First Year - Second Semester Courses (Year One or 1 Second Semester):
INAR 102, Introduction to Interior Architecture, Credit: 6
INAR 103, Graphic Communication, Credit: 3
INAR 114, Space Planning, Credit: 3
INAR 122, Interior Architecture and Aesthetics, Credit: 3
INAR 164, History of Art and Architecture, Credit: 3
ENG 102, Development of Reading and Writing Skills II, Credit: 3
INAR 100, Summer Training I, Credit: 0""",

        # 3rd Semester
        """Second Year - First Semester Courses (Year Two or 2 First Semester):
INAR 201, Interior Architecture Studio I, Credit: 6
INAR 203, Presentation Techniques, Credit: 3
INAR 212, Computer Aided Design I, Credit: 3
INAR 214, Restoration, Credit: 3
INAR 221, Human Factors in Interior Architecture, Credit: 3
INAR 251, Construction I, Credit: 3
INAR 263, History of Interior Architecture and Furniture from Egyptian Period, Credit: 3""",

        # 4th Semester
        """Second Year - Second Semester Courses (Year Two or 2 Second Semester):
INAR 202, Interior Architecture Studio II, Credit: 6
INAR 213, Computer Aided Design II, Credit: 3
INAR 222, Building Material and Components of Interior Elements, Credit: 3
INAR 244, Environmental Control: Physical Factors, Credit: 3
INAR 252, Construction II, Credit: 3
INAR 264, History of Interior Architecture and Furniture from 1900 to today, Credit: 3
INAR 200, Summer Training II, Credit: 0""",

        # 5th Semester
        """Third Year - First Semester Courses (Year Three or 3 First Semester):
INAR 301, Interior Architecture Studio III, Credit: 6
INAR 312, Computer Aided Design III, Credit: 3
INAR 341, Environmental Control: Mechanical Equipment II, Credit: 3
INAR 351, Detailing Studio, Credit: 3
INAR 358, Arts and Crafts, Credit: 3
INAR xxx, Elective, Credit: 3""",

        # 6th Semester
        """Third Year - Second Semester Courses (Year Three or 3 Second Semester):
INAR 302, Interior Architecture Studio IV, Credit: 6
INAR 307, Furniture Design, Credit: 3
INAR 342, Building Performance: Special Use and Users, Credit: 3
INAR 364, Theory of Interior Architecture, Credit: 3
INAR 381, Product Detailing, Credit: 3
INAR xxx, Elective, Credit: 3""",

        # 7th Semester
        """Fourth Year - First Semester Courses (Year Four or 4 First Semester - Final Year First Semester):
INAR 401, Interior Architecture Studio V, Credit: 6
INAR 403, Ergonomics, Credit: 3
INAR 407, Preservation of Historic Interiors: History and Theory, Credit: 3
INAR 417, Building Economics in Interior Architecture, Credit: 3
INAR xxx, Elective, Credit: 3""",

        # 8th Semester
        """Fourth Year - Second Semester Courses (Year Four or 4 Second Semester - Final Year Second Semester):
INAR 402, Graduation Project, Credit: 6
INAR 418, Professional Practice: Interior Architecture, Credit: 3
INAR xxx, Elective, Credit: 3
AIT 101-102, Atatürk's Principles and History of Turkish Republic, Credit: 2
INAR 300, Summer Training III, Credit: 0""",

        # Course Descriptions - Core Design Courses
        """Course Descriptions - Core Design and Studio Courses:

INAR 101, Basic Design, Credit: 6
Fundamental principles of design, elements and principles of visual organization, basic design concepts and applications.

INAR 102, Introduction to Interior Architecture, Credit: 6
Introduction to interior architecture profession, basic design principles, spatial organization and functional requirements.

INAR 201, Interior Architecture Studio I, Credit: 6
Advanced interior design projects focusing on residential spaces, programming, space planning and design development.

INAR 202, Interior Architecture Studio II, Credit: 6
Intermediate level interior design projects with emphasis on commercial and public spaces.

INAR 301, Interior Architecture Studio III, Credit: 6
Complex interior design projects involving specialized spaces and integrated building systems.

INAR 302, Interior Architecture Studio IV, Credit: 6
Advanced interior architecture projects with focus on innovative design solutions and technical integration.

INAR 401, Interior Architecture Studio V, Credit: 6
Comprehensive interior design projects demonstrating professional level design capabilities.

INAR 402, Graduation Project, Credit: 6
Capstone project demonstrating comprehensive knowledge and skills in interior architecture.""",

        # Course Descriptions - Technical and History Courses
        """Course Descriptions - Technical, History and Specialized Courses:

INAR 103, Graphic Communication, Credit: 3
Technical drawing, orthographic projection, architectural graphics and visual communication techniques.

INAR 105, Drawing, Credit: 3
Freehand drawing, sketching techniques, perspective drawing and visual representation.

INAR 111, Design Methods in Interior Architecture, Credit: 3
Design methodologies, creative problem-solving approaches and design process in interior architecture.

INAR 121, Introduction to Interior Architecture, Credit: 3
Overview of interior architecture profession, historical development and contemporary practice.

INAR 164, History of Art and Architecture, Credit: 3
Historical survey of art and architecture from ancient to modern periods.

INAR 203, Presentation Techniques, Credit: 3
Advanced presentation methods including digital and manual techniques for design communication.

INAR 212, Computer Aided Design I, Credit: 3
Introduction to CAD software and digital tools for interior architecture.

INAR 213, Computer Aided Design II, Credit: 3
Advanced CAD applications, 3D modeling and rendering techniques.

INAR 214, Restoration, Credit: 3
Principles and techniques of architectural restoration and conservation.

INAR 221, Human Factors in Interior Architecture, Credit: 3
Anthropometrics, ergonomics and human-centered design principles.

INAR 251, Construction I, Credit: 3
Building construction methods, materials and structural systems.

INAR 252, Construction II, Credit: 3
Advanced construction techniques and detailing in interior architecture.

INAR 263, History of Interior Architecture and Furniture from Egyptian Period, Credit: 3
Historical development of interior architecture and furniture design from ancient Egyptian to pre-modern periods.

INAR 264, History of Interior Architecture and Furniture from 1900 to today, Credit: 3
Modern and contemporary interior architecture and furniture design from 1900 to present.

INAR 307, Furniture Design, Credit: 3
Principles of furniture design, materials, construction and ergonomic considerations.

INAR 312, Computer Aided Design III, Credit: 3
Advanced digital design tools, BIM applications and parametric design.

INAR 341, Environmental Control: Mechanical Equipment II, Credit: 3
Mechanical systems, HVAC, lighting and acoustic design in interior spaces.

INAR 342, Building Performance: Special Use and Users, Credit: 3
Design for special populations, accessibility and specialized building functions.

INAR 351, Detailing Studio, Credit: 3
Technical detailing, construction documents and specification writing.

INAR 358, Arts and Crafts, Credit: 3
Traditional and contemporary arts and crafts applications in interior design.

INAR 364, Theory of Interior Architecture, Credit: 3
Theoretical foundations, critical thinking and design theories in interior architecture.

INAR 381, Product Detailing, Credit: 3
Product design, manufacturing processes and material specifications.

INAR 403, Ergonomics, Credit: 3
Advanced ergonomic principles and applications in interior design.

INAR 407, Preservation of Historic Interiors: History and Theory, Credit: 3
Historic preservation theories and practices for interior spaces.

INAR 417, Building Economics in Interior Architecture, Credit: 3
Cost estimation, budgeting and economic considerations in interior architecture projects.

INAR 418, Professional Practice: Interior Architecture, Credit: 3
Professional ethics, office management, contracts and business practices in interior architecture.""",

        # Program Overview and Career Opportunities
        """Landscape Architecture English Program Overview:
Bachelor's Degree program in English focusing on landscape design, environmental planning, and sustainable design.
Combines artistic design principles with environmental science and technical knowledge.
Includes studio-based learning, technical courses, and professional practice.
Prepares students for careers in landscape architecture, environmental design, and urban planning.

Career Opportunities for Landscape Architecture Graduates:
Landscape Architect
Environmental Designer
Urban Planner
Site Planner
Park Designer
Residential Landscape Designer
Commercial Landscape Designer
Environmental Consultant
Project Manager in Landscape Architecture"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "department": "Landscape Architecture",
            "faculty": "Architecture",
            "language": "English Program",
            "document_type": "program_info",
            "content_type": "general_info"
        },
        {
            "year": "1",
            "semester": "1",
            "document_type": "course_list",
            "content_type": "first_year_first_semester"
        },
        {
            "year": "1",
            "semester": "2",
            "document_type": "course_list",
            "content_type": "first_year_second_semester"
        },
        {
            "year": "2",
            "semester": "1",
            "document_type": "course_list",
            "content_type": "second_year_first_semester"
        },
        {
            "year": "2",
            "semester": "2",
            "document_type": "course_list",
            "content_type": "second_year_second_semester"
        },
        {
            "year": "3",
            "semester": "1",
            "document_type": "course_list",
            "content_type": "third_year_first_semester"
        },
        {
            "year": "3",
            "semester": "2",
            "document_type": "course_list",
            "content_type": "third_year_second_semester"
        },
        {
            "year": "4",
            "semester": "1",
            "document_type": "course_list",
            "content_type": "fourth_year_first_semester"
        },
        {
            "year": "4",
            "semester": "2",
            "document_type": "course_list",
            "content_type": "fourth_year_second_semester"
        },
        {
            "course_type": "core",
            "document_type": "course_description",
            "content_type": "design_studio_courses"
        },
        {
            "course_type": "core",
            "document_type": "course_description", 
            "content_type": "technical_history_courses"
        },
        {
            "document_type": "program_info",
            "content_type": "program_overview_careers"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"landscape_arch_english_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Landscape Architecture English Program curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["landscape architecture design studio"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_landscape_architecture_english_to_chromadb()