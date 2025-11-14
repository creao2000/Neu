import chromadb
from chromadb.utils import embedding_functions

def add_automotive_engineering_curriculum_to_chromadb():
    """Add Automotive Engineering curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_automotive_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_automotive_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_automotive_engineering")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF ENGINEERING
DEPARTMENT OF AUTOMOTIVE ENGINEERING
Bachelor of Science in Automotive Engineering

Program Duration: 4 years (8 semesters)
Degree: Bachelor of Science
Total ECTS for Graduation: 240
Total Credits: 150

Main website: https://muhendislik.neu.edu.tr/?lang=en
Curriculum link: https://muhendislik.neu.edu.tr/academic/academic-programmes/department-of-automotive-engineering/?lang=en

Legend:
PS = Problem Solving
C = Complementary
R = Reformative
T = Tutorial
LAB = Laboratory Hours
Practical = Practical Hours""",

        # 1st Year - 1st Semester
        """First Year - First Semester (Fall) - Compulsory Courses:
CHM101, General Chemistry, Credit:4, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:0, C:2, R:2, T:1
ENG101, English I, Credit:3, ECTS:3, Prerequisite: None, Class:0, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
MTH101, Mathematics I, Credit:4, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ECC103, Engineering Drawing I, Credit:3, ECTS:3, Prerequisite: None, Class:2, LAB:0, Practical:2, PS:0, C:1, R:1, T:2
PHY101, General Physics I, Credit:4, ECTS:6, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:0
AUE100, Orientation, Credit:0, ECTS:1, Prerequisite: None, Class:2, LAB:0, Practical:0, PS:0, C:1, R:1, T:0
TUR101/YIT101, Turkish Language I for Turkish Students/Turkish I for Foreign Students, Credit:2, ECTS:2, Prerequisite: None, Class:2, LAB:0, Practical:0, PS:0, C:2, R:0, T:1

Total Semester: Credit:20, ECTS:26""",

        # 1st Year - 2nd Semester
        """First Year - Second Semester (Spring) - Compulsory Courses:
ECC101, Introduction to Computers and Programming, Credit:3, ECTS:7, Prerequisite: None, Class:4, LAB:1, Practical:0, PS:3, C:1, R:1, T:0
ENG102, English II, Credit:3, ECTS:3, Prerequisite: ENG101, Class:0, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
MTH102, Mathematics II, Credit:4, ECTS:6, Prerequisite: MTH101, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ECC013, Engineering Drawing II, Credit:3, ECTS:6, Prerequisite: ECC103, Class:2, LAB:0, Practical:2, PS:0, C:1, R:1, T:2
TUR102/YIT102, Turkish Language II for Turkish Students/Turkish II for Foreign Students, Credit:2, ECTS:2, Prerequisite: TUR101/YIT101, Class:2, LAB:0, Practical:0, PS:0, C:2, R:0, T:1
PHY102, General Physics II, Credit:4, ECTS:6, Prerequisite: PHY101, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:0

Total Semester: Credit:19, ECTS:30""",

        # 2nd Year - 1st Semester
        """Second Year - First Semester (Fall) - Compulsory Courses:
MTH201, Ordinary Differential Equations, Credit:4, ECTS:6, Prerequisite: MTH102, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ECC211, Engineering Materials, Credit:3, ECTS:5, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:1, C:2, R:1, T:0
ECC206, Statics, Credit:3, ECTS:5, Prerequisite: PHY101, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ECC207, Thermodynamics I, Credit:3, ECTS:5, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
AIT101/AIT103, Ataturk's Principles and Reforms for Students I, Credit:2, ECTS:2, Prerequisite: None, Class:2, LAB:0, Practical:0, PS:0, C:2, R:0, T:1
ENG201, English III, Credit:3, ECTS:3, Prerequisite: ENG102, Class:3, LAB:0, Practical:0, PS:0, C:1, R:1, T:1

Total Semester: Credit:18, ECTS:26""",

        # 2nd Year - 2nd Semester
        """Second Year - Second Semester (Spring) - Compulsory Courses:
AUE205, Basic Electricity & Electronics, Credit:3, ECTS:5, Prerequisite: PHY102, Class:3, LAB:0, Practical:0, PS:2, C:1, R:0, T:0
MTH214, Mathematics for Engineers, Credit:3, ECTS:5, Prerequisite: MTH101, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ECC209, Manufacturing Technology I, Credit:3, ECTS:4, Prerequisite: None, Class:4, LAB:0, Practical:2, PS:2, C:2, R:0, T:2
ECC212, Dynamics, Credit:3, ECTS:4, Prerequisite: PHY101, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ECC208, Thermodynamics II, Credit:3, ECTS:5, Prerequisite: ECC207, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ECC213, Strength of Materials I, Credit:3, ECTS:4, Prerequisite: ECC206, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
AIT102/AIT104, Ataturk's Principles and Reforms for Students II, Credit:2, ECTS:2, Prerequisite: AIT101/AIT103, Class:2, LAB:0, Practical:0, PS:0, C:2, R:0, T:1
AUE200, Workshop Training (2 Weeks), Credit:0, ECTS:1, Prerequisite: None, Class:0, LAB:0, Practical:0, PS:0, C:0, R:0, T:0

Total Semester: Credit:20, ECTS:30""",

        # 3rd Year - 1st Semester
        """Third Year - First Semester (Fall) - Compulsory Courses:
ECC304, Fluid Mechanics I, Credit:4, ECTS:7, Prerequisite: ECC212, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ECC307, Machine Design I, Credit:4, ECTS:6, Prerequisite: ECC213, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
AUE305, Introduction to Automotive Engineering, Credit:3, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ECC305, Manufacturing Technology II, Credit:3, ECTS:5, Prerequisite: ECC209, Class:4, LAB:0, Practical:2, PS:3, C:2, R:1, T:0
ECC306, Heat Transfer I, Credit:3, ECTS:6, Prerequisite: ECC207, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0

Total Semester: Credit:17, ECTS:30""",

        # 3rd Year - 2nd Semester
        """Third Year - Second Semester (Spring) - Compulsory Courses:
MTH323, Numerical Analysis, Credit:3, ECTS:6, Prerequisite: MTH102, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ECC309, Theory of Machines I, Credit:3, ECTS:5, Prerequisite: ECC212, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ECC308, Machine Design II, Credit:4, ECTS:5, Prerequisite: ECC207, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ECC310, Control Systems, Credit:3, ECTS:5, Prerequisite: MTH201, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
AUE306, Vehicle Component Design, Credit:3, ECTS:6, Prerequisite: ECC307, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
AUE300, Industrial Training (6 Weeks), Credit:0, ECTS:3, Prerequisite: None, Class:0, LAB:0, Practical:0, PS:0, C:0, R:0, T:0

Total Semester: Credit:16, ECTS:30""",

        # 4th Year - 1st Semester
        """Fourth Year - First Semester (Fall) - Compulsory Courses:
AUE401, Vehicle Dynamics, Credit:3, ECTS:4, Prerequisite: ECC212, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
AUE403, Vehicle Body Design, Credit:3, ECTS:4, Prerequisite: AUE306, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ECC424, Experimental Analysis of Mechanical Engineering Systems, Credit:3, ECTS:5, Prerequisite: None, Class:2, LAB:2, Practical:0, PS:1, C:2, R:1, T:0
ECC425, Internal Combustion Engines, Credit:3, ECTS:5, Prerequisite: ECC208, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ECC439, Occupational Health and Safety I, Credit:2, ECTS:4, Prerequisite: None
TE, Technical Elective, Credit:3, ECTS:4, Prerequisite: None
TE, Technical Elective, Credit:3, ECTS:4, Prerequisite: None

Total Semester: Credit:20, ECTS:30""",

        # 4th Year - 2nd Semester
        """Fourth Year - Second Semester (Spring) - Compulsory Courses:
AUE400, Graduation Project, Credit:3, ECTS:6, Prerequisite: None
AUE404, Vehicle Production & Systems, Credit:3, ECTS:4, Prerequisite: ECC209, ECC305
ECC440, Occupational Health and Safety II, Credit:2, ECTS:4, Prerequisite: ECC439
TE, Technical Elective, Credit:3, ECTS:4, Prerequisite: None
TE, Technical Elective, Credit:3, ECTS:4, Prerequisite: None
RNTE, Restricted Non-Technical Elective, Credit:3, ECTS:5, Prerequisite: None
FNTE, Free Non-Technical Elective, Credit:3, ECTS:3, Prerequisite: None

Total Semester: Credit:20, ECTS:30

Program Total: Credit:150, ECTS:240""",

        # Technical Elective Courses
        """Technical Elective Courses (TE) - Automotive Engineering Specializations:
ME403, Theory of Machines 2, Credit:3, ECTS:6, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ME443, Computational Fluid Dynamics, Credit:3, ECTS:6, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ME451, Advanced Strength of Materials, Credit:3, ECTS:6, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
EE435, Mechatronics, Credit:3, ECTS:5, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ME418, Refrigeration Techniques, Credit:3, ECTS:6, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
AUE411, Transmission Systems, Credit:3, ECTS:5, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ME423, Heat Exchanger Design, Credit:3, ECTS:6, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
AUE421, Fuel Cells, Credit:3, ECTS:5, Class:3, LAB:0, Practical:0, PS:0, C:2, R:2, T:0
ME426, Introduction to Finite Element Method, Credit:3, ECTS:6, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ME429, Computer Aided Design (CAD), Credit:3, ECTS:6, Class:3, LAB:0, Practical:0, PS:0, C:2, R:2, T:0
AUE422, Internal Combustion Engine Design, Credit:3, ECTS:5, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
AUE431, Electronic Systems in Vehicles, Credit:3, ECTS:5, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
AUE432, Automotive Sensors and Measurement Systems, Credit:3, ECTS:5, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
AUE452, Electric and Hybrid Vehicle, Credit:3, ECTS:5, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ME453, Materials Engineering, Credit:3, ECTS:6, Class:3, LAB:0, Practical:0, PS:1, C:2, R:0, T:0
ME454, Heat Treatment, Credit:3, ECTS:6, Class:3, LAB:0, Practical:0, PS:0, C:1, R:2, T:0
ME472, Quality Control, Credit:3, ECTS:6, Class:3, LAB:0, Practical:0, PS:0, C:2, R:2, T:0
ECC404, Artificial Neural Network, Credit:3, ECTS:6, Class:3, LAB:0, Practical:0, PS:0, C:2, R:2, T:0
ECC419, Digital Image Processing, Credit:3, ECTS:6, Class:3, LAB:0, Practical:0, PS:0, C:2, R:2, T:0
AUE441, Intelligent Vehicle Technology, Credit:3, ECTS:6, Class:3, LAB:0, Practical:0, PS:0, C:2, R:2, T:0
AUE442, Electronic Instrumentation, Credit:3, ECTS:6, Class:3, LAB:0, Practical:0, PS:0, C:2, R:2, T:0""",

        # Restricted Non-Technical Elective Courses
        """Restricted Non-Technical Elective Courses (RNTE):
ECC426, Economics for Engineers, Credit:3, ECTS:5, Class:3, LAB:0, Practical:0, PS:0, C:2, R:2, T:0
ECC427, Management for Engineers, Credit:3, ECTS:5, Class:3, LAB:0, Practical:0, PS:0, C:2, R:2, T:0""",

        # Mission and Vision
        """Department Mission and Vision:

Mission:
To support and lead the nation's requirements and technological developments, to be able to conduct international projects and to have an authority in research areas. To perform research studies and to educate engineers equipped with technical "know-how", creative thinking and being able to try and research new technologies to achieve required goal.

Vision:
The vision of the department is to have respect and authority in engineering activities and to gain acceptance through research projects, support to the nation and delivering high quality engineers.""",

        # Program Summary and Career Opportunities
        """Automotive Engineering Program Summary:
Degree: Bachelor of Science in Automotive Engineering
Duration: 4 years (8 semesters)
Total Credits: 150
Total ECTS: 240

Program Focus Areas:
- Vehicle Dynamics and Control
- Automotive Design and Manufacturing
- Internal Combustion Engines
- Automotive Electronics and Mechatronics
- Vehicle Body Design
- Transmission Systems
- Electric and Hybrid Vehicles
- Automotive Materials and Manufacturing
- Computational Fluid Dynamics
- Automotive Sensors and Instrumentation

Career Opportunities:
Automotive Design Engineer
Vehicle Dynamics Engineer
Powertrain Engineer
Automotive Electronics Engineer
Manufacturing Engineer
Quality Control Engineer
Research and Development Engineer
Automotive Consultant
Project Engineer
Production Engineer
Testing and Validation Engineer
Academic and Research Positions

Professional Recognition:
Graduates are qualified to work in automotive manufacturers, suppliers, research institutions, and engineering consulting firms worldwide."""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Engineering",
            "department": "Automotive Engineering",
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
            "elective_type": "technical",
            "document_type": "course_list",
            "content_type": "technical_electives"
        },
        {
            "course_type": "elective",
            "elective_type": "non_technical",
            "document_type": "course_list",
            "content_type": "restricted_non_technical_electives"
        },
        {
            "document_type": "program_info",
            "content_type": "mission_vision"
        },
        {
            "document_type": "program_info",
            "content_type": "program_summary_careers"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"automotive_eng_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Automotive Engineering curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["vehicle dynamics automotive design"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_automotive_engineering_curriculum_to_chromadb()