import chromadb
from chromadb.utils import embedding_functions

def add_architecture_curriculum_to_chromadb():
    """Add Architecture (English) curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_architecture_english",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_architecture_english",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_architecture_english")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF ARCHITECTURE
DEPARTMENT OF ARCHITECTURE (ENGLISH)
Bachelor of Architecture

Program Duration: 4 years (8 semesters)
Language of Instruction: English
Total ECTS for Graduation: 240

Main website: https://aif.neu.edu.tr/
Curriculum link: https://mimarlik.neu.edu.tr/academic/academic-programmes/department-of-architecture-english/curriculum-after-2021/?lang=en

Legend:
Theory = Theoretical Hours
Application/Laboratory = Practical/Lab Hours
Local Credits = Credit Hours
ECTS = European Credit Transfer System""",

        # 1st Year - 1st Semester
        """First Year - Fall Semester - Compulsory Courses:
ARC101, Basics of Architectural Design I, Theory:4, Application:4, Credits:6, ECTS:9, Prerequisite: None
ARC103, Visual Communication Techniques I, Theory:2, Application:2, Credits:3, ECTS:6, Prerequisite: None
ARC105, Introduction to Architectural Concepts, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
MTH141, Mathematics for Designers, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
CAM100, Campus Orientation, Theory:0, Application:0, Credits:0, ECTS:2, Prerequisite: None
TUR101/YIT101, Turkish Language I/Turkish Language for Foreign Students I, Theory:2, Application:0, Credits:2, ECTS:2, Prerequisite: None
ENG101, Foreign Language I, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
AIT101/AIT103, Atatürk's Principles and the History of Turkish Revolution I, Theory:2, Application:0, Credits:2, ECTS:2, Prerequisite: None

Total Semester ECTS: 30""",

        # 1st Year - 2nd Semester
        """First Year - Spring Semester - Compulsory Courses:
ARC102, Basics of Architectural Design II, Theory:4, Application:4, Credits:6, ECTS:9, Prerequisite: ARC101
ARC104, Visual Communication Techniques II, Theory:2, Application:2, Credits:3, ECTS:3, Prerequisite: ARC103
ARC106, Construction and Materials I, Theory:2, Application:2, Credits:3, ECTS:4, Prerequisite: None
ARC108, Humanities, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
CAR100, Career Planning, Theory:0, Application:0, Credits:0, ECTS:2, Prerequisite: None
TUR102/YIT102, Turkish Language II/Turkish Language for Foreign Students II, Theory:2, Application:0, Credits:2, ECTS:2, Prerequisite: TUR101/YIT101
AIT102/AIT104, Ataturk's Principles and the History of Turkish Revolution II, Theory:2, Application:0, Credits:2, ECTS:2, Prerequisite: AIT101/AIT103
ENG102, Foreign Language II, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
GCE/GECXXX, Elective 1, Theory:2, Application:2, Credits:2, ECTS:2, Prerequisite: None

Total Semester ECTS: 30""",

        # 2nd Year - 1st Semester
        """Second Year - Fall Semester - Compulsory Courses:
ARC201, Architectural Design I, Theory:4, Application:4, Credits:6, ECTS:10, Prerequisite: ARC102
ARC203, Computer Aided Drawing I, Theory:2, Application:2, Credits:3, ECTS:4, Prerequisite: None
ARC205, Construction and Materials II, Theory:2, Application:2, Credits:3, ECTS:4, Prerequisite: None
ARC207, History of Art and Architecture I, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC209, Statics and Mechanics, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC213, Freehand Drawing Techniques and Architecture, Theory:2, Application:2, Credits:3, ECTS:3, Prerequisite: None
ARC110, Surveying, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None

Total Semester ECTS: 30""",

        # 2nd Year - 2nd Semester
        """Second Year - Spring Semester - Compulsory Courses:
ARC202, Architectural Design II, Theory:4, Application:4, Credits:6, ECTS:10, Prerequisite: ARC201
ARC204, Advanced Computer Applications, Theory:2, Application:2, Credits:3, ECTS:3, Prerequisite: None
ARC206, Construction and Materials III, Theory:2, Application:2, Credits:3, ECTS:3, Prerequisite: None
ARC208, History of Art and Architecture II, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC212, Environmental Control Systems I, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
FAEXXX, Elective, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC200, Summer Practice I, Theory:0, Application:0, Credits:0, ECTS:5, Prerequisite: None

Total Semester ECTS: 30""",

        # 3rd Year - 1st Semester
        """Third Year - Fall Semester - Compulsory Courses:
ARC301, Architectural Design III, Theory:4, Application:4, Credits:6, ECTS:12, Prerequisite: ARC202
ARC303, Behavioural Analysis of Structures, Theory:3, Application:0, Credits:3, ECTS:4, Prerequisite: None
ARC305, Architecture of the 20th Century, Theory:3, Application:0, Credits:3, ECTS:4, Prerequisite: None
ARC307, Environmental Control Systems II, Theory:3, Application:0, Credits:3, ECTS:4, Prerequisite: None
ARCXXX, Elective, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
FAEXXX, Elective, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None

Total Semester ECTS: 30""",

        # 3rd Year - 2nd Semester
        """Third Year - Spring Semester - Compulsory Courses:
ARC302, Architectural Design IV, Theory:4, Application:4, Credits:6, ECTS:12, Prerequisite: ARC301
ARC304, Planning and Urban Design, Theory:2, Application:4, Credits:4, ECTS:4, Prerequisite: None
ARC300, Summer Training II, Theory:0, Application:0, Credits:0, ECTS:5, Prerequisite: None
ARCXXX, Elective, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
FAEXXX, Elective, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
GCE/GECXXX, Elective, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None

Total Semester ECTS: 30""",

        # 4th Year - 1st Semester
        """Fourth Year - Fall Semester - Compulsory Courses:
ARC401, Architectural Design V, Theory:4, Application:4, Credits:6, ECTS:12, Prerequisite: ARC302
ARC403, Construction Management, Theory:2, Application:2, Credits:3, ECTS:4, Prerequisite: None
ARC405, Theory of Restoration & Conservation, Theory:3, Application:0, Credits:3, ECTS:5, Prerequisite: None
ARCXXX, Elective, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARCXXX, Elective, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
GCE/GECXXX, Elective, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None

Total Semester ECTS: 30""",

        # 4th Year - 2nd Semester
        """Fourth Year - Spring Semester - Compulsory Courses:
ARC402, Architectural Design VII, Theory:4, Application:4, Credits:6, ECTS:15, Prerequisite: ARC401
ARC404, Legal Aspects of Planning, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC406, Professional Practice and Ethics, Theory:3, Application:2, Credits:4, ECTS:6, Prerequisite: None
ARCXXX, Elective, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
FAEXXX, Elective, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None

Total Semester ECTS: 30

Program Total ECTS: 240""",

        # Architecture Elective Courses
        """Architecture Department Elective Courses (ARC XXX):
ARC412, Quantities, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC414, Model Making, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC410, Landscape Design, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC421, Solar Energy, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC424, Basic Art Education, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC436, Steel Construction, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC446, String Art, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC447, Urban Design Analysis, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC430, Topography, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC407, Housing In Rural Area, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC454, Light In Architecture, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC437, Architecture and Sustainability, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC444, Computer Presentation Techniques, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC434, Large-Span Structures in Architecture, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC450, Seminars on Architectural Monuments, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC466, Descriptive Analysis of Buildings, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC481, Reinforced Concrete Theory, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC467, Environmental Conservation, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC362, Energy Efficient Buildings, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC413, Introduction to Deterioration & Conservation in Historical Buildings, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
ARC409, Formation & Development of Traditional Turkish House, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None""",

        # Faculty of Architecture Elective Courses
        """Faculty of Architecture Elective Courses (FAE XXX):
FAE453, Topographical Modelling, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
FAE457, Introduction to Geographical Information System, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
FAE490, Site Analysis, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
FAE488, Architecture and Photography, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
FAE486, Poster Design, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
FAE352, Cultural Issues in Design, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
FAE387, Digital Communication in Architecture, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
FAE482, Renewable Energy Sources, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
FAE476, Determination of Medium Scale Hospital Needs Programme, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
FAE452, Prefabricated Construction Systems, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
FAE449, Introduction to Architectural Structure, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
FAE455, The Limits of Architectural Criticism, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None
FAE487, Rhinoceras, Theory:3, Application:0, Credits:3, ECTS:3, Prerequisite: None""",

        # Program Summary and Career Opportunities
        """Architecture Program Summary (English):
Degree: Bachelor of Architecture
Duration: 4 years (8 semesters)
Language of Instruction: English
Total ECTS: 240

Program Focus Areas:
- Architectural Design and Studio Work
- Building Construction and Materials
- History and Theory of Architecture
- Environmental Control Systems
- Urban Design and Planning
- Digital Design and Visualization
- Structural Systems and Mechanics
- Professional Practice and Ethics
- Restoration and Conservation

Career Opportunities:
Architect
Urban Designer
Interior Architect
Construction Project Manager
Building Information Modeling (BIM) Specialist
Heritage Conservation Specialist
Sustainable Design Consultant
Architectural Visualizer
Academic and Research Positions
Government Planning Departments
Real Estate Development

Professional Recognition:
Graduates are qualified to work in architectural firms, construction companies, urban planning departments, heritage conservation organizations, and various design-related industries worldwide. The program prepares students for professional licensure and advanced studies in architecture."""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Architecture",
            "department": "Architecture (English)",
            "degree": "Bachelor",
            "language": "English",
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
            "elective_type": "departmental",
            "document_type": "course_list",
            "content_type": "architecture_electives"
        },
        {
            "course_type": "elective",
            "elective_type": "faculty",
            "document_type": "course_list",
            "content_type": "faculty_electives"
        },
        {
            "document_type": "program_info",
            "content_type": "program_summary_careers"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"architecture_eng_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Architecture (English) curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["architectural design studio construction"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_architecture_curriculum_to_chromadb()