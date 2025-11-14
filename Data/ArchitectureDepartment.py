import chromadb
from chromadb.utils import embedding_functions

def add_architecture_to_chromadb():
    """Add Architecture Department curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_architecture",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_architecture",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_architecture")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """Near East University Faculty of Architecture
Department of Architecture (Turkish Program)
Main website link: https://neu.edu.tr/academic/faculties/
Academic Program link: https://mimarlik.neu.edu.tr/academic/academic-programmes/department-of-architecture-english/curriculum-2018-2019/""",

        # First Year Fall Semester
        """First Year - Fall Semester Courses (Year One or 1 First Semester):
IAR101, Basics Of Interior Design I, Credits: 6
IAR103, Colour Theory And Presentation, Credits: 3
IAR105, Visual Communication-Technical Drawing, Credits: 3
IAR107, Freehand Drawing, Credits: 3
IAR109, Introduction of Concepts of Interior Architecture, Credits: 3
ENG101, Foreign Language I, Credits: 3
TUR/YIT101, Turkish Language I, Credits: 2
CAM100, Campus Orientation, Credits: 0""",

        # First Year Spring Semester
        """First Year - Spring Semester Courses (Year One or 1 Second Semester):
IAR102, Basics of Interior Design II, Credits: 6
IAR104, Space Planning, Credits: 3
IAR106, Descriptive Geometry, Credits: 3
GCE/GEC000, University Elective, Credits: 2
ENG102, Foreign Language II, Credits: 3
TUR/YIT102, Turkish Language II, Credits: 2
INAR100, Summer Training I: Construction, Credits: 0
CAR100, Carrier Planning, Credits: 0""",

        # Second Year Fall Semester
        """Second Year - Fall Semester Courses (Year Two or 2 First Semester):
IAR201, Interior Design Studio I, Credits: 6
IAR203, Digital Presentation Techniques II, Credits: 3
IAR205, Environmental Design, Credits: 3
IAR207, Construction and Materials I, Credits: 3
IAR209, History of Interior Architecture and Furniture, Credits: 3
IAR211, Preservation of Historic Interiors: History And Theory, Credits: 4
IAR213, Human Factors And Ergonomics in Interior Design, Credits: 3""",

        # Second Year Spring Semester
        """Second Year - Spring Semester Courses (Year Two or 2 Second Semester):
IAR202, Interior Design Studio II, Credits: 6
IAR204, Digital Presentation Techniques II, Credits: 3
IAR206, Computer Aided Drawing I, Credits: 3
IAR208, Construction And Materials II, Credits: 3
IAR212, Restoration, Credits: 3
IAR214, History of Contemporary Interior Architecture and Furniture, Credits: 3
IAR200, Summer Training II - Atelier, Credits: 0""",

        # Third Year Fall Semester
        """Third Year - Fall Semester Courses (Year Three or 3 First Semester):
IAR301, Interior Design Studio III, Credits: 6
IAR303, Advanced Digital Presentation, Credits: 4
IAR305, Environmental Control and Mechanical Equipment, Credits: 3
IAR307, Detailing Studio - Product Detailing, Credits: 4
IAR309, Environmental Control, Credits: 3
IAR000, Departmental Elective, Credits: 3
AIT101/AIT103, Atatürk's Principles and the History of Turkish Revolution, Credits: 2""",

        # Third Year Spring Semester
        """Third Year - Spring Semester Courses (Year Three or 3 Second Semester):
IAR302, Interior Design Studio IV, Credits: 6
IAR304, Furniture Design, Credits: 4
IAR306, Universal Design: Special Use and Users, Credits: 3
IAR308, Story of Humanities, Credits: 3
IAR000, Departmental Elective, Credits: 3
AIT102/AIT104, Atatürk's Principles and the History of Turkish Revolution (II), Credits: 2
IAR300, Summer Training III - Office, Credits: 5""",

        # Fourth Year Fall Semester
        """Fourth Year - Fall Semester Courses (Year Four or 4 First Semester - Final Year First Semester):
IAR401, Interior Design Studio V, Credits: 6
IAR403, Theory of Interior Architecture, Credits: 3
IAR405, Building Economics in Interior Architecture, Credits: 3
IAR000, Departmental Elective, Credits: 3
IAR000, Departmental Elective, Credits: 3
GEC/GCE000, University Elective, Credits: 3""",

        # Fourth Year Spring Semester
        """Fourth Year - Spring Semester Courses (Year Four or 4 Second Semester - Final Year Second Semester):
IAR402, Graduation Project, Credits: 6
IAR404, Interior Design Professional Practice, Credits: 3
IAR406, Portfolio Design, Credits: 3
IAR000, Departmental Elective, Credits: 2
FAE000, Faculty Elective, Credits: 3""",

        # Elective Courses
        """Departmental Elective Courses:
INAR429, Colour Concept In Architecture, Credits: 3
INAR435, Problem Design, Credits: 3
IAR488, Accessory Design, Credits: 3
IAR322, Watercolour Techniques In Interior Design, Credits: 3
INAR424, Basic Art Education, Credits: 3
IAR432, Advanced Sketching And Rendering Techniques, Credits: 3
INAR478, Advanced Illustration, Credits: 3
IAR454, Architectural Lighting, Credits: 3
IAR324, Nature Inspired Design, Credits: 3
FAE489, Illustration, Credits: 3
INAR487, Accessory Design in Space, Credits: 3
INAR433, Interior Textiles, Credits: 3
INAR428, Planning Techniques, Credits: 3
INAR427, Freehand Drawing, Credits: 3
FAE443, Interior Design Approaches in Architectural Projects, Credits: 3
INAR360, Industrial Design, Credits: 3
FAE352, Cultural Issues in Design, Credits: 3""",

        # Course Descriptions - Core Design Studios
        """Course Descriptions - Core Design Studio Courses:

IAR101, Basics Of Interior Design I, Credits: 6
Fundamental principles of interior design, basic design concepts, spatial organization, and introductory design projects.

IAR102, Basics of Interior Design II, Credits: 6
Continuation of basic interior design principles with more complex spatial problems and design solutions.

IAR201, Interior Design Studio I, Credits: 6
Intermediate level interior design projects focusing on residential spaces and small-scale commercial projects.

IAR202, Interior Design Studio II, Credits: 6
Advanced residential and commercial interior design projects with emphasis on technical integration.

IAR301, Interior Design Studio III, Credits: 6
Complex interior design projects involving specialized spaces and integrated building systems.

IAR302, Interior Design Studio IV, Credits: 6
Advanced interior architecture projects with focus on innovative design solutions and comprehensive technical integration.

IAR401, Interior Design Studio V, Credits: 6
Professional level interior design projects demonstrating comprehensive design capabilities and technical proficiency.

IAR402, Graduation Project, Credits: 6
Capstone project demonstrating comprehensive knowledge and skills in interior architecture and design.""",

        # Course Descriptions - Technical and History Courses
        """Course Descriptions - Technical, History and Specialized Courses:

IAR103, Colour Theory And Presentation, Credits: 3
Principles of color theory, color psychology, and application of color in interior design presentations.

IAR105, Visual Communication-Technical Drawing, Credits: 3
Technical drawing techniques, orthographic projection, and architectural graphics for interior design.

IAR107, Freehand Drawing, Credits: 3
Freehand drawing, sketching techniques, perspective drawing and visual representation for designers.

IAR109, Introduction of Concepts of Interior Architecture, Credits: 3
Overview of interior architecture profession, fundamental concepts, and historical development.

IAR104, Space Planning, Credits: 3
Principles of spatial organization, circulation patterns, and functional planning in interior spaces.

IAR106, Descriptive Geometry, Credits: 3
Geometric principles and projection techniques for spatial representation in design.

IAR203, Digital Presentation Techniques II, Credits: 3
Advanced digital presentation methods including 2D and 3D visualization techniques.

IAR205, Environmental Design, Credits: 3
Sustainable design principles, environmental considerations, and eco-friendly design strategies.

IAR207, Construction and Materials I, Credits: 3
Building construction methods, materials, and structural systems for interior applications.

IAR209, History of Interior Architecture and Furniture, Credits: 3
Historical development of interior architecture and furniture design from ancient to modern periods.

IAR211, Preservation of Historic Interiors: History And Theory, Credits: 4
Theories and practices of historic preservation for interior spaces and architectural conservation.

IAR213, Human Factors And Ergonomics in Interior Design, Credits: 3
Anthropometrics, ergonomic principles, and human-centered design approaches.

IAR404, Interior Design Professional Practice, Credits: 3
Professional ethics, office management, contracts, and business practices in interior architecture.

IAR406, Portfolio Design, Credits: 3
Development of professional design portfolios and presentation materials for career advancement.""",

        # Program Overview and Career Opportunities
        """Architecture Department Program Overview:
Bachelor's Degree program focusing on architectural design, interior architecture, and spatial planning.
Combines artistic design principles with technical knowledge and professional practice.
Includes design studios, technical courses, and professional training.
Prepares students for careers in architecture, interior design, and related fields.

Career Opportunities for Architecture Graduates:
Architect
Interior Architect
Urban Designer
Space Planner
Architectural Designer
Project Manager
Design Consultant
Construction Manager
Building Information Modeling (BIM) Specialist
Sustainable Design Consultant"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "department": "Architecture",
            "faculty": "Architecture",
            "language": "English Program",
            "document_type": "program_info",
            "content_type": "general_info"
        },
        {
            "year": "1",
            "semester": "1",
            "document_type": "course_list",
            "content_type": "first_year_fall_semester"
        },
        {
            "year": "1",
            "semester": "2",
            "document_type": "course_list",
            "content_type": "first_year_spring_semester"
        },
        {
            "year": "2",
            "semester": "1",
            "document_type": "course_list",
            "content_type": "second_year_fall_semester"
        },
        {
            "year": "2",
            "semester": "2",
            "document_type": "course_list",
            "content_type": "second_year_spring_semester"
        },
        {
            "year": "3",
            "semester": "1",
            "document_type": "course_list",
            "content_type": "third_year_fall_semester"
        },
        {
            "year": "3",
            "semester": "2",
            "document_type": "course_list",
            "content_type": "third_year_spring_semester"
        },
        {
            "year": "4",
            "semester": "1",
            "document_type": "course_list",
            "content_type": "fourth_year_fall_semester"
        },
        {
            "year": "4",
            "semester": "2",
            "document_type": "course_list",
            "content_type": "fourth_year_spring_semester"
        },
        {
            "course_type": "elective",
            "document_type": "course_list",
            "content_type": "departmental_electives"
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
    ids = [f"architecture_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Architecture Department curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["architecture design studio"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_architecture_to_chromadb()