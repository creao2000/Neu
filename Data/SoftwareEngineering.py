

# import chromadb

# # Initialize ChromaDB client
# chroma_client = chromadb.PersistentClient(path="./chroma_db")

# # List all collections first to confirm
# collections = chroma_client.list_collections()
# print("Current collections:", [col.name for col in collections])

# # Delete the specific collection
# try:
#     chroma_client.delete_collection(name="neu_software_engineering")
#     print("✅ Collection 'neu_software_engineering' deleted successfully!")
# except Exception as e:
#     print(f"❌ Error deleting collection: {e}")

# # Verify it's gone
# collections = chroma_client.list_collections()
# print("Remaining collections:", [col.name for col in collections])


import chromadb
from chromadb.utils import embedding_functions

def add_software_engineering_curriculum_to_chromadb():
    """Add Software Engineering curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_software_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_software_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_software_engineering")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """Software Engineering Program Information
Bachelor of Software Engineering Curriculum Overview
Main website link: https://aif.neu.edu.tr/
Curriculum link: https://aif.neu.edu.tr/academic/academic-programmes/department-of-software-engineering/

T (Theoretical Study Hours): The number of hours dedicated to lectures or theoretical learning in the course.
P (Practice/Lab Hours): The number of hours spent on practical work, labs, or hands-on activities.
C (Credits): The credit value assigned to the course, reflecting its academic weight.
ECTS (European Credit Transfer and Accumulation System): A standard for comparing study attainment and performance across the European Union, representing the workload and learning outcomes of the course.""",

        # 1st Semester
        """First Year - First Semester Courses (Year One or 1 First Semester):
CHM101, General Chemistry, Type: C, T: 3, P: 2, C: 4, ECTS: 5
AII102, Programming and Problem Solving, Type: C, T: 3, P: 2, C: 4, ECTS: 5
ENG101, English I, Type: C, T: 3, P: 0, C: 3, ECTS: 3
MTH101, Calculus I, Type: C, T: 4, P: 0, C: 4, ECTS: 5
MTH113, Linear Algebra, Type: C, T: 3, P: 0, C: 3, ECTS: 5
PHY101, Physics I, Type: C, T: 3, P: 2, C: 4, ECTS: 5
CAM100, Campus Orientation, Type: C, T: 2, P: 0, C: 0, ECTS: 2

Total: T: 21, P: 6, C: 22, ECTS: 30""",

        # 2nd Semester
        """First Year - Second Semester Courses (Year One or 1 Second Semester):
AII108, Object Oriented Programming, Type: C, T: 2, P: 2, C: 3, ECTS: 6
ENG102, English II, Type: C, T: 3, P: 0, C: 2, ECTS: 3
MTH102, Calculus II, Type: C, T: 4, P: 0, C: 4, ECTS: 6
AII104, Discrete Structures, Type: C, T: 3, P: 0, C: 3, ECTS: 5
PHY102, Physics II, Type: C, T: 3, P: 2, C: 4, ECTS: 6
CAR100, Career Planning, Type: C, T: 2, P: 0, C: 0, ECTS: 2
GEC351, 21st Century Skills, Type: E, T: 2, P: 0, C: 0, ECTS: 2

Total: T: 19, P: 4, C: 16, ECTS: 30""",

        # 3rd Semester
        """Second Year - First Semester Courses (Year Two or 2 First Semester):
AII201, Data Structures and Algorithms, Type: C, T: 3, P: 2, C: 4, ECTS: 6
AII001, Logic Design, Type: C, T: 3, P: 2, C: 4, ECTS: 6
ENG201, Oral Communication Skills, Type: C, T: 3, P: 0, C: 3, ECTS: 4
MTH251, Probability and Statistics, Type: C, T: 3, P: 0, C: 3, ECTS: 6
AII003, Principles of Software Engineering, Type: C, T: 3, P: 0, C: 3, ECTS: 6
CHC100, Cyprus History and Culture, Type: E, T: 2, P: 0, C: 0, ECTS: 2

Total: T: 17, P: 4, C: 17, ECTS: 30""",

        # 4th Semester
        """Second Year - Second Semester Courses (Year Two or 2 Second Semester):
AII203, Computer Organisation and Architecture, Type: C, T: 3, P: 2, C: 4, ECTS: 5
AII202, Database Systems, Type: C, T: 3, P: 2, C: 4, ECTS: 5
SWE202, Software Construction, Type: C, T: 2, P: 2, C: 3, ECTS: 4
SWE234, Human Computer Interaction, Type: C, T: 3, P: 0, C: 3, ECTS: 3
YIT101/TUR101, Turkish Language for International Students, Type: C, T: 2, P: 0, C: 2, ECTS: 2
TE, Technical Elective, Type: E, T: 3, P: 0, C: 3, ECTS: 5
SWE299, Summer Training I, Type: C, T: 0, P: 0, C: 0, ECTS: 6

Total: T: 16, P: 6, C: 19, ECTS: 30""",

        # 5th Semester
        """Third Year - First Semester Courses (Year Three or 3 First Semester):
AII302, Operating Systems, Type: C, T: 3, P: 0, C: 3, ECTS: 6
SWE395, Advanced Object Oriented Programming, Type: C, T: 3, P: 0, C: 3, ECTS: 4
AII311, Management Information Systems for Engineers, Type: C, T: 4, P: 0, C: 4, ECTS: 7
SWE301, Software Design and Architecture, Type: C, T: 3, P: 2, C: 4, ECTS: 5
AII439, Occupational Health and Safety, Type: C, T: 2, P: 0, C: 2, ECTS: 4
AIT103/AIT101, Ataturk's Principles and Reforms, Type: C, T: 2, P: 0, C: 2, ECTS: 2
YIT102/TUR102, Turkish Language for International Students II, Type: C, T: 2, P: 0, C: 2, ECTS: 2

Total: T: 19, P: 2, C: 20, ECTS: 30""",

        # 6th Semester
        """Third Year - Second Semester Courses (Year Three or 3 Second Semester):
AII005, Internet Programming, Type: C, T: 3, P: 0, C: 3, ECTS: 5
AII303, Data Communications and Computer Networks, Type: C, T: 3, P: 2, C: 4, ECTS: 5
SWE302, Software Quality Assurance and Testing, Type: C, T: 2, P: 2, C: 3, ECTS: 4
SWE304, Software Requirements Analysis, Type: E, T: 2, P: 2, C: 3, ECTS: 4
SWE396, Advanced Object Oriented Programming II, Type: C, T: 3, P: 0, C: 3, ECTS: 4
AIT104/AIT102, Ataturk's Principles and Reforms II, Type: C, T: 2, P: 0, C: 2, ECTS: 2
SWE399, Summer Training II, Type: C, T: 0, P: 0, C: 0, ECTS: 6

Total: T: 15, P: 6, C: 18, ECTS: 30""",

        # 7th Semester
        """Fourth Year - First Semester Courses (Year Four or 4 First Semester - Final Year First Semester):
AII430, Principles of Information Security, Type: E, T: 3, P: 0, C: 3, ECTS: 6
AII427, Introduction to Management, Type: E, T: 3, P: 0, C: 3, ECTS: 5
SWE491, Graduation Project I, Type: C, T: 2, P: 0, C: 2, ECTS: 4
TE, Technical Elective, Type: E, T: 3, P: 0, C: 3, ECTS: 5
TE, Technical Elective, Type: E, T: 3, P: 0, C: 3, ECTS: 5
TE, Technical Elective, Type: E, T: 3, P: 0, C: 3, ECTS: 5

Total: T: 17, P: 0, C: 17, ECTS: 30""",

        # 8th Semester
        """Fourth Year - Second Semester Courses (Year Four or 4 Second Semester - Final Year Second Semester):
AII429, Engineering Ethics, Type: E, T: 3, P: 0, C: 3, ECTS: 6
AII426, Economics for Engineers, Type: E, T: 3, P: 0, C: 3, ECTS: 6
SWE492, Graduation Project II, Type: C, T: 4, P: 0, C: 4, ECTS: 7
SWE401, Software Project Management, Type: E, T: 2, P: 0, C: 3, ECTS: 6
TE, Technical Elective, Type: E, T: 3, P: 0, C: 3, ECTS: 5

Total: T: 15, P: 0, C: 16, ECTS: 30""",

        # Technical Elective Courses
        """Technical Elective Courses (TE) - Selected Highlights:
AII431, E-Commerce, T: 2, P: 2, C: 3, ECTS: 5
AII412, Database Application, T: 2, P: 2, C: 3, ECTS: 5
AII405, Computer Hardware, T: 2, P: 2, C: 3, ECTS: 5
AII409, Object Oriented Programming II, T: 2, P: 2, C: 3, ECTS: 5
AII417, Mobile Programming, T: 2, P: 2, C: 3, ECTS: 5

Additional Technical Electives:
System Simulation, Neural Networks, Image Processing, Computer Graphics, System Programming, 
Artificial Intelligence, Advanced Object Oriented Programming, Programming Languages II,
Large Scale Software Development, Software Patterns, Distributed Software Patterns,
Real-Time Embedded Systems, Formal Methods in Software Engineering, 
Analysis and Design of User Interfaces, Rapid Application Development, Decision Making""",

        # Program Summary
        """Program Summary:
Total Courses: 52
Total Electives: 13
Total Credits: 145
Total ECTS: 240
Percentage of Electives: 23%

Course Type Legend:
C = Compulsory Course
E = Elective Course
T = Theoretical Study Hours
P = Practice/Lab Hours
C = Credits
ECTS = European Credit Transfer and Accumulation System""",

        # Course Descriptions - Core Programming Courses
        """Course Descriptions - Core Programming Courses:

AII102, Programming and Problem Solving (T: 3, P: 2, C: 4, ECTS: 5)
Course objective: This course provides an introduction to fundamental concepts of programming and use of built-in data structures in solving problems using programming languages.
Course Content: Students study how to write user-defined functions using iteration as well as recursion. This course also stresses the importance of programming tools such as programming editors and debuggers.

AII108, Object Oriented Programming (T: 2, P: 2, C: 3, ECTS: 6)
Course objective: This course provides an in-depth discussion of object-oriented programming and how object oriented programming can be used in solving real-life problems.
Course Content: This course requires a more advanced use of programming tools. The course builds upon the knowledge of programming fundamentals.

AII201, Data Structures and Algorithms (T: 3, P: 2, C: 4, ECTS: 6)
Course objective: This course comprises an introductory exploration into the design and implementation of Abstract Data Types (ADTs) along with the study of algorithm design and complexity analysis.
Course Content: Implementation of data structures using object-oriented programming.""",

        # Course Descriptions - Software Engineering Core
        """Course Descriptions - Software Engineering Core Courses:

AII003, Principles of Software Engineering (T: 3, P: 0, C: 3, ECTS: 6)
Course objective: The aim of the course is to prepare students to real life application of software engineering.
Course Content: Introduction to Software Engineering, Modeling, Project Organization and Communication, Requirements Elicitation, Analysis, System Design, Object Design, Testing, Configuration Management, Project Management, Software Life Cycle.

SWE202, Software Construction (T: 2, P: 2, C: 3, ECTS: 4)
Course objective: This course aims to engage students with concepts related to the construction of software systems at scale.
Course content: General principles and techniques for disciplined low-level software design. BNF and basic theory of grammars and parsing. Use of parser generators.

SWE301, Software Design and Architecture (T: 3, P: 2, C: 4, ECTS: 5)
Course objective: The main aim of this course is to familiarize with concepts and methods of software design and architecture.
Course content: An in-depth look at software design. Continuation of the study of design patterns, frameworks, and architectures.""",

        # Mission and Vision
        """Mission and Vision:

Mission
The mission of the department of Software Engineering of the Near East University is to educate engineers that meet the needs of society within world standards and pursue scientific cooperation with national and international entities in academia, public and private sectors.

Vision
The vision of department is to be recognized as one of the leading institutions with Software Engineering programs, imparting the highest quality education to students and become a national and international center of research excellence in Software Engineering.""",

        # Career Opportunities
        """Career Opportunities for Software Engineering Graduates:
Software Engineer
Software Developer
Systems Analyst
Application Programmer
Database Administrator
Network Designer
Security Administrator
System Evaluator
System Programmer
System Designer
Quality Assurance Engineer
Project Manager
IT Consultant"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "department": "Software Engineering",
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
            "course_type": "core",
            "document_type": "course_description",
            "content_type": "programming_courses"
        },
        {
            "course_type": "core",
            "document_type": "course_description",
            "content_type": "software_engineering_courses"
        },
        {
            "document_type": "program_info",
            "content_type": "mission_vision"
        },
        {
            "document_type": "program_info",
            "content_type": "career_opportunities"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"se_curriculum_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Software Engineering curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["software engineering courses ECTS"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_software_engineering_curriculum_to_chromadb()