import chromadb
from chromadb.utils import embedding_functions

def add_cyber_security_engineering_curriculum_to_chromadb():
    """Add Cyber Security Engineering curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_cyber_security_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_cyber_security_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_cyber_security_engineering")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """Department of Cyber Security Engineering
Bachelor of Cyber Security Engineering Curriculum Overview
Main website link: https://aif.neu.edu.tr/
Curriculum link: https://aif.neu.edu.tr/academic/academic-programmes/department-of-cyber-security-engineering/

T (Theory Hours): The number of hours dedicated to lectures or theoretical learning in the course.
P (Practice Hours): The number of hours spent on practical work, labs, or hands-on activities.
C (Credits): The credit value assigned to the course, reflecting its academic weight.
E (ECTS): European Credit Transfer and Accumulation System, representing the workload and learning outcomes.

Course Type Legend:
C = Compulsory Course
E = Elective Course""",

        # 1st Semester
        """First Year - First Semester Courses (Year One or 1 First Semester):
MTH113, LINEAR ALGEBRA, T: 3, P: 0, C: 3, E: 5
AII102, PROGRAMMING AND PROBLEM SOLVING, T: 3, P: 2, C: 4, E: 5
ENG101, ENGLISH I, T: 3, P: 0, C: 3, E: 3
MTH101, CALCULUS I, T: 4, P: 0, C: 4, E: 5
PHY101, GENERAL PHYSICS I, T: 3, P: 2, C: 4, E: 5
CAM100, CAMPUS ORIENTATION, T: 2, P: 0, C: 0, E: 2
CHM101, GENERAL CHEMISTRY I, T: 3, P: 2, C: 4, E: 5

Total: T: 21, P: 6, C: 22, E: 30""",

        # 2nd Semester
        """First Year - Second Semester Courses (Year One or 1 Second Semester):
AII104, DISCRETE STRUCTURES, T: 3, P: 0, C: 3, E: 6
ENG102, ENGLISH II, T: 3, P: 0, C: 3, E: 3
MTH102, CALCULUS II, T: 4, P: 0, C: 4, E: 6
PHY102, GENERAL PHYSICS II, T: 3, P: 2, C: 4, E: 6
AII108, OBJECT ORIENTED PROGRAMMING, T: 2, P: 2, C: 3, E: 5
GEC351, 21ST CENTURY SKILLS, T: 2, P: 0, C: 0, E: 2
CAR100, CAREER PLANNING, T: 2, P: 0, C: 0, E: 2

Total: T: 19, P: 4, C: 17, E: 30""",

        # 3rd Semester
        """Second Year - First Semester Courses (Year Two or 2 First Semester):
AII001, LOGIC DESIGN, T: 3, P: 2, C: 4, E: 6
AII201, DATA STRUCTURES & ALGORITHMS, T: 3, P: 2, C: 4, E: 6
CSE002, INTRODUCTION TO CYBER SECURITY ENGINEERING, T: 3, P: 0, C: 3, E: 3
MTH201, DIFFERENTIAL EQUATIONS, T: 4, P: 0, C: 4, E: 6
CSE003, INTRODUCTION TO ENGINEERING, T: 3, P: 0, C: 3, E: 5
AIT103, ATATÜRK PRINCIPLES AND REFORMS I, T: 2, P: 0, C: 2, E: 2
YIT101, TURKISH FOR FOREIGNERS I, T: 2, P: 0, C: 2, E: 2

Total: T: 20, P: 4, C: 22, E: 30""",

        # 4th Semester
        """Second Year - Second Semester Courses (Year Two or 2 Second Semester):
AII202, DATABASE MANAGEMENT SYSTEMS, T: 4, P: 0, C: 4, E: 5
CSE004, INTRODUCTION TO COMPUTATION AND PROGRAMMING, T: 2, P: 2, C: 3, E: 5
CSE005, CRYPTOGRAPHY FUNDAMENTALS, T: 4, P: 0, C: 3, E: 4
MTH251, PROBABILITY AND STATISTICS, T: 3, P: 0, C: 3, E: 6
AIT104, ATATÜRK PRINCIPLES AND REFORMS II, T: 2, P: 0, C: 0, E: 2
YIT102, TURKISH FOR FOREIGNERS II, T: 2, P: 0, C: 2, E: 2
CSE299, SUMMER TRAINING I, T: 0, P: 2, C: 0, E: 6

Total: T: 17, P: 4, C: 17, E: 30""",

        # 5th Semester
        """Third Year - First Semester Courses (Year Three or 3 First Semester):
CSE006, INTRODUCTION TO COMPUTING FOR DIGITAL SYSTEMS ENGINEERING, T: 3, P: 2, C: 3, E: 4
CSE007, RF SOFTWARE ENGINEERING, T: 4, P: 0, C: 4, E: 5
CSE008, DATA COMMUNICATION, T: 3, P: 0, C: 3, E: 5
AII302, OPERATING SYSTEMS, T: 4, P: 0, C: 3, E: 6
AII439, OCCUPATIONAL HEALTH AND SAFETY I, T: 2, P: 0, C: 2, E: 4
ENG201, ORAL COMMUNICATION SKILLS, T: 2, P: 0, C: 3, E: 4
CHC100, CYPRUS HISTORY AND CULTURE, T: 2, P: 0, C: 2, E: 2

Total: T: 20, P: 2, C: 20, E: 30""",

        # 6th Semester
        """Third Year - Second Semester Courses (Year Three or 3 Second Semester):
CSE009, COMPUTER NETWORKING, T: 3, P: 0, C: 3, E: 5
CSE010, SYSTEMS ENGINEERING, T: 3, P: 0, C: 3, E: 5
CSE011, POWER SYSTEMS AND SMART GRID SECURITY, T: 3, P: 0, C: 4, E: 6
CSE012, TRANSPORTATION SYSTEMS DESIGN, T: 3, P: 0, C: 4, E: 6
AII440, OCCUPATIONAL HEALTH AND SAFETY II, T: 3, P: 0, C: 3, E: 2
CSE399, SUMMER TRAINING II, T: 0, P: 2, C: 0, E: 6

Total: T: 15, P: 2, C: 17, E: 30""",

        # 7th Semester
        """Fourth Year - First Semester Courses (Year Four or 4 First Semester - Final Year First Semester):
CSE013, ENGINEERING SENIOR SEMINAR, T: 3, P: 2, C: 4, E: 5
CSE014, INDUSTRIAL CONTROL SYSTEMS SECURITY, T: 3, P: 0, C: 4, E: 5
CSE510, SENIOR ADVANCED DESIGN PROJECT I, T: 3, P: 0, C: 3, E: 5
CSE015, EMBEDDED AND REAL TIME SYSTEMS, T: 4, P: 2, C: 4, E: 5
TE, TECHNICAL ELECTIVE, T: 2, P: 2, C: 3, E: 5
TE, TECHNICAL ELECTIVE, T: 2, P: 2, C: 3, E: 5

Total: T: 17, P: 8, C: 21, E: 30""",

        # 8th Semester
        """Fourth Year - Second Semester Courses (Year Four or 4 Second Semester - Final Year Second Semester):
CSE511, SENIOR ADVANCED DESIGN PROJECT II, T: 3, P: 0, C: 3, E: 5
CSE016, HUMAN FACTORS AND CYBER SECURITY ENGINEERING, T: 3, P: 0, C: 3, E: 5
CSE017, SYSTEM SECURITY AND RESILIENCE SYSTEM, T: 3, P: 2, C: 4, E: 5
CSE018, MOBILE DEVICES AND NETWORK SECURITY, T: 4, P: 2, C: 4, E: 5
TE, TECHNICAL ELECTIVE, T: 3, P: 0, C: 3, E: 5
TE, TECHNICAL ELECTIVE, T: 3, P: 0, C: 3, E: 5

Total: T: 19, P: 4, C: 20, E: 30""",

        # Technical Elective Courses
        """Technical Elective Courses (TE) - Available Options:
CSE431, E-COMMERCE, T: 2, P: 2, C: 3, E: 5
AII404, NEURAL NETWORKS, T: 2, P: 2, C: 3, E: 5
AII419, IMAGE PROCESSING, T: 2, P: 2, C: 3, E: 5
CSE417, MOBILE PROGRAMMING, T: 2, P: 2, C: 3, E: 5
AII415, DECISION MAKING, T: 2, P: 2, C: 3, E: 5
CSE445, INTRODUCTION TO MACHINE LEARNING, T: 2, P: 2, C: 3, E: 5
CSE411, ADVANCED DATA ANALYSIS, T: 2, P: 2, C: 3, E: 5
CSE412, INFORMATION RETRIEVAL AND WEB SEARCH, T: 2, P: 2, C: 3, E: 5
CSE418, INTERNET PROGRAMMING, T: 2, P: 2, C: 3, E: 5
CSE428, E-GOVERNMENT, T: 2, P: 2, C: 3, E: 5
AII429, ENGINEERING ETHICS, T: 2, P: 2, C: 3, E: 5
CSE430, PRINCIPLES OF INFORMATION SECURITY, T: 2, P: 2, C: 3, E: 5
AII426, ECONOMICS FOR ENGINEERS, T: 2, P: 2, C: 3, E: 5""",

        # Program Summary
        """Cyber Security Engineering Program Summary:
- Department: Cyber Security Engineering
- Degree: Bachelor of Science
- Total Semesters: 8
- Total Courses: 50
- Total Electives: 14
- Total Credits: 152
- Total ECTS Credits: 240
- Elective Percentage: 26%
- Language of Instruction: English

Key Specializations:
- Network Security and Cryptography
- Industrial Control Systems Security
- Embedded Systems Security
- Mobile and Wireless Security
- Smart Grid and Critical Infrastructure Protection
- Digital Forensics and Incident Response""",

        # Core Cyber Security Courses Description
        """Core Cyber Security Engineering Courses:

CSE002, INTRODUCTION TO CYBER SECURITY ENGINEERING (T: 3, P: 0, C: 3, E: 3)
Fundamental concepts of cyber security engineering, security principles, threat landscape, and basic security controls.

CSE005, CRYPTOGRAPHY FUNDAMENTALS (T: 4, P: 0, C: 3, E: 4)
Principles of cryptography, encryption algorithms, digital signatures, cryptographic protocols, and key management.

CSE009, COMPUTER NETWORKING (T: 3, P: 0, C: 3, E: 5)
Network architectures, protocols, network security mechanisms, and secure network design principles.

CSE011, POWER SYSTEMS AND SMART GRID SECURITY (T: 3, P: 0, C: 4, E: 6)
Security of critical infrastructure, smart grid systems, SCADA security, and industrial control system protection.

CSE014, INDUSTRIAL CONTROL SYSTEMS SECURITY (T: 3, P: 0, C: 4, E: 5)
Security of industrial automation systems, PLC security, and protection of critical manufacturing systems.

CSE017, SYSTEM SECURITY AND RESILIENCE SYSTEM (T: 3, P: 2, C: 4, E: 5)
System hardening, security monitoring, incident response, and building resilient security architectures.

CSE018, MOBILE DEVICES AND NETWORK SECURITY (T: 4, P: 2, C: 4, E: 5)
Mobile platform security, wireless network security, and protection of mobile applications and devices.""",

        # Career Opportunities
        """Career Opportunities for Cyber Security Engineering Graduates:
Cyber Security Engineer
Network Security Specialist
Security Analyst
Information Security Officer
Cryptography Specialist
Industrial Control Systems Security Engineer
Security Architect
Digital Forensics Investigator
Incident Response Specialist
Security Consultant
Vulnerability Analyst
Penetration Tester
Security Operations Center (SOC) Analyst
Cyber Security Researcher""",

        # Program Focus Areas
        """Program Focus Areas and Specializations:

1. Network and Infrastructure Security
   - Secure network design and implementation
   - Firewall and intrusion detection systems
   - Wireless and mobile network security

2. Cryptography and Data Protection
   - Encryption algorithms and protocols
   - Digital signatures and authentication
   - Key management systems

3. Industrial and Critical Infrastructure Security
   - SCADA and ICS security
   - Smart grid protection
   - Transportation systems security

4. Embedded and Real-Time Systems Security
   - IoT device security
   - Embedded system protection
   - Real-time operating system security

5. Security Operations and Incident Response
   - Security monitoring and analysis
   - Digital forensics
   - Incident handling and response"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "department": "Cyber Security Engineering",
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
            "content_type": "cyber_security_core_courses"
        },
        {
            "document_type": "program_info",
            "content_type": "career_opportunities"
        },
        {
            "document_type": "program_info",
            "content_type": "focus_areas"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"cse_curriculum_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Cyber Security Engineering curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["cyber security cryptography network security"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_cyber_security_engineering_curriculum_to_chromadb()