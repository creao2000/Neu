

# import chromadb

# # Initialize ChromaDB client
# chroma_client = chromadb.PersistentClient(path="./chroma_db")

# # List all collections first to confirm
# collections = chroma_client.list_collections()
# print("Current collections:", [col.name for col in collections])

# # Delete the specific collection
# try:
#     chroma_client.delete_collection(name="neu_cis_curriculum")
#     print("✅ Collection 'neu_cis_curriculum' deleted successfully!")
# except Exception as e:
#     print(f"❌ Error deleting collection: {e}")

# # Verify it's gone
# collections = chroma_client.list_collections()
# print("Remaining collections:", [col.name for col in collections])




import chromadb
from chromadb.utils import embedding_functions

def add_cis_curriculum_to_chromadb():
    """Add Computer Information Systems curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_cis_curriculum",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_cis_curriculum",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_cis_curriculum")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """Computer Information Systems Department (CIS)
Information Systems Engineer (Bachelor's Degree/ first cycle in Bologna System)
Main website link: https://aif.neu.edu.tr/
Curriculum link: https://aif.neu.edu.tr/academic/academic-programmes/department-of-computer-information-systems/

T (Theory Hours): The number of hours dedicated to lectures or theoretical learning in the course.
P (Practice Hours): The number of hours spent on practical work, labs, or hands-on activities.
C (Credits): The credit value assigned to the course, reflecting its academic weight.
E (ECTS): European Credit Transfer and Accumulation System, representing the workload and learning outcomes.

Course Type Legend:
C = Compulsory Course
E = Elective Course""",

        # 1st Semester
        """First Year - First Semester Courses (Year One or 1 First Semester):
ENG101, ENGLISH I, T: 3, P: 0, C: 2, E: 3
MTH171, MATHEMATICS FOR BUSINESS AND ECONOMICS I, T: 3, P: 0, C: 3, E: 6
EAS101, PRINCIPLES OF ECONOMICS I, T: 3, P: 0, C: 3, E: 7
EAS103, INTRODUCTION TO BUSINESS, T: 3, P: 0, C: 3, E: 6
CIS131, INTRO. TO COMPUTER INFORMATION SYSTEMS, T: 3, P: 0, C: 3, E: 4
YİT101/TUR101, TURKISH FOR INTERNATIONAL STUDENTS I / TURKISH LANGUAGE I, T: 2, P: 0, C: 2, E: 2
CAM100, CAMPUS ORIENTATION, T: 0, P: 0, C: 0, E: 2

Total: T: 17, P: 0, C: 16, E: 30""",

        # 2nd Semester
        """First Year - Second Semester Courses (Year One or 1 Second Semester):
ENG102, ENGLISH II, T: 3, P: 0, C: 2, E: 3
MTH172, MATHEMATICS FOR BUSINESS AND ECONOMICS II, T: 3, P: 0, C: 3, E: 6
EAS102, PRINCIPLES OF ECONOMICS II, T: 3, P: 0, C: 3, E: 7
EAS104, PRINCIPLES OF MANAGEMENT, T: 3, P: 0, C: 3, E: 6
CIS132, INTRO. TO ALGORITHM AND PROGRAMMING, T: 3, P: 0, C: 3, E: 4
YİT102/TUR102, TURKISH FOR INTERNATIONAL STUDENTS II / TURKISH LANGUAGE II, T: 2, P: 0, C: 2, E: 2
GEC351, 21st CENTURY SKILLS, T: 0, P: 0, C: 0, E: 2

Total: T: 19, P: 0, C: 16, E: 30""",

        # 3rd Semester
        """Second Year - First Semester Courses (Year Two or 2 First Semester):
MAN201, COMMUNICATION FOR BUSINESS I, T: 3, P: 0, C: 3, E: 4
CIS205, FUNDAMENTALS OF PROGRAMMING, T: 2, P: 2, C: 3, E: 4
MTH261, STATISTICS I, T: 3, P: 0, C: 3, E: 6
CIS243, ESSENTIAL DATA STRUCTURES AND APPLICATIONS, T: 3, P: 0, C: 3, E: 6
EAS203, FINANCIAL ACCOUNTING I, T: 3, P: 0, C: 3, E: 6
AIT101/AIT103, ATATURK'S PRINCIPLES AND HISTORY OF TURKISH REVOLUTION I, T: 2, P: 0, C: 2, E: 2
CHC100, CYPRUS HISTORY AND CULTURE, T: 2, P: 0, C: 2, E: 2

Total: T: 18, P: 2, C: 19, E: 30""",

        # 4th Semester
        """Second Year - Second Semester Courses (Year Two or 2 Second Semester):
CIS202, SYSTEM SOFTWARE AND OPERATING ENVIRONMENTS, T: 3, P: 0, C: 3, E: 4
CIS232, ADVANCED PROGRAMMING TECHNIQUES, T: 2, P: 2, C: 3, E: 6
MTH262, STATISTICS II, T: 3, P: 0, C: 3, E: 6
CIS246, DATABASE SYSTEMS FOR INFORMATION MANAGEMENT, T: 2, P: 2, C: 3, E: 6
CIS242, TECHNICAL ELECTIVE, T: 0, P: 2, C: 3, E: 4
AIT102/AIT104, ATATURK'S PRINCIPLES AND HISTORY OF TURKISH REVOLUTION II, T: 2, P: 0, C: 2, E: 2
CAR100, CAREER PLANNING, T: 0, P: 0, C: 0, E: 2

Total: T: 14, P: 6, C: 17, E: 30""",

        # 5th Semester
        """Third Year - First Semester Courses (Year Three or 3 First Semester):
EAS305, PRINCIPLES OF MARKETING, T: 3, P: 0, C: 3, E: 6
CIS331, INFORMATION SYSTEMS ANALYSIS AND DESIGN, T: 3, P: 0, C: 3, E: 6
CIS363, SOFTWARE DESIGN AND IMPLEMENTATION, T: 3, P: 0, C: 3, E: 6
CIS340, WEB PROGRAMMING TECHNIQUES, T: 2, P: 2, C: 3, E: 6
CIS386, STRUCTURED QUERY PROGRAMMING, T: 2, P: 2, C: 3, E: 6

Total: T: 13, P: 4, C: 15, E: 30""",

        # 6th Semester
        """Third Year - Second Semester Courses (Year Three or 3 Second Semester):
EAS308, OPERATIONS RESEARCH AND MANAGEMENT, T: 3, P: 0, C: 3, E: 6
CIS348, E-BUSINESS SYSTEMS, T: 2, P: 2, C: 3, E: 6
CIS352, APPLICATION DEVELOPMENT WITH ADVANCED PROGRAMMING, T: 2, P: 2, C: 3, E: 6
CIS342, ETHICAL AND SOCIAL ISSUES IN INFORMATION SYSTEMS, T: 3, P: 0, C: 3, E: 6
CIS356, INTRODUCTION TO OBJECT-ORIENTED DESIGN, T: 2, P: 2, C: 3, E: 6

Total: T: 12, P: 6, C: 15, E: 30""",

        # 7th Semester
        """Fourth Year - First Semester Courses (Year Four or 4 First Semester - Final Year First Semester):
CIS468, ADVANCED PROGRAMMING IN APPLICATION FRAMEWORKS, T: 2, P: 2, C: 3, E: 6
CIS403, GRADUATION PROJECT PROPOSAL, T: 3, P: 0, C: 3, E: 3
CIS406, SUMMER TRAINING, T: 0, P: 0, C: 0, E: 3
EAS402, HUMAN RESOURCE MANAGEMENT, T: 3, P: 0, C: 3, E: 6
TE, TECHNICAL ELECTIVE, T: 2, P: 2, C: 3, E: 4
TE, TECHNICAL ELECTIVE, T: 2, P: 2, C: 3, E: 4
TE, TECHNICAL ELECTIVE, T: 2, P: 2, C: 3, E: 4

Total: T: 14, P: 8, C: 18, E: 30""",

        # 8th Semester
        """Fourth Year - Second Semester Courses (Year Four or 4 Second Semester - Final Year Second Semester):
CIS411, MANAGEMENT INFORMATION SYSTEMS, T: 3, P: 0, C: 3, E: 6
CIS400, GRADUATION PROJECT, T: 3, P: 0, C: 3, E: 6
TE, TECHNICAL ELECTIVE, T: 2, P: 2, C: 3, E: 6
TE, TECHNICAL ELECTIVE, T: 2, P: 2, C: 3, E: 4
TE, TECHNICAL ELECTIVE, T: 2, P: 2, C: 3, E: 4
TE, TECHNICAL ELECTIVE, T: 2, P: 2, C: 3, E: 4

Total: T: 14, P: 8, C: 18, E: 30""",

        # Elective Courses
        """Technical Elective Courses (TE) - Available Options:
CIS242, ANIMATION TECHNOLOGIES, T: 2, P: 2, C: 3, E: 4
CIS401, E-GOVERNMENT, T: 2, P: 2, C: 3, E: 4
CIS412, CRYPTOGRAPHY AND CODING THEORY, T: 2, P: 2, C: 3, E: 4
CIS414, MULTIMEDIA SYSTEMS, T: 2, P: 2, C: 3, E: 4
CIS415, GEOGRAPHIC INFORMATION SYSTEMS, T: 2, P: 2, C: 3, E: 4
CIS416, COMPUTER NETWORKS, T: 2, P: 2, C: 3, E: 4
CIS418, TELECOMMUNICATION IN BUSINESSES, T: 2, P: 2, C: 3, E: 4
CIS419, INTRODUCTION TO ARTIFICIAL INTELLIGENCE, T: 2, P: 2, C: 3, E: 4
CIS420, INFORMATION SYSTEMS SECURITY, T: 2, P: 2, C: 3, E: 4
CIS421, TESTING FUNDAMENTALS IN SOFTWARE DEVELOPMENT, T: 2, P: 2, C: 3, E: 4
CIS430, INFORMATION SYSTEMS FOR COMMUNICATION, T: 2, P: 2, C: 3, E: 4
CIS432, DECISION MAKING SYSTEMS, T: 2, P: 2, C: 3, E: 4
CIS435, E-LEARNING SYSTEMS, T: 2, P: 2, C: 3, E: 4
CIS436, WEB TECHNOLOGIES, T: 2, P: 2, C: 3, E: 4
CIS450, IT PROJECT MANAGEMENT, T: 2, P: 2, C: 3, E: 4
CIS460, MOBILE APPLICATION DEVELOPMENT, T: 2, P: 2, C: 3, E: 4
CIS468, ADVANCED PROGRAMMING IN APPLICATION FRAMEWORKS, T: 2, P: 2, C: 3, E: 6
CIS480, DATA SCIENCE, T: 2, P: 2, C: 3, E: 6
CIS485, INFOGRAPHIC DESIGN, T: 2, P: 2, C: 3, E: 6
CIS486, DATABASE PROGRAMMING II, T: 2, P: 2, C: 3, E: 4
CIS488, WEB DEVELOPMENT, T: 2, P: 2, C: 3, E: 4
CIS489, SOCIAL MEDIA MANAGEMENT, T: 2, P: 2, C: 3, E: 4
CIS490, IT AND SUSTAINABILITY, T: 2, P: 2, C: 3, E: 4
CIS491, DIGITAL TRANSFORMATION FOR SUSTAINABLE BUSINESSES, T: 2, P: 2, C: 3, E: 4""",

        # Mission and Vision
        """Mission and Vision:

Mission
The mission of the Bachelor's Program in Computer Information Systems is to contribute to society, industry, and academia by educating qualified professionals in the fields of informatics systems and information technologies. The program aims to equip students with a strong foundation in computer science, information systems, and business process management, integrating both theoretical knowledge and practical skills alongside research competence. It seeks to cultivate individuals who are sensitive to current technological advancements, adhere to ethical standards, and embrace innovation. Through project-based learning and collaborative group work, students apply up-to-date technologies to analyze real-world problems and develop solutions or applications that facilitate daily life. In doing so, they enhance both their technical and managerial competencies. Furthermore, the program aspires to educate individuals who are responsive to societal needs, open to lifelong learning, and capable of engaging in interdisciplinary work.

Vision
The vision of the Bachelor's Program in Computer Information Systems is to become an innovative and solution-oriented academic program that is recognized at both national and international levels in the fields of informatics systems and information technologies. The program prioritizes quality in education, sustainability in research, and impact in societal contribution, aiming to educate individuals capable of shaping technological advancements. With a focus on data-driven decision-making, digital transformation, and a multidisciplinary work culture, the program aspires to be a leading department that contributes to the advancement of the information technology sector and academia.""",

        # Program Summary
        """Computer Information Systems Program Summary:
- Department: Computer Information Systems (CIS)
- Degree: Bachelor of Science
- Total Semesters: 8
- Total Courses: 50+
- Total ECTS Credits: 240
- Language of Instruction: English
- Focus Areas: Information Systems, Business Technology, Software Development, Database Management

Key Specializations:
- Information Systems Analysis and Design
- Business Process Management
- Web and Application Development
- Database Systems and Management
- E-Business Systems
- IT Project Management""",

        # Career Opportunities
        """Career Opportunities for CIS Graduates:
Information Systems Analyst
Business Systems Analyst
IT Consultant
Software Developer
Database Administrator
Web Developer
Systems Administrator
IT Project Manager
Business Intelligence Analyst
E-Business Specialist
Data Analyst
Network Administrator
IT Support Specialist
Digital Transformation Consultant"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "department": "Computer Information Systems",
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
            "content_type": "mission_vision"
        },
        {
            "document_type": "program_info",
            "content_type": "program_summary"
        },
        {
            "document_type": "program_info",
            "content_type": "career_opportunities"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"cis_curriculum_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Computer Information Systems curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["information systems business technology courses"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_cis_curriculum_to_chromadb()

