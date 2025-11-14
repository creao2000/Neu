import chromadb
from chromadb.utils import embedding_functions

def add_industrial_engineering_curriculum_to_chromadb():
    """Add Industrial Engineering curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_industrial_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_industrial_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_industrial_engineering")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF ENGINEERING
DEPARTMENT OF INDUSTRIAL ENGINEERING
Bachelor of Science in Industrial Engineering

Program Duration: 4 years (8 semesters)
Degree: Bachelor of Science
Total ECTS for Graduation: 240
Total Credits: 143

Main website: https://muhendislik.neu.edu.tr/?lang=en
Curriculum link: https://muhendislik.neu.edu.tr/academic/academic-programmes/department-of-industrial-engineering/?lang=en

Legend:
PS = Problem Solving
C = Complementary
R = Reformative
T = Tutorial
LAB = Laboratory Hours
Practical = Practical Hours""",

        # 1st Year - 1st Semester
        """First Year - First Semester (Fall) - Compulsory Courses:
PHY101, General Physics I, Credit:4, ECTS:6, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:1
CHM101, General Chemistry I, Credit:4, ECTS:6, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:0, C:2, R:2, T:1
MTH101, Mathematics I, Credit:4, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ENG101, English I, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
IND101, Fundamentals of Industrial Engineering, Credit:3, ECTS:5, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:0, C:1, R:0, T:2
YIT101, Turkish for Foreign Students I, Credit:2, ECTS:2, Prerequisite: None, Class:2, LAB:0, Practical:0, PS:0, C:2, R:0, T:1
TUR101, Turkish Language I, Credit:2, ECTS:2, Prerequisite: None, Class:2, LAB:0, Practical:0, PS:2, C:0, R:0, T:2

Total Semester: Credit:20, ECTS:30""",

        # 1st Year - 2nd Semester
        """First Year - Second Semester (Spring) - Compulsory Courses:
PHY102, General Physics II, Credit:4, ECTS:6, Prerequisite: PHY101, Class:3, LAB:2, Practical:0, PS:2, C:2, R:1, T:0
MTH102, Mathematics II, Credit:4, ECTS:6, Prerequisite: MTH101, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
TD102, Technical Drawing, Credit:3, ECTS:5, Prerequisite: None, Class:2, LAB:2, Practical:0
ENG102, English II, Credit:3, ECTS:5, Prerequisite: ENG101, Class:3, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
YIT102, Turkish for Foreign Students II, Credit:2, ECTS:2, Prerequisite: YIT101, Class:2, LAB:0, Practical:0, PS:0, C:2, R:0, T:1
TUR102, Turkish Language II, Credit:2, ECTS:2, Prerequisite: TUR101, Class:0, LAB:0, Practical:0, PS:2, C:0, R:0, T:2
IND102, Information Technologies for Industrial Engineering, Credit:3, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:0, C:2, R:2, T:1

Total Semester: Credit:19, ECTS:30""",

        # 2nd Year - 1st Semester
        """Second Year - First Semester (Fall) - Compulsory Courses:
AIT101, Atatürk Principles and the History of Turkish Revolution I, Credit:2, ECTS:2, Prerequisite: None, Class:2, LAB:0, Practical:0, PS:0, C:2, R:0, T:1
AIT103, Principles of Atatürk and the History of Turkish Revolution I, Credit:2, ECTS:2, Prerequisite: None, Class:2, LAB:0, Practical:0, PS:0, C:2, R:0, T:1
ECC101, Introduction to Computers and Programming, Credit:3, ECTS:5, Prerequisite: None, Class:2, LAB:2, Practical:0, PS:3, C:1, R:1, T:0
IND201, Elements of Linear Algebra, Credit:3, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:0, C:1, R:1, T:2
IND203, Statistics I, Credit:3, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:0, C:2, R:2, T:1
IND205, Production & Operations Management I, Credit:3, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:0, C:2, R:2, T:1
NTE, Non-Technical Electives, Credit:3, ECTS:5, Prerequisite: None, Class:3

Total Semester: Credit:17, ECTS:30""",

        # 2nd Year - 2nd Semester
        """Second Year - Second Semester (Spring) - Compulsory Courses:
AIT102, Principles of Atatürk and Recent Turkish History II, Credit:2, ECTS:2, Prerequisite: AIT101, Class:2, LAB:0, Practical:0, PS:0, C:2, R:0, T:1
AIT104, Principles of Atatürk and the History of Turkish Revolution II, Credit:2, ECTS:2, Prerequisite: AIT103, Class:2, LAB:0, Practical:0, PS:0, C:2, R:0, T:1
ECC108, Object Oriented Programming, Credit:3, ECTS:5, Prerequisite: None, Class:2, LAB:2, Practical:0, PS:0, C:2, R:0, T:1
IND202, Graphing & Optimization Principles, Credit:3, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:0, C:2, R:0, T:1
IND204, Statistics II, Credit:3, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:0, C:1, R:1, T:2
IND206, Production & Operations Management II, Credit:3, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practical:2, PS:2, C:2, R:0, T:2
IND208, Factory Internship, Credit:0, ECTS:1, Prerequisite: None, Class:0, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
NTE, Non-Technical Elective, Credit:3, ECTS:4, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:1, R:1, T:2

Total Semester: Credit:17, ECTS:30""",

        # 3rd Year - 1st Semester
        """Third Year - First Semester (Fall) - Compulsory Courses:
IND301, Analysis of Service Systems, Credit:4, ECTS:7, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
IND303, Operational Research I, Credit:4, ECTS:7, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:3, C:2, R:1, T:0
IND31X, Technical Elective, Credit:3, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
IND31X, Technical Elective, Credit:3, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:0, C:3, R:1, T:0
NTE, Non-Technical Elective, Credit:3, ECTS:4, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:3, R:1, T:0

Total Semester: Credit:17, ECTS:30""",

        # 3rd Year - 2nd Semester
        """Third Year - Second Semester (Spring) - Compulsory Courses:
IND302, Entrepreneurship & Innovation, Credit:4, ECTS:5, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:1, C:0, R:1, T:1
IND304, Operational Research II, Credit:4, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:0, C:1, R:1, T:2
IND31X, Technical Elective, Credit:3, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:0, C:1, R:1, T:2
IND31X, Technical Elective, Credit:3, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:1, C:1, R:1, T:2
NTE, Nontechnical Elective, Credit:3, ECTS:6, Prerequisite: None, Class:3
IND306, Service Internship, Credit:0, ECTS:1, Prerequisite: None, Class:0, LAB:0, Practical:0, PS:0, C:0, R:0, T:0

Total Semester: Credit:17, ECTS:30""",

        # 4th Year - 1st Semester
        """Fourth Year - First Semester (Fall) - Compulsory Courses:
IND401, Transforming Ideas to Projects, Credit:4, ECTS:7, Prerequisite: None, Class:2, LAB:3, Practical:0, PS:0, C:1, R:1, T:2
IND403, Auditing Productivity, Credit:4, ECTS:7, Prerequisite: None, Class:3, LAB:1, Practical:0, PS:0, C:1, R:1, T:2
IND41X, Technical Elective, Credit:3, ECTS:6
IND41X, Technical Elective, Credit:3, ECTS:6
NTE, Non-Technical Elective, Credit:3, ECTS:4, Prerequisite: None

Total Semester: Credit:17, ECTS:30""",

        # 4th Year - 2nd Semester
        """Fourth Year - Second Semester (Spring) - Compulsory Courses:
IND402, Strategy of Quality, Credit:4, ECTS:4, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
IND404, Designing the Factory, Credit:4, ECTS:4, Prerequisite: None, Class:4, LAB:0
IND41X, Technical Elective, Credit:3, ECTS:4, Prerequisite: None, Class:4, LAB:0
IND41X, Technical Elective, Credit:3, ECTS:4, Prerequisite: None, Class:4, LAB:0
NTE, Non-Technical Elective, Credit:3, ECTS:4, Prerequisite: None, Class:3
IND400, Graduation Project, Credit:3, ECTS:10, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:1, R:1, T:1

Total Semester: Credit:19, ECTS:30

Program Total: Credit:143, ECTS:240""",

        # Technical Elective Courses 31X
        """Technical Elective Courses (IND 31X) - 3rd Year:
IND311, Safety & Occupational Management, Credit:3, ECTS:4, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
IND312, Lean Thinking, Credit:3, ECTS:4, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:1
IND313, Implementing Industry 4.0, Credit:3, ECTS:4, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:1, C:1, R:1, T:0
IND314, Decision Theory, Credit:3, ECTS:4, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
IND315, Forecasting, Credit:3, ECTS:4, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:1, C:1, R:1, T:0
IND316, Supply Chain & Logistics, Credit:3, ECTS:4, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:1, C:1, R:1, T:0
MTH323, Numerical Analysis, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:1, C:1, R:1, T:0
BME340, Modeling of Biological Systems, Credit:3, ECTS:5
ECC311, Management of Information Systems, Credit:3, ECTS:5""",

        # Technical Elective Courses 41X
        """Technical Elective Courses (IND 41X) - 4th Year:
IND411, Six Sigma, Credit:3, ECTS:4, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
IND412, Digitalization & Industry 4.0, Credit:3, ECTS:4, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:1, C:1, R:1, T:0
IND413, Economic Principles in Industrial Engineering, Credit:3, ECTS:4, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:1, C:1, R:2, T:1
IND414, Scheduling, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:1
IND415, Fuzzy Systems, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:1
IND416, Advanced Operations Management, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:1
IND417, Location Techniques & Problems, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
IND434, Quality Engineering, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:2, R:2, T:0
EE432, Mechatronics, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:1
EE463, Image Processing, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
BME448, Micro and Nano Technologies in Biomedical Engineering, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:1
ISE412, Health Information Management, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
ISE413, Strategic Information Systems Management, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:1, C:1, R:1, T:0
PGE436, Simulating of Geosystems, Credit:3, ECTS:5, Prerequisite: None, Class:2, LAB:1, Practical:0, PS:0, C:1, R:1, T:1
ME426, Introduction to Finite Elements, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ME429, Computer Aided Design (CAD), Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:2, R:2, T:0
ECC404, Artificial Neural Network, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:2, R:2, T:0""",

        # Non-Technical Elective Courses
        """Restricted Non-Technical Elective Courses (NTE):
MAN101, Introduction to Management, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:2, R:2, T:0
ECON101, Introduction to Economics, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:2, R:2, T:0
FRE101, French I, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:1, C:1, R:1, T:0
FRE102, French II, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
GER101, German I, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:1, C:1, R:1, T:0
GER102, German II, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:1, C:1, R:2, T:1
PHIL101, Introduction to Philosophy, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:1
HIST103, History of Civilization, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:1
POL101, Political Science I, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:1
SOC101, Sociology, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:1, R:1, T:1""",

        # Program Summary and Career Opportunities
        """Industrial Engineering Program Summary:
Degree: Bachelor of Science in Industrial Engineering
Duration: 4 years (8 semesters)
Total Credits: 143
Total ECTS: 240

Program Focus Areas:
- Operations Research and Optimization
- Production and Operations Management
- Supply Chain and Logistics
- Quality Engineering and Six Sigma
- Systems Analysis and Design
- Industrial 4.0 and Digitalization
- Ergonomics and Human Factors
- Project Management
- Entrepreneurship and Innovation

Career Opportunities:
Industrial Engineer
Production Manager
Quality Engineer
Supply Chain Manager
Operations Research Analyst
Process Improvement Specialist
Project Manager
Consultant
Data Analyst
Systems Engineer
Lean Manufacturing Specialist
Logistics Coordinator

Professional Recognition:
Graduates are qualified to work in manufacturing, healthcare, logistics, consulting, technology, and service industries worldwide."""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Engineering",
            "department": "Industrial Engineering",
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
            "content_type": "technical_electives_31x"
        },
        {
            "course_type": "elective",
            "elective_type": "technical",
            "document_type": "course_list",
            "content_type": "technical_electives_41x"
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
    ids = [f"industrial_eng_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Industrial Engineering curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["operations research industrial engineering"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_industrial_engineering_curriculum_to_chromadb()