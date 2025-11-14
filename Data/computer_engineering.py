import chromadb
from chromadb.utils import embedding_functions

def add_computer_engineering_curriculum_to_chromadb():
    """Add Computer Engineering curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_computer_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_computer_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_computer_engineering")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """Department of Computer Engineering
Bachelor of Computer Engineering Curriculum Overview
Main website link: https://aif.neu.edu.tr/
Curriculum link: https://aif.neu.edu.tr/academic/academic-programmes/department-of-computer-engineering/

T (Theory Hours): The number of hours dedicated to lectures or theoretical learning in the course.
P (Practice Hours): The number of hours spent on practical work, labs, or hands-on activities.
C (Credits): The credit value assigned to the course, reflecting its academic weight.
E (ECTS): European Credit Transfer and Accumulation System, representing the workload and learning outcomes.

Course Type Legend:
C = Compulsory Course
E = Elective Course""",

        # 1st Semester
        """First Year - First Semester Courses (Year One or 1 First Semester):
COM106, Introduction to Programming, Type: C, T: 3, P: 2, C: 4, E: 6
CHM101, General Chemistry, Type: C, T: 3, P: 2, C: 4, E: 5
ENG101, English I, Type: C, T: 3, P: 0, C: 2, E: 3
MTH101, Calculus I, Type: C, T: 4, P: 0, C: 4, E: 5
PHY101, General Physics I, Type: C, T: 3, P: 2, C: 4, E: 5
CAM100, Campus Orientation, Type: C, T: 2, P: 0, C: 0, E: 2
YİT101/TUR101, Turkish for Foreigners I / Turkish Language I, Type: C, T: 2, P: 0, C: 2, E: 2
COM001, Computer Engineering Orientation, Type: C, T: 2, P: 0, C: 0, E: 2

Total: T: 22, P: 6, C: 20, E: 30""",

        # 2nd Semester
        """First Year - Second Semester Courses (Year One or 1 Second Semester):
AII104, Discrete Structures, Type: C, T: 3, P: 0, C: 3, E: 5
AII102, Programming & Problem Solving, Type: C, T: 3, P: 2, C: 4, E: 6
ENG102, English II, Type: C, T: 3, P: 2, C: 2, E: 3
MTH102, Calculus II, Type: C, T: 4, P: 0, C: 4, E: 6
PHY102, General Physics II, Type: C, T: 3, P: 2, C: 4, E: 6
YİT102/TUR102, Turkish for Foreigners II / Turkish Language II, Type: C, T: 2, P: 0, C: 2, E: 2
GEC351, 21st Century Skills, Type: E, T: 2, P: 0, C: 0, E: 2

Total: T: 20, P: 4, C: 19, E: 30""",

        # 3rd Semester
        """Second Year - First Semester Courses (Year Two or 2 First Semester):
AII001, Logic Design, Type: C, T: 3, P: 2, C: 4, E: 6
AII201, Data Structures & Algorithms, Type: C, T: 3, P: 2, C: 4, E: 6
AII204, Electrical Circuits, Type: C, T: 3, P: 0, C: 3, E: 5
MTH201, Differential Equations, Type: C, T: 4, P: 0, C: 4, E: 6
AİT103/AİT101, Atatürk Principles & Reforms I, Type: C, T: 2, P: 0, C: 2, E: 2
MTH113, Linear Algebra, Type: C, T: 3, P: 0, C: 3, E: 5

Total: T: 18, P: 4, C: 20, E: 30""",

        # 4th Semester
        """Second Year - Second Semester Courses (Year Two or 2 Second Semester):
AII202, Database Management Systems, Type: C, T: 3, P: 2, C: 4, E: 5
AII203, Computer Architecture and Organization, Type: C, T: 3, P: 2, C: 4, E: 5
COM208, Electronics I, Type: C, T: 3, P: 2, C: 4, E: 5
ENG201, English Communication Skills, Type: C, T: 3, P: 0, C: 3, E: 4
AİT104/AİT102, Atatürk Principles & Reforms II, Type: C, T: 2, P: 0, C: 2, E: 2
RE, Restricted Electives, Type: E, T: 3, P: 0, C: 3, E: 4
COM200, Summer Training I, Type: C, T: 0, P: 0, C: 0, E: 5

Total: T: 17, P: 6, C: 20, E: 30""",

        # 5th Semester
        """Third Year - First Semester Courses (Year Three or 3 First Semester):
AII302, Operating Systems, Type: C, T: 3, P: 0, C: 3, E: 6
COM362, Signals and Systems for Computer Engineers, Type: C, T: 3, P: 2, C: 4, E: 6
COM339, Programming Language Concepts, Type: C, T: 3, P: 0, C: 3, E: 5
MTH251, Probability and Statistics, Type: C, T: 3, P: 0, C: 3, E: 6
COM344, Automata Theory, Type: C, T: 3, P: 0, C: 3, E: 5
CAR100, Career Planning, Type: C, T: 2, P: 0, C: 0, E: 2

Total: T: 17, P: 2, C: 16, E: 30""",

        # 6th Semester
        """Third Year - Second Semester Courses (Year Three or 3 Second Semester):
AII351, Embedded Systems, Type: C, T: 3, P: 2, C: 4, E: 5
AII303, Data Communications and Networking, Type: C, T: 3, P: 2, C: 4, E: 5
COM333, Operational Research, Type: E, T: 3, P: 0, C: 3, E: 5
COM382, Real Time Systems, Type: E, T: 3, P: 0, C: 3, E: 5
AII002, Systems Simulation, Type: C, T: 3, P: 0, C: 3, E: 5
COM300, Summer Training II, Type: C, T: 0, P: 0, C: 0, E: 5

Total: T: 15, P: 4, C: 17, E: 30""",

        # 7th Semester
        """Fourth Year - First Semester Courses (Year Four or 4 First Semester - Final Year First Semester):
COM490, Engineering Design I, Type: C, T: 2, P: 2, C: 3, E: 7
AII003, Software Engineering, Type: C, T: 3, P: 0, C: 3, E: 6
TE, Technical Elective, Type: E, T: 3, P: 0, C: 3, E: 5
TE, Technical Elective, Type: E, T: 3, P: 0, C: 3, E: 5
TE, Technical Elective, Type: E, T: 3, P: 0, C: 3, E: 5
CHC100, Cyprus: History and Culture, Type: E, T: 2, P: 0, C: 0, E: 2

Total: T: 16, P: 2, C: 15, E: 30""",

        # 8th Semester
        """Fourth Year - Second Semester Courses (Year Four or 4 Second Semester - Final Year Second Semester):
COM491, Engineering Design II, Type: C, T: 2, P: 2, C: 3, E: 7
AII426, Economics For Engineers, Type: E, T: 3, P: 0, C: 3, E: 6
FE, Free Elective, Type: E, T: 3, P: 0, C: 3, E: 5
TE, Technical Elective, Type: E, T: 3, P: 0, C: 3, E: 5
TE, Technical Elective, Type: E, T: 3, P: 0, C: 3, E: 5
AII010, Safety in Informatics, Type: E, T: 2, P: 0, C: 3, E: 2

Total: T: 16, P: 2, C: 18, E: 30""",

        # Technical Elective Courses
        """Technical Elective Courses (TE) - Available Options:
AII401, Microprocessor Systems, T: 3, P: 0, C: 3, E: 5
AII402, Computer Graphics, T: 3, P: 0, C: 3, E: 5
COM410, Parallel Computer Architecture, T: 3, P: 0, C: 3, E: 5
COM414, Digital Control Systems, T: 3, P: 0, C: 3, E: 5
COM416, Computer Networks, T: 3, P: 0, C: 3, E: 5
AII404, Neural Networks, T: 3, P: 0, C: 3, E: 5
AII405, Computer Hardware, T: 3, P: 0, C: 3, E: 5
AII406, System Programming, T: 3, P: 0, C: 3, E: 5
COM430, Programming Languages I, T: 3, P: 0, C: 3, E: 5
AII407, Programming Languages II, T: 3, P: 0, C: 3, E: 5
AII005, Internet Programming, T: 3, P: 0, C: 3, E: 5
AII408, Advanced Object Oriented Programming, T: 3, P: 0, C: 3, E: 5
AII409, Object Oriented Programming II, T: 3, P: 0, C: 3, E: 5
COM447, Advanced Operating System, T: 3, P: 0, C: 3, E: 5
AII411, Digital Signal Processing, T: 3, P: 0, C: 3, E: 5
AII412, Database Applications, T: 3, P: 0, C: 3, E: 5
AII413, Introduction to Artificial Intelligence, T: 3, P: 0, C: 3, E: 5
COM452, Introduction to Parallel Computing, T: 3, P: 0, C: 3, E: 5
AII415, Decision Making, T: 3, P: 0, C: 3, E: 5
COM454, Advanced Computer Architecture and Organization, T: 3, P: 0, C: 3, E: 5
AII417, Mobile Computing, T: 3, P: 0, C: 3, E: 5
AII419, Digital Image Processing, T: 3, P: 0, C: 3, E: 5
COM471, Hardware Design using FPGAs, T: 3, P: 0, C: 3, E: 5
AII006, Web Design and Programming, T: 3, P: 0, C: 3, E: 5
AII007, Multimedia Systems, T: 3, P: 0, C: 3, E: 5
AII435, Mechatronics, T: 3, P: 0, C: 3, E: 5
AII423, Robotic Systems, T: 3, P: 0, C: 3, E: 5
AII445, Introduction to Machine Learning, T: 3, P: 0, C: 3, E: 5
AII439, Occupational Safety (Elective), T: 2, P: 0, C: 3, E: 3""",

        # Restricted and Free Electives
        """Restricted Electives (RE) and Free Electives (FE):
Restricted Electives:
MTH323, Numerical Analysis, T: 3, P: 0, C: 3, E: 4
COM315, Algorithms, T: 3, P: 0, C: 3, E: 4
AII217, Microbiology, T: 3, P: 0, C: 3, E: 4
BME102, Biochemistry, T: 3, P: 0, C: 3, E: 4

Free Electives:
AII427, Management for Engineers, T: 3, P: 0, C: 3, E: 5
BME102, One of Technical Electives, T: 3, P: 0, C: 3, E: 5""",

        # Program Summary
        """Computer Engineering Program Summary:
Total Courses: 52
Total Electives: 13
Total Credits: 145
Percentage of Electives: 25%
Total ECTS: 240

Previous Total Credits: 147
New Total Credits: 145
Previous Total ECTS: 242
New Total ECTS: 240

Program Focus Areas:
- Computer Hardware and Architecture
- Software Engineering and Programming
- Embedded Systems and Electronics
- Computer Networks and Communications
- Operating Systems and System Programming
- Artificial Intelligence and Machine Learning
- Database Systems and Applications

Key Features:
- Strong foundation in both hardware and software
- Emphasis on engineering design and practical applications
- Integration of theoretical knowledge with hands-on experience
- Focus on emerging technologies and computer systems""",

        # Career Opportunities
        """Career Opportunities for Computer Engineering Graduates:
Computer Hardware Engineer
Software Engineer
Embedded Systems Engineer
Network Engineer
Systems Architect
Database Administrator
IT Consultant
Mobile Application Developer
AI/ML Engineer
Robotics Engineer
Computer Systems Analyst
Research and Development Engineer
Technical Project Manager
Cybersecurity Specialist""",

        # Program Objectives
        """Program Educational Objectives:
1. To provide comprehensive education in computer engineering principles and practices
2. To develop skills in both hardware and software design and implementation
3. To prepare graduates for careers in various sectors requiring computer engineering expertise
4. To foster innovation and problem-solving capabilities in computer systems development
5. To emphasize ethical practices and professional responsibility in engineering
6. To integrate theoretical knowledge with practical applications through hands-on projects

Program Learning Outcomes:
Graduates will be able to:
- Design and implement computer hardware and software systems
- Analyze and solve complex engineering problems using computational methods
- Develop embedded systems and real-time applications
- Design and manage computer networks and communication systems
- Apply software engineering principles to develop reliable and efficient software
- Work effectively in multidisciplinary teams and communicate technical information
- Engage in lifelong learning and adapt to evolving technologies"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "department": "Computer Engineering",
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
            "course_type": "elective",
            "document_type": "course_list",
            "content_type": "restricted_free_electives"
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
    ids = [f"ce_curriculum_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Computer Engineering curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["computer engineering hardware software"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_computer_engineering_curriculum_to_chromadb()