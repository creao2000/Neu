import chromadb
from chromadb.utils import embedding_functions

def add_data_analytics_engineering_curriculum_to_chromadb():
    """Add Data Analytics Engineering curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_data_analytics_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_data_analytics_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_data_analytics_engineering")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """Department of Data Analytics Engineering
Bachelor of Data Analytics Engineering Curriculum Overview
Main website link: https://aif.neu.edu.tr/

T (Theory Hours): The number of hours dedicated to lectures or theoretical learning in the course.
U (Practice Hours): The number of hours spent on practical work, labs, or hands-on activities.
C (Credits): The credit value assigned to the course, reflecting its academic weight.
E (ECTS): European Credit Transfer and Accumulation System, representing the workload and learning outcomes.

Course Type Legend:
C = Compulsory Course
E = Elective Course""",

        # 1st Semester
        """First Year - First Semester Courses (Year One or 1 First Semester):
MTH113, LINEAR ALGEBRA, T: 3, U: 0, C: 3, E: 5
AII102, PROGRAMMING AND PROBLEM SOLVING, T: 3, U: 2, C: 4, E: 5
ENG101, ENGLISH I, T: 2, U: 0, C: 2, E: 5
MTH101, CALCULUS I, T: 4, U: 0, C: 4, E: 5
PHY101, GENERAL PHYSICS I, T: 2, U: 2, C: 4, E: 5
CAM100, CAMPUS ORIENTATION, T: 0, U: 0, C: 0, E: 5
CHM101, GENERAL CHEMISTRY I, T: 2, U: 2, C: 4, E: 5

Total: T: 21, U: 6, C: 19, E: 30""",

        # 2nd Semester
        """First Year - Second Semester Courses (Year One or 1 Second Semester):
AII104, DISCRETE STRUCTURES, T: 3, U: 0, C: 3, E: 5
ENG102, ENGLISH II, T: 2, U: 0, C: 2, E: 3
MTH102, CALCULUS II, T: 4, U: 0, C: 4, E: 6
PHY102, GENERAL PHYSICS II, T: 2, U: 2, C: 4, E: 6
AII108, OBJECT ORIENTED PROGRAMMING, T: 2, U: 2, C: 3, E: 6
YIT101, TURKISH FOR FOREIGNERS I, T: 2, U: 0, C: 2, E: 2
GEC351, 21st CENTURY SKILLS, T: 0, U: 0, C: 0, E: 2

Total: T: 19, U: 4, C: 18, E: 30""",

        # 3rd Semester
        """Second Year - First Semester Courses (Year Two or 2 First Semester):
DAE001, ADVANCED ALGEBRA AND CALCULUS, T: 2, U: 2, C: 4, E: 6
AII201, DATA STRUCTURES & ALGORITHMS, T: 2, U: 2, C: 4, E: 6
DAE003, INFORMATION THEORY, T: 0, U: 4, C: 4, E: 4
MTH201, DIFFERENTIAL EQUATIONS, T: 0, U: 4, C: 4, E: 6
DAE002, INTRODUCTION TO AUDIOVISUAL PROCESSING, T: 0, U: 3, C: 3, E: 4
AIT103, ATATÜRK PRINCIPLES AND REFORMS I, T: 0, U: 2, C: 2, E: 2
YIT102, TURKISH FOR FOREIGNERS II, T: 0, U: 2, C: 2, E: 2

Total: T: 20, U: 4, C: 23, E: 30""",

        # 4th Semester
        """Second Year - Second Semester Courses (Year Two or 2 Second Semester):
AII202, DATABASE MANAGEMENT SYSTEMS, T: 4, U: 0, C: 4, E: 5
DAE004, DATA ENGINEERING THEORY, T: 2, U: 2, C: 3, E: 5
DAE005, SIGNALS AND SYSTEMS, T: 0, U: 4, C: 4, E: 4
MTH251, PROBABILITY AND STATISTICS, T: 0, U: 3, C: 3, E: 6
AIT104, ATATÜRK PRINCIPLES AND REFORMS II, T: 0, U: 2, C: 2, E: 2
AIE299, SUMMER TRAINING I, T: 2, U: 0, C: 0, E: 6
CHC100, CYPRUS HISTORY AND CULTURE, T: 0, U: 0, C: 0, E: 2

Total: T: 18, U: 4, C: 16, E: 30""",

        # 5th Semester
        """Third Year - First Semester Courses (Year Three or 3 First Semester):
DAE007, PROBABILITY AND STATISTICS 2, T: 3, U: 0, C: 3, E: 5
DAE006, MACHINE LEARNING FOR SATELLITE IMAGERY, T: 2, U: 2, C: 3, E: 5
ENG201, ORAL COMMUNICATION SKILLS, T: 3, U: 0, C: 3, E: 4
DAE008, PRESCRIPTIVE ANALYTICS I, T: 3, U: 0, C: 3, E: 5
AII439, OCCUPATIONAL HEALTH AND SAFETY I, T: 2, U: 0, C: 2, E: 4
DAE009, SYSTEMS ENGINEERING, T: 3, U: 0, C: 3, E: 5
CAR100, CAREER PLANNING, T: 2, U: 0, C: 0, E: 2

Total: T: 18, U: 2, C: 17, E: 30""",

        # 6th Semester
        """Third Year - Second Semester Courses (Year Three or 3 Second Semester):
DAE011, MACHINE LEARNING 1, T: 3, U: 0, C: 4, E: 5
DAE012, MATHEMATICAL OPTIMIZATION, T: 3, U: 2, C: 4, E: 5
DAE013, PARALLELISM AND DISTRIBUTED SYSTEMS, T: 3, U: 0, C: 4, E: 5
DAE014, ADVANCED DATABASES, T: 4, U: 2, C: 4, E: 5
AIE399, SUMMER TRAINING II, T: 0, U: 0, C: 0, E: 5
DAE010, PRESCRIPTIVE ANALYTICS II, T: 3, U: 0, C: 4, E: 5

Total: T: 16, U: 4, C: 20, E: 30""",

        # 7th Semester
        """Fourth Year - First Semester Courses (Year Four or 4 First Semester - Final Year First Semester):
DAE015, MACHINE LEARNING 2, T: 3, U: 0, C: 3, E: 5
DAE016, ENTREPRENEURSHIP AND INNOVATION, T: 3, U: 0, C: 3, E: 4
DAE018, SENIOR ADVANCED DESIGN PROJECT I, T: 4, U: 2, C: 4, E: 6
TE, TECHNICAL ELECTIVE, T: 3, U: 0, C: 3, E: 5
TE, TECHNICAL ELECTIVE, T: 3, U: 0, C: 3, E: 5
DAE017, INFORMATION RETRIEVAL AND ANALYSIS, T: 3, U: 2, C: 4, E: 5

Total: T: 19, U: 4, C: 20, E: 30""",

        # 8th Semester
        """Fourth Year - Second Semester Courses (Year Four or 4 Second Semester - Final Year Second Semester):
AII429, ENGINEERING ETHICS, T: 3, U: 0, C: 3, E: 5
DAE019, SENIOR ADVANCED DESIGN PROJECT II, T: 3, U: 0, C: 3, E: 5
DAE020, INFORMATION VISUALIZATION, T: 3, U: 0, C: 3, E: 4
TE, TECHNICAL ELECTIVE, T: 3, U: 0, C: 3, E: 5
TE, TECHNICAL ELECTIVE, T: 3, U: 0, C: 3, E: 5
DAE021, IMAGE PROCESSING AND MACHINE VISION, T: 3, U: 0, C: 3, E: 4
AII440, OCCUPATIONAL HEALTH AND SAFETY II, T: 2, U: 0, C: 3, E: 2

Total: T: 18, U: 0, C: 21, E: 30""",

        # Elective Courses
        """Technical Elective Courses (TE) - Available Options:
AII419, IMAGE PROCESSING, T: 2, U: 2, C: 3, E: 5
AII415, DECISION MAKING, T: 2, U: 2, C: 3, E: 5
AIE411, ADVANCED DATA ANALYSIS, T: 2, U: 2, C: 3, E: 5
AIE412, INFORMATION RETRIEVAL AND WEB SEARCH, T: 2, U: 2, C: 3, E: 5
AIE413, HUMAN-ROBOT INTERACTION, T: 2, U: 2, C: 3, E: 5
AIE414, DEEP REINFORCEMENT LEARNING AND CONTROL, T: 2, U: 2, C: 3, E: 5
AIE415, MOBILE ROBOT PROGRAMMING, T: 2, U: 2, C: 3, E: 5
AIE416, AUTONOMOUS AGENTS, T: 2, U: 2, C: 3, E: 5
AIE417, INTRODUCTION TO QUANTUM COMPUTING, T: 2, U: 2, C: 3, E: 5
AIE418, COMPUTER ANIMATION & VISUALIZATION, T: 2, U: 2, C: 3, E: 5
AIE419, ALGORITHMIC GAME THEORY AND ITS APPLICATIONS, T: 2, U: 2, C: 3, E: 5
AIE420, FUZZY SYSTEMS, T: 2, U: 2, C: 3, E: 5
AIE458, AI AND INTERNET OF THINGS, T: 2, U: 2, C: 3, E: 5
AIE457, AI AND CLOUD COMPUTING, T: 2, U: 2, C: 3, E: 5
DAE022, BIG DATA SYSTEMS, T: 2, U: 2, C: 3, E: 5
DAE023, DATA SECURITY AND PRIVACY FOR ANALYTICS, T: 2, U: 2, C: 3, E: 5
DAE024, BUSINESS ANALYTICS, T: 2, U: 2, C: 3, E: 5
DAE025, HEALTH INFORMATICS, T: 2, U: 2, C: 3, E: 5""",

        # Admission Requirements
        """Specific Admission Requirements:
In the framework of the regulations set by Higher Education Council of Turkey (YÖK), student admission for this undergraduate program is made through a university entrance examination called YKS. Following the submission of students' academic program preferences, Student Selection and Placement Center (ÖSYM) places the students to the relevant program according to the score they get from ÖSYS.

International students are accepted to this undergraduate program according to the score of one of the international exams they take such as SAT, ACT and so on, or according to their high school diploma score.

Exchange student admission is made according to the requirements determined by bilateral agreements signed by NEU and the partner university.

Visiting students can enroll for the courses offered in this program upon the confirmation of the related academic unit. Additionally, they need to prove their English language level since the medium of instruction of the program is English.""",

        # Program Outcomes
        """Program Outcomes:
1. To have adequate knowledge in Mathematics, Science and Artificial Intelligence Engineering; to be able to use theoretical and applied information in these areas on complex engineering problems.
2. Gains the ability to understand the basic algorithms of artificial intelligence-based systems and understand the basic concepts of artificial intelligence-based systems.
3. Gain knowledge of problem solving and planning.
4. To be able to design artificial intelligence based systems.
5. To be able to devise, select, and use modern techniques and tools needed for analysis and solution of complex problems in Artificial Intelligence Engineering applications; to be able to use information technologies effectively.
6. Intelligent agents, search methods in problem solving, informed and uninformed search methods, exploration methods, constraint supply problems, game playing, knowledge and reasoning, primary logic, knowledge representation, learning.
7. To be able to solve real life problems involving large and complex data sets using mathematical computational and artificial intelligence techniques.
8. To have knowledge about global and social impact of Artificial Intelligence Engineering practices on health, environment, and safety; to have knowledge about contemporary issues as they pertain to engineering; to be aware of the legal ramifications of Artificial Intelligence Engineering solutions.
9. To be aware of ethical behaviour, professional and ethical responsibility; to have knowledge about standards utilized in engineering applications.
10. To be able to represent information using different techniques.
11. To be able to the appropriate scanning technique to achieve the desired goals.
12. To be able to collect data in the area of Artificial Intelligence Engineering, and to be able to communicate with colleagues in a foreign language. ("European Language Portfolio Global Scale", Level B1).
13. To be able to communicate effectively in Turkish, both orally and in writing; to be able to author and comprehend written reports, to be able to prepare design and implementation reports, to present effectively, to be able to give and receive clear and comprehensible instructions.""",

        # Graduation Requirements
        """Graduation Requirements:
In order to graduate from this undergraduate program, the students are required:

1. to succeed in all of the courses listed in the curriculum of the program by getting the grade of at least DD/S with a minimum of 251 ECTS
2. to have a Cumulative Grade Point Average (CGPA) of 2.00 out of 4.00
3. to complete their compulsory internship in a specified duration and quality.

Total ECTS Required: 251
Minimum CGPA: 2.00/4.00""",

        # Program Summary
        """Data Analytics Engineering Program Summary:
- Department: Data Analytics Engineering
- Degree: Bachelor of Science
- Total Semesters: 8
- Total Courses: 53+
- Total ECTS Credits: 251
- Language of Instruction: English
- Focus Areas: Machine Learning, Data Engineering, Statistical Analysis, Big Data Systems, Artificial Intelligence

Key Specializations:
- Machine Learning and AI
- Data Engineering and Database Systems
- Statistical Analysis and Optimization
- Big Data and Distributed Systems
- Data Visualization and Business Intelligence""",

        # Career Opportunities
        """Career Opportunities for Data Analytics Engineering Graduates:
Data Analyst
Data Scientist
Machine Learning Engineer
Data Engineer
Business Intelligence Analyst
Data Analytics Consultant
Big Data Engineer
Data Visualization Specialist
Quantitative Analyst
AI/ML Specialist
Database Administrator
Research Scientist
Business Analyst
Data Product Manager"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "department": "Data Analytics Engineering",
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
            "content_type": "admission_requirements"
        },
        {
            "document_type": "program_info",
            "content_type": "program_outcomes"
        },
        {
            "document_type": "program_info",
            "content_type": "graduation_requirements"
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
    ids = [f"dae_curriculum_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Data Analytics Engineering curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["machine learning data analytics courses"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_data_analytics_engineering_curriculum_to_chromadb()