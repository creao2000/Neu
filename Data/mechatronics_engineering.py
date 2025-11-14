
# import chromadb

# # Initialize ChromaDB client
# chroma_client = chromadb.PersistentClient(path="./chroma_db")

# # List all collections first to confirm
# collections = chroma_client.list_collections()
# print("Current collections:", [col.name for col in collections])

# # Delete the specific collection
# try:
#     chroma_client.delete_collection(name="neu_mechatronics_engineering")
#     print("✅ Collection 'neu_mechatronics_engineering' deleted successfully!")
# except Exception as e:
#     print(f"❌ Error deleting collection: {e}")

# # Verify it's gone
# collections = chroma_client.list_collections()
# print("Remaining collections:", [col.name for col in collections])












import chromadb
from chromadb.utils import embedding_functions

def add_mechatronics_engineering_curriculum_to_chromadb():
    """Add Mechatronics Engineering curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_mechatronics_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_mechatronics_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_mechatronics_engineering")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF ENGINEERING
DEPARTMENT OF MECHATRONICS ENGINEERING
Bachelor of Science in Mechatronics Engineering

Program Duration: 4 years (8 semesters)
Degree: Bachelor of Science
Total ECTS for Graduation: 220
Total Credits: 145

Main website: https://muhendislik.neu.edu.tr/?lang=en
Curriculum link: https://muhendislik.neu.edu.tr/academic/academic-programmes/department-of-mechatronics-engineering/?lang=en

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
ECC101, Introduction to Computer Programming, Credit:3, ECTS:5, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:0, C:0, R:0, T:4
ENG101, English I, Credit:3, ECTS:5, Prerequisite: None, Class:0, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
MTH101, Calculus I, Credit:4, ECTS:5, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
AIT101, Atatürk İlkeleri ve İnkilap Tarihi I, Credit:2, ECTS:2, Prerequisite: None, Class:0, LAB:0, Practical:0, PS:2, C:0, R:0, T:2
TUR101, Türk Dili I, Credit:2, ECTS:5, Prerequisite: None, Class:4, LAB:1, Practical:0, PS:3, C:1, R:1, T:0
YIT101, Turkish for Foreign Students I, Credit:2, ECTS:2, Prerequisite: None, Class:2, LAB:0, Practical:0, PS:0, C:2, R:0, T:1
AIT103, Ataturk's Principles & Turkish Reform I, Credit:2, ECTS:2, Prerequisite: None, Class:2, LAB:0, Practical:0, PS:0, C:2, R:0, T:1

Total Semester: Credit:22, ECTS:31""",

        # 1st Year - 2nd Semester
        """First Year - Second Semester (Spring) - Compulsory Courses:
ENG102, English II, Credit:3, ECTS:3, Prerequisite: ENG101, Class:0, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
MTH102, Calculus II, Credit:4, ECTS:5, Prerequisite: MTH101, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
MTH113, Linear Algebra, Credit:3, ECTS:5, Prerequisite: MTH101, Class:4, LAB:0, Practical:0, PS:2, C:2, R:0, T:0
PHY102, General Physics II, Credit:4, ECTS:5, Prerequisite: PHY101, Class:3, LAB:2, Practical:0, PS:2, C:2, R:1, T:0
MCT102, Mechanical Workshop Practice, Credit:3, ECTS:3, Prerequisite: None, Class:1, LAB:0, Practical:0, PS:0, C:1, R:0, T:2
MCT100, Introduction to Mechatronics Engineering, Credit:1, ECTS:3, Prerequisite: None, Class:1, LAB:0, Practical:0, PS:0, C:1, R:0, T:2

Total Semester: Credit:18, ECTS:24""",

        # 2nd Year - 1st Semester
        """Second Year - First Semester (Fall) - Compulsory Courses:
ECC216, Electrical Circuit Theory, Credit:4, ECTS:5, Prerequisite: PHY102, MTH101, Class:4, LAB:2, Practical:0, PS:2, C:1, R:1, T:0
ECC211, Engineering Materials, Credit:3, ECTS:5, Prerequisite: CHM101, Class:3, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
ECC206, Statics, Credit:4, ECTS:6, Prerequisite: PHY101, Class:3, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
MTH201, Differential Equations, Credit:4, ECTS:5, Prerequisite: MTH102, Class:4, LAB:0, Practical:0, PS:2, C:2, R:0, T:0
ECC207, Thermodynamics, Credit:4, ECTS:6, Prerequisite: CHM101, Class:3, LAB:0, Practical:0, PS:0, C:2, R:0, T:1
ECC103, Engineering Drawing I, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:0, C:1, R:1, T:1

Total Semester: Credit:22, ECTS:32""",

        # 2nd Year - 2nd Semester
        """Second Year - Second Semester (Spring) - Compulsory Courses:
ECC224, Strength of Materials I, Credit:4, ECTS:5, Prerequisite: ECC206, Class:4, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
ECC212, Dynamics, Credit:3, ECTS:5, Prerequisite: PHY101, Class:3, LAB:0, Practical:0, PS:0, C:0, R:0, T:0
ECC222, Manufacturing Technology, Credit:3, ECTS:4, Prerequisite: None, Class:3, LAB:0, Practical:2, PS:1, C:1, R:1, T:0
ECC218, Electronics I, Credit:4, ECTS:6, Prerequisite: ECC216, ECC211, Class:4, LAB:2, Practical:0, PS:2, C:1, R:1, T:0
ECC013, Engineering Drawing II, Credit:4, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:0, C:1, R:1, T:1
MCT200, Summer Training I, Credit:0, ECTS:1, Prerequisite: None, Class:2, LAB:0, Practical:0, PS:0, C:2, R:0, T:1

Total Semester: Credit:18, ECTS:26""",

        # 3rd Year - 1st Semester
        """Third Year - First Semester (Fall) - Compulsory Courses:
ECC001, Logic Circuit Design, Credit:4, ECTS:6, Prerequisite: ECC218, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:2
MCT301, Mechanical Components & Instrumentation, Credit:3, ECTS:5, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ECC008, Signals and Systems, Credit:4, ECTS:6, Prerequisite: ECC216, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:2
MCT310, Computer Applications for Mechatronics Engineering, Credit:3, ECTS:5, Prerequisite: ECC101, Class:4, LAB:0, Practical:0, PS:1, C:0, R:1, T:1
ENG201, English Communication Skills, Credit:3, ECTS:3, Prerequisite: ENG102, Class:0, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
NTE, Non-Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3
CAR100, Career Planning, Credit:0, ECTS:0, Prerequisite: None, Class:0

Total Semester: Credit:20, ECTS:30""",

        # 3rd Year - 2nd Semester
        """Third Year - Second Semester (Spring) - Compulsory Courses:
ECC301, Microprocessors, Credit:4, ECTS:6, Prerequisite: ECC001, Class:4, LAB:2, Practical:0, PS:2, C:1, R:1, T:2
ECC310, Control Systems, Credit:3, ECTS:5, Prerequisite: MTH201, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:2
MCT311, Machine Elements, Credit:4, ECTS:5, Prerequisite: ECC224, Class:4, LAB:0, Practical:0, PS:1, C:0, R:1, T:1
MTH251, Probability and Random Variables, Credit:3, ECTS:5, Prerequisite: MTH102, Class:4, LAB:0, Practical:0, PS:2, C:2, R:0, T:0
RE, Restricted Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3
MCT300, Summer Training II, Credit:0, ECTS:1, Prerequisite: MCT200, Class:2, LAB:0, Practical:0, PS:0, C:2, R:0, T:1

Total Semester: Credit:17, ECTS:27""",

        # 4th Year - 1st Semester
        """Fourth Year - First Semester (Fall) - Compulsory Courses:
MCT435, Mechatronics, Credit:3, ECTS:0, Prerequisite: None, Class:2, LAB:3, Practical:0, PS:0, C:1, R:1, T:2
ECC429, Engineering Ethics, Credit:3, ECTS:5, Prerequisite: None, Class:4, LAB:2, Practical:0, PS:0, C:1, R:1, T:1
TE, Technical Elective, Credit:3, ECTS:4, Prerequisite: None
TE, Technical Elective, Credit:3, ECTS:4, Prerequisite: None
TE, Technical Elective, Credit:3, ECTS:4, Prerequisite: None
MCT410, Introduction to Capstone Design, Credit:4, ECTS:0, Prerequisite: None, Class:2, LAB:3, Practical:0, PS:0, C:1, R:1, T:2

Total Semester: Credit:19, ECTS:17""",

        # 4th Year - 2nd Semester
        """Fourth Year - Second Semester (Spring) - Compulsory Courses:
MCT411, Capstone Team Project, Credit:4, ECTS:12, Prerequisite: MCT410, Class:3, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
ECC437, Robotic Systems, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:2
TE, Technical Elective, Credit:3, ECTS:4, Prerequisite: None
TE, Technical Elective, Credit:3, ECTS:4, Prerequisite: None
AIT104, Turkish for Foreign Students II, Credit:2, ECTS:2, Prerequisite: AIT103, Class:2, LAB:0, Practical:0, PS:0, C:2, R:0, T:1
YIT102, Ataturk's Principles & Turkish Reform II, Credit:2, ECTS:2, Prerequisite: YIT101, Class:2, LAB:0, Practical:0, PS:0, C:2, R:0, T:1
AIT102, Atatürk İlkeleri ve İnkilap Tarihi II, Credit:2, ECTS:2, Prerequisite: AIT101, Class:0, LAB:0, Practical:0, PS:2, C:0, R:0, T:2
TUR102, Türk Dili II, Credit:2, ECTS:5, Prerequisite: TUR101, Class:4, LAB:1, Practical:0, PS:3, C:1, R:1, T:0

Total Semester: Credit:21, ECTS:36

Program Total: Credit:145, ECTS:220""",

        # Technical Elective Courses
        """Technical Elective Courses (TE) - Mechatronics Specializations:
EE424, Process Control Instrumentation Technology, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:2
EE451, Digital Electronics, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
EE454, Digital Control Systems, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
EE470, Programmable Logic Controllers, Credit:3, ECTS:5, Prerequisite: ECC001, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:2
EE433, Power Electronics, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:0
EE471, Power System Analysis I, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:2
EE472, Power System Analysis II, Credit:3, ECTS:5, Prerequisite: EE471, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:2
EE474, Static Power Conversion, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:2
EE474, High Voltage Techniques I, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:2, C:1, R:2, T:1
ME453, Material Engineering, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:1
ME454, Heat Treatment, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:1
EE432, Mechatronics, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:1
EE463, Image Processing, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
BME448, Micro and Nano Technologies in Biomedical Engineering, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:1""",

        # Restricted Non-Technical Elective Courses
        """Restricted Non-Technical Elective Courses (NTE/RE):
MAN101, Introduction to Management, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:2, R:2, T:0
ECON101, Introduction to Economics, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:2, R:2, T:0
FRE101, French I, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:1, C:1, R:1, T:0
FRE102, French II, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
GER101, German I, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:1, C:1, R:1, T:0
GER102, German II, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:1, C:1, R:2, T:1
PHIL101, Introduction to Philosophy, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:1
HIST103, History of Civilization, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:1
POL101, Political Science I, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:1
SOC101, Sociology, Credit:3, ECTS:5, Prerequisite: None, Class:0, LAB:0, Practical:0, PS:1, C:1, R:1, T:1""",

        # Program Summary and Career Opportunities
        """Mechatronics Engineering Program Summary:
Degree: Bachelor of Science in Mechatronics Engineering
Duration: 4 years (8 semesters)
Total Credits: 145
Total ECTS: 220

Program Focus Areas:
- Mechanical Systems and Machine Design
- Electronics and Circuit Design
- Control Systems and Automation
- Robotics and Intelligent Systems
- Microprocessors and Embedded Systems
- Signal Processing and Instrumentation
- Power Electronics and Systems
- Manufacturing Technology
- Computer Applications in Engineering

Career Opportunities:
Mechatronics Engineer
Robotics Engineer
Automation Engineer
Control Systems Engineer
Embedded Systems Engineer
Instrumentation Engineer
Manufacturing Engineer
Research and Development Engineer
Project Engineer
Maintenance Engineer
Quality Control Engineer
Academic and Research Positions

Professional Recognition:
Graduates are qualified to work in automation, robotics, manufacturing, automotive, aerospace, and various high-tech industries worldwide."""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Engineering",
            "department": "Mechatronics Engineering",
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
            "content_type": "non_technical_electives"
        },
        {
            "document_type": "program_info",
            "content_type": "program_summary_careers"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"mechatronics_eng_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Mechatronics Engineering curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["mechatronics robotics control systems"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_mechatronics_engineering_curriculum_to_chromadb()