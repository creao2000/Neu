import chromadb
from chromadb.utils import embedding_functions

def add_information_systems_engineering_curriculum_to_chromadb():
    """Add Information Systems Engineering curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_information_systems_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_information_systems_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_information_systems_engineering")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """Department of Information Systems Engineering
Bachelor of Information Systems Engineering Curriculum Overview
Main website link: https://aif.neu.edu.tr/
Curriculum link: https://aif.neu.edu.tr/academic/academic-programmes/department-of-information-system-engineering/

T (Theory Hours): The number of hours dedicated to lectures or theoretical learning in the course.
P (Practice Hours): The number of hours spent on practical work, labs, or hands-on activities.
C (Credits): The credit value assigned to the course, reflecting its academic weight.
E (ECTS): European Credit Transfer and Accumulation System, representing the workload and learning outcomes.

Course Type Legend:
C = Compulsory Course
E = Elective Course""",

        # 1st Semester
        """First Year - First Semester Courses (Year One or 1 First Semester):
CHM101, G. CHEMISTRY, T: 3, P: 2, C: 4, E: 5
ENG101, ENGLISH I, T: 2, P: 0, C: 2, E: 3
PHY101, G. PHYSICS I, T: 3, P: 2, C: 4, E: 5
MTH101, MATHEMATICS I, T: 4, P: 0, C: 4, E: 5
AII102, PROGRAMMING AND PROBLEM SOLVING, T: 3, P: 2, C: 4, E: 5
CAM100, CAMPUS ORIENTATION, T: 2, P: 0, C: 0, E: 2

Total: T: 20, P: 6, C: 21, E: 30""",

        # 2nd Semester
        """First Year - Second Semester Courses (Year One or 1 Second Semester):
AII108, OBJECT-ORIENTED PROGRAMMING, T: 2, P: 2, C: 3, E: 6
ENG102, ENGLISH II, T: 3, P: 0, C: 2, E: 3
MTH102, MATHEMATICS II, T: 4, P: 0, C: 4, E: 6
AII104, DISCRETE STRUCTURES, T: 3, P: 0, C: 3, E: 5
PHY102, G. PHYSICS II, T: 3, P: 2, C: 4, E: 6
CAR100, CAREER, T: 2, P: 0, C: 0, E: 2
GEC351, 21ST CENTURY SKILLS, T: 2, P: 0, C: 0, E: 2

Total: T: 19, P: 4, C: 16, E: 30""",

        # 3rd Semester
        """Second Year - First Semester Courses (Year Two or 2 First Semester):
AII201, DATA STRUCTURES AND ALGORITHMS, T: 3, P: 2, C: 4, E: 6
AII001, LOGIC DESIGN, T: 3, P: 2, C: 4, E: 6
AII020, SYSTEM ANALYSIS AND DESIGN, T: 3, P: 0, C: 3, E: 5
AII427, MANAGEMENT FOR ENGINEERS, T: 3, P: 0, C: 3, E: 5
MTH251/MTH201, PROBABILITY AND STATISTICS/DIFFERENTIAL EQUATIONS, T: 3, P: 0, C: 3, E: 6
YIT101/TUR101, TURKISH FOR FOREIGN STUDENTS I, T: 2, P: 0, C: 2, E: 2

Total: T: 17, P: 4, C: 19, E: 30""",

        # 4th Semester
        """Second Year - Second Semester Courses (Year Two or 2 Second Semester):
AII202, DATABASE MANAGEMENT SYSTEMS, T: 4, P: 0, C: 4, E: 5
AII006, WEB DESIGN AND PROGRAMMING, T: 2, P: 2, C: 3, E: 4
AII426, ECONOMICS FOR ENGINEERS, T: 3, P: 0, C: 3, E: 6
AII007, MULTIMEDIA SYSTEMS, T: 2, P: 2, C: 3, E: 4
ISE206, PROJECT MANAGEMENT, T: 3, P: 0, C: 2, E: 3
YIT102/TUR102, TURKISH FOR FOREIGN STUDENTS II/TURKISH II, T: 2, P: 0, C: 2, E: 2
ISE299, SUMMER TRAINING I, T: 0, P: 0, C: 0, E: 6

Total: T: 16, P: 4, C: 17, E: 30""",

        # 5th Semester
        """Third Year - First Semester Courses (Year Three or 3 First Semester):
AII302, OPERATING SYSTEMS, T: 3, P: 0, C: 3, E: 6
AII004, PROGRAMMING LANGUAGES I, T: 2, P: 2, C: 3, E: 7
ENG201, ORAL COMMUNICATION SKILLS, T: 3, P: 0, C: 3, E: 4
AII311, MANAGEMENT INFORMATION SYSTEMS FOR ENGINEERS, T: 4, P: 0, C: 4, E: 7
AII439, OCCUPATIONAL HEALTH AND SAFETY I, T: 2, P: 0, C: 2, E: 4
AIT103/AIT101, PRINCIPLES OF ATATÜRK AND THE HISTORY OF TURKISH REVOLUTION I, T: 2, P: 0, C: 2, E: 2

Total: T: 16, P: 2, C: 17, E: 30""",

        # 6th Semester
        """Third Year - Second Semester Courses (Year Three or 3 Second Semester):
CS322, WEB APPLICATION DEVELOPMENT, T: 2, P: 2, C: 3, E: 4
AII303, DATA COMMUNICATION AND NETWORKING, T: 2, P: 2, C: 4, E: 5
ISE301, GEOGRAPHIC INFORMATION SYSTEMS, T: 3, P: 2, C: 4, E: 5
AII003, SOFTWARE ENGINEERING, T: 3, P: 0, C: 3, E: 6
CHC100, CYPRUS: HISTORY AND CULTURE, T: 2, P: 0, C: 0, E: 2
AIT104/AIT102, PRINCIPLES OF ATATÜRK AND THE HISTORY OF TURKISH REVOLUTION II, T: 2, P: 0, C: 2, E: 2
ISE399, SUMMER TRAINING II, T: 0, P: 0, C: 0, E: 6

Total: T: 14, P: 6, C: 16, E: 30""",

        # 7th Semester
        """Fourth Year - First Semester Courses (Year Four or 4 First Semester - Final Year First Semester):
AII428, e-Government, T: 3, P: 0, C: 3, E: 5
AII430, PRINCIPLES OF INFORMATION SECURITY, T: 3, P: 0, C: 3, E: 6
ISE491, GRADUATION PROJECT I, T: 0, P: 6, C: 3, E: 4
AII452, ARTIFICIAL INTELLIGENCE APPLICATIONS, T: 2, P: 2, C: 3, E: 3
AII010, SAFETY IN INFORMATICS, T: 2, P: 0, C: 3, E: 2
TE, TECHNICAL ELECTIVE, T: 3, P: 0, C: 3, E: 5
TE, TECHNICAL ELECTIVE, T: 3, P: 0, C: 3, E: 5

Total: T: 16, P: 8, C: 21, E: 30""",

        # 8th Semester
        """Fourth Year - Second Semester Courses (Year Four or 4 Second Semester - Final Year Second Semester):
AII429, ENGINEERING ETHICS, T: 3, P: 0, C: 3, E: 6
ISE492, GRADUATION PROJECT II, T: 0, P: 6, C: 3, E: 5
AII422, SOFTWARE TESTING, T: 2, P: 2, C: 3, E: 4
TE, TECHNICAL ELECTIVE, T: 2, P: 2, C: 3, E: 5
TE, TECHNICAL ELECTIVE, T: 2, P: 2, C: 3, E: 5
TE, TECHNICAL ELECTIVE, T: 2, P: 2, C: 3, E: 5

Total: T: 11, P: 8, C: 18, E: 30""",

        # Technical Elective Courses
        """Technical Elective Courses (TE) - Available Options:
AII431, e-Commerce, T: 2, P: 2, C: 3, E: 5
AII412, Database Applications, T: 2, P: 2, C: 3, E: 5
AII002, System Simulation, T: 3, P: 0, C: 3, E: 5
ISE412, Health Information Management, T: 3, P: 0, C: 3, E: 5
ISE413, Strategic Information Systems Management, T: 3, P: 0, C: 3, E: 5
ISE414, Information in Hospitality & Tourism, T: 3, P: 0, C: 3, E: 5
ISE415, Accounting Information Systems, T: 3, P: 0, C: 3, E: 5
ISE430, Human-Computer Interaction, T: 3, P: 0, C: 3, E: 5
AII404, Neural Networks, T: 2, P: 2, C: 3, E: 5
AII419, Image Processing, T: 2, P: 2, C: 3, E: 5
AII005, Internet Programming, T: 2, P: 2, C: 3, E: 5
AII402, Computer Graphics, T: 2, P: 2, C: 3, E: 5
AII405, Computer Hardware, T: 3, P: 0, C: 3, E: 5
AII406, System Programming, T: 2, P: 2, C: 3, E: 5
AII413, Introduction to Artificial Intelligence, T: 3, P: 0, C: 3, E: 5
ISE428, Forensic Information Systems, T: 2, P: 2, C: 3, E: 5
AII417, Mobile Programming, T: 2, P: 2, C: 3, E: 5
AII408, Advanced Object-Oriented Programming, T: 2, P: 2, C: 3, E: 5
AII409, Object-Oriented Programming II, T: 2, P: 2, C: 3, E: 5
AII351, Embedded Systems, T: 2, P: 2, C: 3, E: 5
AII407, Programming Languages II, T: 2, P: 2, C: 3, E: 5
AII415, Decision Making, T: 3, P: 0, C: 3, E: 5""",

        # Program Summary
        """Information Systems Engineering Program Summary:
Total Courses: 53
Electives: 14
Total Credits: 145
Elective Percentage: 26.4%
Total ECTS: 240

Program Focus Areas:
- Information Systems Analysis and Design
- Database Management Systems
- Software Engineering
- Web and Application Development
- Information Security
- Management Information Systems
- Geographic Information Systems
- Artificial Intelligence Applications

Key Features:
- Strong foundation in both technical and management aspects
- Emphasis on practical applications and project work
- Integration of business and technology perspectives
- Focus on emerging technologies and information systems""",

        # Career Opportunities
        """Career Opportunities for Information Systems Engineering Graduates:
Information Systems Engineer
Systems Analyst
Database Administrator
IT Project Manager
Information Security Specialist
Web Application Developer
Software Engineer
Business Intelligence Analyst
GIS Specialist
IT Consultant
Network Administrator
ERP Specialist
Data Analyst
Systems Architect
Technology Consultant""",

        # Program Objectives
        """Program Educational Objectives:
1. To provide students with strong foundation in information systems engineering principles
2. To develop skills in analyzing, designing, and implementing information systems
3. To integrate technical knowledge with business and management perspectives
4. To prepare graduates for careers in various sectors requiring information systems expertise
5. To foster innovation and problem-solving capabilities in information systems development
6. To emphasize ethical practices and social responsibility in information systems engineering

Program Learning Outcomes:
Graduates will be able to:
- Analyze complex business problems and design appropriate information system solutions
- Develop and implement database systems and web applications
- Apply software engineering principles to information systems development
- Manage information systems projects effectively
- Ensure information security and privacy in system design
- Integrate emerging technologies into information systems solutions"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "department": "Information Systems Engineering",
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
            "content_type": "program_summary"
        },
        {
            "document_type": "program_info",
            "content_type": "career_opportunities"
        },
        {
            "document_type": "program_info",
            "content_type": "program_objectives"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"ise_curriculum_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Information Systems Engineering curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["information systems engineering database management"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_information_systems_engineering_curriculum_to_chromadb()