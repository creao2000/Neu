import chromadb
from chromadb.utils import embedding_functions

def add_eu_relations_curriculum_to_chromadb():
    """Add European Union Relations curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_eu_relations",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_eu_relations",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_eu_relations")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF ECONOMICS AND ADMINISTRATIVE SCIENCES
DEPARTMENT OF EUROPEAN UNION RELATIONS
Bachelor of Arts in European Union Relations

Program Duration: 4 years (8 semesters)
Degree: Bachelor of Arts
Total ECTS for Graduation: 240

Main website: https://iktisat.neu.edu.tr/?lang=en
Curriculum link: https://iktisat.neu.edu.tr/academic/academic-programmes/department-of-european-union-relations/courses/?lang=en

Legend:
C = Compulsory Course
E = Elective Course
T = Theoretical Hours
ECTS = European Credit Transfer System""",

        # 1st Year - 1st Semester
        """First Year - First Semester - Compulsory Courses:
ENG101, English I, C, Credit:3, ECTS:4, Hours:3
COM101, Introduction to Computers, C, Credit:3, ECTS:6, Hours:3
MTH171, Mathematics for Business & Economics I, C, Credit:3, ECTS:6, Hours:3
EAS101, Principles of Economics I, C, Credit:3, ECTS:6, Hours:3
EAS103, Introduction to Business, C, Credit:3, ECTS:6, Hours:3
YIT101/TUR101, Turkish for International Students I/Turkish Language I, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:30, Hours:17""",

        # 1st Year - 2nd Semester
        """First Year - Second Semester - Compulsory Courses:
ENG102, English II, C, Credit:3, ECTS:4, Hours:3
EU100, Introduction to European Integration, C, Credit:3, ECTS:6, Hours:3
MTH172, Mathematics for Business & Economics II, C, Credit:3, ECTS:6, Hours:3
EAS102, Principles of Economics II, C, Credit:3, ECTS:6, Hours:3
EAS104, Principles of Management, C, Credit:3, ECTS:6, Hours:3
YIT102/TUR102, Turkish for International Students II/Turkish Language II, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:30, Hours:17""",

        # 2nd Year - 1st Semester
        """Second Year - First Semester - Compulsory Courses:
MAN201, Communication for Business I, C, Credit:3, ECTS:6, Hours:3
EAS105, History of Civilization, C, Credit:3, ECTS:6, Hours:3
EU201, EU Competition Policy, C, Credit:3, ECTS:6, Hours:3
EAS201, Microeconomics, C, Credit:3, ECTS:6, Hours:3
EAS110, Political Science I, C, Credit:3, ECTS:6, Hours:3
AİT101/103, Atatürk's Principles I/Principles of Atatürk I, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:32, Hours:17""",

        # 2nd Year - 2nd Semester
        """Second Year - Second Semester - Compulsory Courses:
MAN202, Communication for Business II, C, Credit:3, ECTS:6, Hours:3
EAS112, Political Sciences II, C, Credit:3, ECTS:6, Hours:3
MTH261, Statistics I, C, Credit:3, ECTS:6, Hours:3
EAS202, Macroeconomics, C, Credit:3, ECTS:6, Hours:3
EU208, Theories of EU Integration, C, Credit:3, ECTS:6, Hours:3
AİT102/104, Atatürk's Principles II/Principles of Atatürk II, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:32, Hours:17""",

        # 3rd Year - 1st Semester
        """Third Year - First Semester - Compulsory Courses:
EU301, History of Europe, C, Credit:3, ECTS:6, Hours:3
EAS205, Constitutional Law, C, Credit:3, ECTS:6, Hours:3
IR207, Introduction to International Relations I, C, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 3rd Year - 2nd Semester
        """Third Year - Second Semester - Compulsory Courses:
IR203, Diplomatic History, C, Credit:3, ECTS:6, Hours:3
EU308, European Monetary, C, Credit:3, ECTS:6, Hours:3
IR208, Introduction to International Relations II, C, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 4th Year - 1st Semester
        """Fourth Year - First Semester - Compulsory Courses:
EU404, EU and International Trade, C, Credit:3, ECTS:6, Hours:3
EU406, The European Economy, C, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 4th Year - 2nd Semester
        """Fourth Year - Second Semester - Compulsory Courses:
EU410, European Union Labour Market, C, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # Elective Courses
        """Elective Course Options for European Union Relations:

EU Policy and Governance Electives:
EU302, EU Environmental Policy
EU303, EU Social Policy
EU304, EU Regional Policy
EU305, EU Agricultural Policy
EU306, EU External Relations
EU307, EU Enlargement Policy

Economics and Business Electives:
EAS301, International Economics
EAS302, Development Economics
EAS303, Public Finance
EAS304, Monetary Economics
MAN301, International Business
MAN302, Cross-Cultural Management

Law and Political Science Electives:
EAS206, Administrative Law
EAS207, International Law
IR301, Foreign Policy Analysis
IR302, International Organizations
IR303, Conflict Resolution
IR304, Global Governance

Research and Special Topics:
EU409, EU Research Methods
EU411, EU Project Management
EU412, Current Issues in EU Affairs
EU413, EU-Turkey Relations
EU414, Comparative Regional Integration
EU415, EU Lobbying and Interest Groups""",

        # Core Course Descriptions
        """Core Course Descriptions - European Union Focus:

EU100 - Introduction to European Integration:
Historical development of European integration, EU institutions, decision-making processes, and key policies.

EU201 - EU Competition Policy:
EU competition law, antitrust regulations, state aid rules, and merger control in the European single market.

EU208 - Theories of EU Integration:
Theoretical approaches to European integration including federalism, functionalism, and intergovernmentalism.

EU301 - History of Europe:
European history from ancient times to present, focusing on political, economic, and cultural developments.

EU308 - European Monetary:
European monetary systems, Eurozone economics, monetary policy, and financial integration.

EU404 - EU and International Trade:
EU trade policy, WTO relations, trade agreements, and the EU's role in global trade governance.

EU406 - The European Economy:
Structure and performance of the European economy, economic policies, and challenges of economic integration.

EU410 - European Union Labour Market:
EU labor market policies, employment strategies, social dialogue, and worker mobility within the EU.

IR207/208 - Introduction to International Relations:
Theories of international relations, global politics, and the role of international organizations.

IR203 - Diplomatic History:
Historical development of diplomatic relations, major international treaties, and diplomatic practices.""",

        # Program Summary and Career Opportunities
        """European Union Relations Program Summary:
Degree: Bachelor of Arts in European Union Relations
Duration: 4 years (8 semesters)
Total ECTS: 240
Language of Instruction: English

Program Focus Areas:
- EU Institutions and Governance
- European Integration Theories
- EU Economic and Monetary Policies
- EU External Relations
- International Relations and Diplomacy
- EU-Turkey Relations
- European Law and Policy Making

Core Competencies Developed:
- Understanding of EU institutional framework
- Analysis of European integration processes
- Knowledge of EU policies and legislation
- International relations theory application
- Economic analysis of European markets
- Diplomatic and negotiation skills
- Research and policy analysis

Career Opportunities:
EU Affairs Specialist
International Relations Officer
Policy Analyst
Diplomatic Service Officer
EU Project Coordinator
International Organization Staff
Government Relations Specialist
EU Lobbyist and Consultant
Research Analyst in European Studies
International Business Consultant
NGO Program Officer

Professional Settings:
European Union Institutions
Government Ministries (Foreign Affairs, EU Affairs)
International Organizations
Diplomatic Missions and Embassies
Multinational Corporations
Non-Governmental Organizations
Research Institutes and Think Tanks
Public Relations and Consulting Firms
Academic and Teaching Positions""",

        # Program Structure and Specializations
        """Program Structure and Specialization Tracks:

Foundation Year (1st Year):
- Basic economics and business principles
- Mathematics and statistics for social sciences
- Introduction to European integration
- Language and communication skills

Core Development (2nd Year):
- Advanced economics (micro and macro)
- Political science and constitutional law
- EU competition policy and integration theories
- Business communication and statistics

Specialization (3rd Year):
- European history and international relations
- Constitutional law and diplomatic history
- European monetary systems
- Elective course specialization

Professional Preparation (4th Year):
- Advanced EU policies and international trade
- European economy and labor markets
- Extensive elective course selection
- Professional skill development

Specialization Tracks:
1. EU Policy and Governance: Institutional analysis, policy making, governance structures
2. EU Economics and Business: Economic integration, trade policies, business environment
3. International Relations: Diplomacy, foreign policy, global governance
4. EU-Turkey Relations: Bilateral relations, accession process, regional cooperation

Unique Program Features:
- Focus on EU-Turkey relations context
- Integration of economics and political science
- English language instruction
- International perspective on European affairs"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Economics and Administrative Sciences",
            "department": "European Union Relations",
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
            "content_type": "elective_courses"
        },
        {
            "course_type": "core",
            "document_type": "course_description",
            "content_type": "eu_core_courses"
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
    ids = [f"eu_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} European Union Relations curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["EU integration policies European economy"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_eu_relations_curriculum_to_chromadb()