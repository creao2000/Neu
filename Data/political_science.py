




# import chromadb

# # Initialize ChromaDB client
# chroma_client = chromadb.PersistentClient(path="./chroma_db")

# # List all collections first to confirm
# collections = chroma_client.list_collections()
# print("Current collections:", [col.name for col in collections])

# # Delete the specific collection
# try:
#     chroma_client.delete_collection(name="neu_political_science")
#     print("✅ Collection 'neu_political_science' deleted successfully!")
# except Exception as e:
#     print(f"❌ Error deleting collection: {e}")

# # Verify it's gone
# collections = chroma_client.list_collections()
# print("Remaining collections:", [col.name for col in collections])







import chromadb
from chromadb.utils import embedding_functions

def add_political_science_curriculum_to_chromadb():
    """Add Political Science curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_political_science",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_political_science",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_political_science")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF ECONOMICS AND ADMINISTRATIVE SCIENCES
DEPARTMENT OF POLITICAL SCIENCE
Bachelor of POLITICAL SCIENCE

Program Duration: 4 years (8 semesters)
Degree: Bachelor of POLITICAL SCIENCE
Total ECTS for Graduation: 240

Main website: https://iktisat.neu.edu.tr/?lang=en
Curriculum link: https://iktisat.neu.edu.tr/academic/academic-programmes/department-of-political-science/courses/?lang=en

Legend:
C = Compulsory Course
E = Elective Course
T = Theoretical Hours
ECTS = European Credit Transfer System""",

        # 1st Year - 1st Semester
        """First Year - First Semester - Compulsory Courses:
ENG101, English I, C, Credit:3, ECTS:4, Hours:3
SOC100, Sociology, C, Credit:3, ECTS:6, Hours:3
EAS110, Political Science I, C, Credit:3, ECTS:6, Hours:3
EAS101, Principles of Economics I, C, Credit:3, ECTS:6, Hours:3
EAS105, History of Civilizations, C, Credit:3, ECTS:6, Hours:3
YIT101/TUR101, Turkish for International Students I/Turkish Language I, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:30, Hours:17""",

        # 1st Year - 2nd Semester
        """First Year - Second Semester - Compulsory Courses:
ENG102, English II, C, Credit:3, ECTS:4, Hours:3
EAS112, Political Science II, C, Credit:3, ECTS:6, Hours:3
EAS111, History of Political Thought, C, Credit:3, ECTS:6, Hours:3
EAS102, Principles of Economics II, C, Credit:3, ECTS:6, Hours:3
EAS206, Introduction to Law, C, Credit:3, ECTS:6, Hours:3
YIT102/TUR102, Turkish for International Students II/Turkish Language II, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:30, Hours:17""",

        # 2nd Year - 1st Semester
        """Second Year - First Semester - Compulsory Courses:
EAS215, Academic Communication, C, Credit:3, ECTS:4, Hours:3
PUB201, Public Administration, C, Credit:3, ECTS:6, Hours:3
LAW205, Constitutional Law, C, Credit:3, ECTS:6, Hours:3
POL210, Modern Political Thought, C, Credit:3, ECTS:6, Hours:3
IR207, Introduction to International Relations I, C, Credit:3, ECTS:6, Hours:3
AİT101/103, Atatürk's Principles I/Principles of Atatürk I, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:30, Hours:17""",

        # 2nd Year - 2nd Semester
        """Second Year - Second Semester - Compulsory Courses:
EAS216, Academic Writing, C, Credit:3, ECTS:4, Hours:3
HIST205, World History of the 20th Century, C, Credit:3, ECTS:6, Hours:3
POL205, Political Psychology, C, Credit:3, ECTS:6, Hours:3
EAS208, Research Methods, C, Credit:3, ECTS:6, Hours:3
IR208, Introduction to International Relations II, C, Credit:3, ECTS:6, Hours:3
AİT102/104, Atatürk's Principles II/Principles of Atatürk II, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:30, Hours:17""",

        # 3rd Year - 1st Semester
        """Third Year - First Semester - Compulsory Courses:
POL303, Public Policy, C, Credit:3, ECTS:6, Hours:3
ECON305, History of Economic Thought, C, Credit:3, ECTS:6, Hours:3
IR313, International Politics & Security, C, Credit:3, ECTS:6, Hours:3
POL312, Comparative Political Systems, C, Credit:3, ECTS:6, Hours:3
HIST308, Ottoman Economic, Social & Political Structure I, C, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 3rd Year - 2nd Semester
        """Third Year - Second Semester - Compulsory Courses:
IR312, International Institutions & Organization, C, Credit:3, ECTS:6, Hours:3
IR311, Turkish Foreign Policy I, C, Credit:3, ECTS:6, Hours:3
ECON307, Public Finance, C, Credit:3, ECTS:6, Hours:3
POL306, Modern Turkish Politics, C, Credit:3, ECTS:6, Hours:3
HIST309, Ottoman Economic, Social & Political Structure II, C, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 4th Year - 1st Semester
        """Fourth Year - First Semester - Elective Courses:
Elective Course, Political Science Elective, E, Credit:3, ECTS:6, Hours:3
Elective Course, Political Science Elective, E, Credit:3, ECTS:6, Hours:3
Elective Course, Political Science Elective, E, Credit:3, ECTS:6, Hours:3
Elective Course, Political Science Elective, E, Credit:3, ECTS:6, Hours:3
Elective Course, Political Science Elective, E, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 4th Year - 2nd Semester
        """Fourth Year - Second Semester - Elective Courses:
Elective Course, Political Science Elective, E, Credit:3, ECTS:6, Hours:3
Elective Course, Political Science Elective, E, Credit:3, ECTS:6, Hours:3
Elective Course, Political Science Elective, E, Credit:3, ECTS:6, Hours:3
Elective Course, Political Science Elective, E, Credit:3, ECTS:6, Hours:3
Elective Course, Political Science Elective, E, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # Elective Courses
        """Elective Course Options for Political Science:

Political Theory and Philosophy Electives:
POL401, Contemporary Political Theory
POL402, Political Philosophy
POL403, Democratic Theory
POL404, Political Ideologies
POL405, Critical Theory
POL406, Feminist Political Theory
POL407, Post-Colonial Political Thought

Comparative Politics Electives:
POL408, European Politics
POL409, Middle Eastern Politics
POL410, Asian Political Systems
POL411, Latin American Politics
POL412, African Politics
POL413, Comparative Democratization
POL414, Political Parties and Elections

International Relations Electives:
IR401, International Political Economy
IR402, Foreign Policy Analysis
IR403, Conflict Resolution and Peace Studies
IR404, International Security Studies
IR405, Global Governance
IR406, Human Rights in International Relations
IR407, Diplomacy and Negotiation

Turkish Politics and History Electives:
POL415, Turkish Political History
POL416, Political Economy of Turkey
POL417, Turkish-European Union Relations
POL418, Local Government in Turkey
POL419, Civil Society in Turkey
POL420, Turkish Constitutional Development
POL421, Politics of Modern Turkey

Public Policy and Administration Electives:
PUB401, Public Policy Analysis
PUB402, Administrative Law
PUB403, Urban Politics and Policy
PUB404, Environmental Policy
PUB405, Social Policy and Welfare State
PUB406, Health Policy
PUB407, Education Policy

Research and Methodology Electives:
POL422, Qualitative Research Methods
POL423, Political Data Analysis
POL424, Survey Research in Politics
POL425, Case Study Research
POL426, Political Ethnography
POL427, Advanced Research Design""",

        # Core Course Descriptions
        """Core Course Descriptions - Political Science Focus:

EAS110/112 - Political Science I & II:
Introduction to political concepts, theories, institutions, and behavior in comparative perspective.

EAS111 - History of Political Thought:
Evolution of political ideas from ancient to modern times, major political philosophers and their contributions.

PUB201 - Public Administration:
Structure and function of public bureaucracies, administrative theory, and public management.

LAW205 - Constitutional Law:
Principles of constitutional governance, separation of powers, judicial review, and constitutional rights.

POL210 - Modern Political Thought:
Development of political ideas in modern era, including liberalism, conservatism, socialism, and nationalism.

IR207/208 - Introduction to International Relations I & II:
Theories of international relations, state behavior, international organizations, and global governance.

EAS208 - Research Methods:
Research design, data collection, and analytical methods in political science research.

POL303 - Public Policy:
Policy process, policy analysis, implementation, and evaluation in various policy domains.

POL312 - Comparative Political Systems:
Analysis of different political systems, institutions, and processes across countries.

IR313 - International Politics & Security:
Security studies, conflict analysis, military strategy, and contemporary security challenges.

IR312 - International Institutions & Organization:
Structure and function of international organizations, global governance, and multilateral diplomacy.

IR311 - Turkish Foreign Policy I:
Historical development and contemporary issues in Turkish foreign policy.

POL306 - Modern Turkish Politics:
Political development, institutions, and current issues in Turkish politics.

HIST308/309 - Ottoman Economic, Social & Political Structure:
Historical analysis of Ottoman Empire's political, economic, and social structures.""",

        # Program Summary and Career Opportunities
        """Political Science Program Summary:
Degree: Bachelor of Arts in Political Science
Duration: 4 years (8 semesters)
Total ECTS: 240
Language of Instruction: English

Program Focus Areas:
- Political Theory and Philosophy
- Comparative Politics
- International Relations
- Public Administration and Policy
- Turkish Politics and History
- Research Methodology
- Constitutional Law and Governance

Core Competencies Developed:
- Critical thinking and analytical skills
- Political theory and philosophical analysis
- Comparative political analysis
- International relations theory
- Research design and methodology
- Policy analysis and evaluation
- Academic writing and communication
- Historical and contextual understanding

Career Opportunities:
Political Analyst
Policy Analyst
Diplomatic Service Officer
International Organization Staff
Government Affairs Specialist
Political Consultant
Intelligence Analyst
Public Administration Officer
Non-Profit Program Manager
Journalist/Political Reporter
Academic Researcher
Legislative Assistant
Foreign Service Officer
Political Campaign Manager

Professional Settings:
Government Ministries and Agencies
Diplomatic Missions and Embassies
International Organizations (UN, EU, NATO)
Political Parties and Campaigns
Think Tanks and Research Institutes
Non-Governmental Organizations
Media and Journalism Outlets
Public Administration Departments
Academic and Educational Institutions
Corporate Government Relations
Intelligence and Security Agencies
Public Policy Consulting Firms""",

        # Program Structure and Specializations
        """Program Structure and Specialization Tracks:

Foundation Year (1st Year):
- Basic political science concepts and theories
- Historical and philosophical foundations
- Economics and sociology context
- Language and communication skills

Core Development (2nd Year):
- Public administration and constitutional law
- International relations theory
- Modern political thought
- Research methods and academic writing
- 20th century world history

Advanced Specialization (3rd Year):
- Comparative political systems
- Public policy and finance
- International security and institutions
- Turkish foreign policy and politics
- Ottoman and Turkish historical context

Professional Preparation (4th Year):
- Extensive elective course selection
- Specialization in chosen subfields
- Advanced research and analysis
- Professional skill development

Specialization Tracks through Electives:
1. Political Theory and Philosophy: Contemporary theory, political philosophy, ideologies
2. Comparative Politics: Regional studies, political systems, democratization
3. International Relations: Foreign policy, security studies, global governance
4. Turkish Politics and History: Turkish political development, EU relations, local governance
5. Public Policy and Administration: Policy analysis, public management, administrative law

Unique Program Features:
- Strong foundation in both Turkish and international politics
- Integration of historical and contemporary perspectives
- Emphasis on research methodology and analytical skills
- Preparation for diverse careers in public service and international affairs
- English language instruction with global perspective"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Economics and Administrative Sciences",
            "department": "Political Science",
            "degree": "Bachelor of Arts",
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
            "content_type": "political_science_electives"
        },
        {
            "course_type": "core",
            "document_type": "course_description",
            "content_type": "political_science_core_courses"
        },
        {
            "document_type": "program_info",
            "content_type": "program_summary_careers"
        },
        {
            "document_type": "program_info",
            "content_type": "program_structure"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"ps_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Political Science curriculum documents to ChromaDB!")
        print("✅ Degree correctly set as: Bachelor of Arts in Political Science")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["political theory international relations public policy"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_political_science_curriculum_to_chromadb()