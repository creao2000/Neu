import chromadb
from chromadb.utils import embedding_functions

def add_traffic_transportation_curriculum_to_chromadb():
    """Add Traffic and Transportation Engineering curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_traffic_transportation",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_traffic_transportation",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_traffic_transportation")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF CIVIL AND ENVIRONMENTAL ENGINEERING
DEPARTMENT OF TRAFFIC AND TRANSPORTATION ENGINEERING
Bachelor of Science in Traffic and Transportation Engineering

Program Duration: 4 years (8 semesters)
Degree: Bachelor of Science
Total ECTS for Graduation: 240
Total Credits: 158

Main website: https://insaatvecevre.neu.edu.tr/?lang=en
Curriculum link: https://insaatvecevre.neu.edu.tr/wp-content/uploads/sites/136/2023/11/24/TRAFFIC-AND-TRANSPORTATION-ENGINEERING-COURSES.pdf

Legend:
C = Compulsory Course
E = Elective Course
T = Theoretical Hours
P = Practical Hours
C = Credits
E = ECTS Credits""",

        # 1st Semester
        """First Year - First Semester - Compulsory Courses:
ENG101, English I, C, T:2, P:0, C:3, E:3
MTH101, Calculus I, C, T:3, P:2, C:4, E:5
PHY101, General Physics I, C, T:3, P:2, C:4, E:5
CHM101, General Chemistry I, C, T:3, P:2, C:4, E:5
ECC101, Computer Programming, C, T:2, P:2, C:3, E:4
CAM100, Campus Orientation, C, T:0, P:0, C:0, E:0
YIT101, Turkish Language for International Students I, C, T:2, P:0, C:2, E:2
AIT103, Ataturk's Principles and the History of Turkish Revolution I, C, T:2, P:0, C:2, E:2

Elective Course:
CHC100, Cyprus History and Culture, E, T:1, P:0, C:1, E:1

Total: T:22, P:4, C:23, ECTS:27""",

        # 2nd Semester
        """First Year - Second Semester - Compulsory Courses:
ENG102, English II, C, T:3, P:0, C:3, E:3
MTH102, Calculus II, C, T:4, P:0, C:4, E:6
PHY102, General Physics II, C, T:3, P:2, C:4, E:6
GEO102, Geology for Engineering, C, T:3, P:2, C:4, E:6
TD102, Technical Drawing, C, T:2, P:2, C:3, E:4
CAR101, Career Planning, C, T:1, P:0, C:1, E:1
YIT102, Turkish Language for International Students II, C, T:2, P:0, C:2, E:2
AIT104, Ataturk's Principles and the History of Turkish Revolution II, C, T:2, P:0, C:2, E:2

Total: T:20, P:4, C:23, ECTS:30""",

        # 3rd Semester
        """Second Year - Third Semester - Compulsory Courses:
MTH201, Differential Equations and Linear Algebra, C, T:4, P:0, C:4, E:6
MTH251, Statistics and Probability, C, T:3, P:0, C:3, E:6
ECC206, Statics, C, T:3, P:0, C:3, E:5
ECC246, Engineering Economy, C, T:3, P:0, C:3, E:5
TTE241, Materials Science, C, T:4, P:0, C:4, E:6

Elective Course:
NTE, Non-Technical Elective Course, E, T:2, P:0, C:2, E:2

Total: T:19, P:0, C:19, ECTS:30""",

        # 4th Semester
        """Second Year - Fourth Semester - Compulsory Courses:
MTH232, Advanced Calculus, C, T:3, P:0, C:3, E:5
MTH323, Numerical Analysis, C, T:3, P:0, C:3, E:5
TTE204, Surveying, C, T:3, P:2, C:4, E:6
TTE244, Materials of Construction, C, T:3, P:0, C:3, E:5
ECC213, Strength of Materials, C, T:4, P:0, C:4, E:5

Elective Course:
NTE, Non-Technical Elective Course, E, T:2, P:0, C:2, E:2

Total: T:18, P:2, C:19, ECTS:28""",

        # 5th Semester
        """Third Year - Fifth Semester - Compulsory Courses:
TTE306, Computer Applications in Engineering, C, T:2, P:2, C:3, E:6
TTE351, Introduction to Transportation Engineering, C, T:2, P:3, C:4, E:6
TTE361, Soil Mechanics I, C, T:4, P:2, C:4, E:6
TTE371, Fluid Mechanics, C, T:3, P:2, C:4, E:6
TTE381, Structural Analysis I, C, T:3, P:2, C:4, E:6
TTE300, Summer Practice I (30 days), C, T:0, P:0, C:0, E:0

Total: T:14, P:8, C:19, ECTS:30""",

        # 6th Semester
        """Third Year - Sixth Semester - Compulsory Courses:
TTE362, Soil Mechanics II, C, T:4, P:0, C:4, E:6
TTE363, Transportation Systems, C, T:3, P:2, C:4, E:6
TTE364, Pavement Materials and Design, C, T:3, P:2, C:4, E:6
TTE365, Traffic Engineering, C, T:3, P:2, C:4, E:6
TTE366, Highway Design, C, T:2, P:3, C:4, E:6

Total: T:15, P:8, C:20, ECTS:30""",

        # 7th Semester
        """Fourth Year - Seventh Semester - Compulsory Courses:
TTE431, Project Management, C, T:3, P:0, C:3, E:6
TTE432, Geographic Information Systems, C, T:3, P:2, C:4, E:6
TTE433, Railway and Highway Engineering, C, T:3, P:0, C:3, E:6
TTE434, Public Transportation, C, T:3, P:0, C:3, E:6
TTE400, Summer Practice II (30 days), C, T:0, P:0, C:0, E:0

Elective Course:
TE, Technical Elective, E, T:3, P:0, C:3, E:6

Total: T:15, P:2, C:16, ECTS:30""",

        # 8th Semester
        """Fourth Year - Eighth Semester - Compulsory Courses:
TTE435, Airport Engineering, C, T:4, P:0, C:4, E:6
TTE436, Bridge Engineering, C, T:4, P:0, C:4, E:6
TTE471, Risk Management, C, T:3, P:0, C:3, E:6
TTE498, Graduation Project, C, T:4, P:0, C:4, E:6

Elective Course:
TE, Technical Elective, E, T:3, P:0, C:3, E:6

Total: T:18, P:0, C:18, ECTS:30""",

        # Technical Elective Courses
        """Technical Elective Courses (Sample):

Transportation Planning Electives:
TTE441, Urban Transportation Planning
TTE442, Transportation Modeling and Simulation
TTE443, Intelligent Transportation Systems
TTE444, Transportation Safety and Accident Analysis

Infrastructure Electives:
TTE445, Pavement Management Systems
TTE446, Transportation Geotechnics
TTE447, Bridge Design and Maintenance
TTE448, Tunnel Engineering

Environmental and Sustainability Electives:
TTE449, Sustainable Transportation Systems
TTE450, Transportation and Environment
TTE451, Public Transport Planning
TTE452, Transportation Economics

Management and Technology Electives:
TTE453, Logistics and Supply Chain Management
TTE454, Port and Harbor Engineering
TTE455, Transportation Policy and Legislation
TTE456, Advanced Traffic Engineering""",

        # Program Summary and Career Opportunities
        """Traffic and Transportation Engineering Program Summary:
Degree: Bachelor of Science in Traffic and Transportation Engineering
Duration: 4 years (8 semesters)
Total Credits: 158
Total ECTS: 240
Percentage of Electives: 8%

Program Focus Areas:
- Transportation Systems Planning and Design
- Traffic Engineering and Management
- Highway and Pavement Engineering
- Public Transportation Systems
- Transportation Infrastructure
- Geographic Information Systems (GIS)
- Project Management in Transportation

Core Competencies Developed:
- Transportation system analysis and design
- Traffic flow theory and control
- Highway and pavement design
- Public transportation planning
- GIS applications in transportation
- Project management and risk assessment
- Infrastructure planning and maintenance

Career Opportunities:
Traffic Engineer
Transportation Planner
Highway Design Engineer
Public Transportation Specialist
Transportation Modeler
GIS Specialist in Transportation
Transportation Project Manager
Infrastructure Engineer
Urban Mobility Planner
Transportation Consultant
Logistics and Supply Chain Manager

Industry Sectors:
Government Transportation Departments
Municipalities and City Planning
Transportation Consulting Firms
Construction and Infrastructure Companies
Public Transportation Authorities
Logistics and Supply Chain Companies
Research and Development Institutions
Academic and Teaching Positions""",

        # Course Progression and Specializations
        """Course Progression and Specialization Tracks:

Foundation Year (1st Year):
- Basic sciences and mathematics
- Engineering fundamentals
- Computer programming and technical drawing
- Language and cultural courses

Core Engineering (2nd Year):
- Advanced mathematics and statistics
- Engineering mechanics and materials
- Surveying and construction materials
- Engineering economy

Transportation Specialization (3rd Year):
- Transportation engineering fundamentals
- Soil mechanics and structural analysis
- Traffic engineering and highway design
- Transportation systems and pavement materials

Professional Practice (4th Year):
- Advanced transportation systems
- Project management and GIS
- Infrastructure engineering (bridges, airports)
- Graduation project and technical electives

Specialization Tracks:
1. Traffic Engineering and Management: Traffic flow, control systems, intelligent transportation
2. Transportation Planning: Urban planning, modeling, public transportation
3. Infrastructure Engineering: Highways, pavements, bridges, airports
4. Transportation Systems: Logistics, supply chain, multimodal transport

Practical Components:
- Two summer internships (30 days each)
- Computer applications and GIS laboratories
- Graduation project
- Technical elective specialization"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Civil and Environmental Engineering",
            "department": "Traffic and Transportation Engineering",
            "degree": "Bachelor",
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
            "course_type": "elective",
            "document_type": "course_list",
            "content_type": "technical_electives"
        },
        {
            "document_type": "program_info",
            "content_type": "program_summary_careers"
        },
        {
            "document_type": "program_info",
            "content_type": "specialization_tracks"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"tte_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Traffic and Transportation Engineering curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["traffic engineering highway design transportation"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_traffic_transportation_curriculum_to_chromadb()