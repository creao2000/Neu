import chromadb
from chromadb.utils import embedding_functions

def add_international_business_curriculum_to_chromadb():
    """Add International Business curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_international_business",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_international_business",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_international_business")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF ECONOMICS AND ADMINISTRATIVE SCIENCES
DEPARTMENT OF INTERNATIONAL BUSINESS
Bachelor of International Business

Program Duration: 4 years (8 semesters)
Degree: Bachelor of Science
Total ECTS for Graduation: 240

Main website: https://iktisat.neu.edu.tr/?lang=en
Curriculum link: https://iktisat.neu.edu.tr/academic/academic-programmes/department-of-international-business/courses/?lang=en

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
COM102, Computer Applications, C, Credit:3, ECTS:6, Hours:3
MTH172, Mathematics for Business & Economics II, C, Credit:3, ECTS:6, Hours:3
EAS102, Principles of Economics II, C, Credit:3, ECTS:6, Hours:3
EAS104, Principles of Management, C, Credit:3, ECTS:6, Hours:3
YIT102/TUR102, Turkish for International Students II/Turkish Language II, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:30, Hours:17""",

        # 2nd Year - 1st Semester
        """Second Year - First Semester - Compulsory Courses:
MAN201, Communication for Business I, C, Credit:3, ECTS:6, Hours:3
EAS203, Financial Accounting I, C, Credit:3, ECTS:6, Hours:3
MTH261, Statistics I, C, Credit:3, ECTS:6, Hours:3
EAS201, Microeconomics, C, Credit:3, ECTS:6, Hours:3
EAS206, Introduction to Law, C, Credit:3, ECTS:6, Hours:3
AİT101/103, Atatürk's Principles I/Principles of Atatürk I, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:32, Hours:17""",

        # 2nd Year - 2nd Semester
        """Second Year - Second Semester - Compulsory Courses:
MAN202, Communication for Business II, C, Credit:3, ECTS:6, Hours:3
EAS204, Financial Accounting II, C, Credit:3, ECTS:6, Hours:3
MTH262, Statistics II, C, Credit:3, ECTS:6, Hours:3
EAS202, Macroeconomics, C, Credit:3, ECTS:6, Hours:3
EAS207, Business Law, C, Credit:3, ECTS:6, Hours:3
AİT102/104, Atatürk's Principles II/Principles of Atatürk II, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:32, Hours:17""",

        # 3rd Year - 1st Semester
        """Third Year - First Semester - Compulsory Courses:
EAS310, Organizational Behaviour, C, Credit:3, ECTS:6, Hours:3
EAS305, Principles of Marketing, C, Credit:3, ECTS:6, Hours:3
EAS303, Managerial Accounting, C, Credit:3, ECTS:6, Hours:3
EAS301, Business Finance, C, Credit:3, ECTS:6, Hours:3
EAS306, Money and Banking, C, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 3rd Year - 2nd Semester
        """Third Year - Second Semester - Compulsory Courses:
EAS308, Operations Research and Management, C, Credit:3, ECTS:6, Hours:3
EAS304, Marketing Management, C, Credit:3, ECTS:6, Hours:3
EAS307, Research Methods, C, Credit:3, ECTS:6, Hours:3
EAS302, Financial Management, C, Credit:3, ECTS:6, Hours:3
MAN303, Cross Culture Communication, C, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 4th Year - 1st Semester
        """Fourth Year - First Semester - Compulsory Courses:
MAN409, Management Information Systems, C, Credit:3, ECTS:6, Hours:3
EAS403, Marketing Research, C, Credit:3, ECTS:6, Hours:3
MAN424, Enterprise Resource Planning, C, Credit:3, ECTS:6, Hours:3
MAN388, Trade Agreement, C, Credit:3, ECTS:6, Hours:3
Elective Course, International Business Elective, E, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 4th Year - 2nd Semester
        """Fourth Year - Second Semester - Compulsory Courses:
EAS401, International Business, C, Credit:3, ECTS:6, Hours:3
FIN404, International Finance, C, Credit:3, ECTS:6, Hours:3
Elective Course, International Business Elective, E, Credit:3, ECTS:6, Hours:3
Elective Course, International Business Elective, E, Credit:3, ECTS:6, Hours:3
Elective Course, International Business Elective, E, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # Elective Courses
        """Elective Course Options for International Business:

International Trade and Economics:
IB401, International Trade Theory and Policy
IB402, Global Supply Chain Management
IB403, Export-Import Management
IB404, International Economic Institutions
IB405, Trade Finance and Documentation
IB406, Customs Procedures and Regulations
IB407, International Trade Law

Global Business Management:
IB408, Multinational Corporation Management
IB409, Global Strategic Management
IB410, International Human Resource Management
IB411, Cross-Cultural Negotiation
IB412, Global Leadership
IB413, International Business Ethics
IB414, Emerging Markets Business

Regional Business Studies:
IB415, European Business Environment
IB416, Asian Business Practices
IB417, Middle Eastern Markets
IB418, North American Business Systems
IB419, Latin American Business Culture
IB420, African Business Opportunities
IB421, Turkish Business in Global Context

International Marketing and Finance:
IB422, Global Marketing Strategy
IB423, International Brand Management
IB424, Foreign Exchange Risk Management
IB425, International Investment Analysis
IB426, Global E-commerce
IB427, International Consumer Behavior
IB428, Digital International Marketing

Specialized International Topics:
IB429, International Entrepreneurship
IB430, Global Business Project Management
IB431, International Business Negotiations
IB432, Business in Islamic Countries
IB433, International Business Research
IB434, Sustainable Global Business
IB435, International Business Simulation""",

        # Core Course Descriptions
        """Core Course Descriptions - International Business Focus:

EAS401 - International Business:
Global business environment, international market entry strategies, and multinational corporation management.

MAN303 - Cross Culture Communication:
Cultural differences in business communication, negotiation styles, and intercultural management.

FIN404 - International Finance:
Foreign exchange markets, international capital flows, multinational corporate finance, and risk management.

MAN388 - Trade Agreement:
International trade agreements, WTO regulations, regional trade blocs, and trade policy.

MAN409 - Management Information Systems:
Information technology in global business, ERP systems, and digital business transformation.

MAN424 - Enterprise Resource Planning:
Integrated business management systems, process optimization, and global operations coordination.

EAS306 - Money and Banking:
International monetary systems, banking operations, and global financial markets.

EAS308 - Operations Research and Management:
Quantitative methods for international business decision-making and operational efficiency.

EAS403 - Marketing Research:
International market research methods, consumer behavior analysis, and global market intelligence.

MAN201/202 - Communication for Business I & II:
Professional business communication skills for international business contexts.

EAS307 - Research Methods:
Research design and methodology for international business studies and market analysis.""",

        # Program Summary and Career Opportunities
        """International Business Program Summary:
Degree: Bachelor of Science in International Business
Duration: 4 years (8 semesters)
Total ECTS: 240
Language of Instruction: English

Program Focus Areas:
- International Trade and Economics
- Cross-Cultural Business Management
- Global Marketing and Finance
- International Business Strategy
- Multinational Corporation Operations
- Global Supply Chain Management
- International Business Law and Ethics

Core Competencies Developed:
- Global business strategy formulation
- Cross-cultural communication and negotiation
- International market analysis and entry
- Multinational financial management
- Global supply chain coordination
- International trade regulations knowledge
- Cultural intelligence and adaptation
- International business research skills

Career Opportunities:
International Business Manager
Export-Import Specialist
Global Marketing Manager
International Trade Analyst
Multinational Corporation Executive
Cross-Cultural Consultant
Global Supply Chain Manager
International Financial Analyst
Foreign Market Entry Specialist
International Business Development Manager
Trade Compliance Officer
Global Operations Manager
International Project Manager
Foreign Investment Analyst

Professional Settings:
Multinational Corporations
Export-Import Companies
International Trading Firms
Global Logistics and Supply Chain Companies
International Banks and Financial Institutions
Foreign Investment Agencies
Government Trade Departments
International Consulting Firms
Chambers of Commerce and Trade Associations
Global Manufacturing Companies
International Service Providers
E-commerce Global Companies
Foreign Market Research Firms""",

        # Program Structure and Specializations
        """Program Structure and Specialization Tracks:

Foundation Year (1st Year):
- Basic business and economics principles
- Mathematics and statistics foundation
- Computer applications and technology
- Management and organizational basics

Core Development (2nd Year):
- Financial accounting and business law
- Statistics and quantitative methods
- Micro and macroeconomics
- Business communication skills

Business Specialization (3rd Year):
- Organizational behavior and marketing
- Financial and managerial accounting
- Operations research and management
- Cross-cultural communication
- Money and banking systems

International Focus (4th Year):
- International business and finance
- Management information systems
- Enterprise resource planning
- Trade agreements and regulations
- Extensive international business electives

Specialization Tracks through Electives:
1. International Trade: Export-import, trade agreements, supply chain, customs
2. Global Management: Multinational corporations, cross-cultural management, strategy
3. International Marketing: Global marketing, brand management, consumer behavior
4. International Finance: Foreign exchange, investment analysis, risk management
5. Regional Business: Specific geographic market expertise

Unique Program Features:
- Strong emphasis on cross-cultural business competence
- Integration of technology and global business systems
- Focus on both theoretical and practical international business
- Preparation for diverse global business environments
- English language instruction with international perspective"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Economics and Administrative Sciences",
            "department": "International Business",
            "degree": "Bachelor of Science",
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
            "content_type": "international_business_electives"
        },
        {
            "course_type": "core",
            "document_type": "course_description",
            "content_type": "international_business_core_courses"
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
    ids = [f"ib_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} International Business curriculum documents to ChromaDB!")
        print("✅ Degree correctly set as: Bachelor of Science in International Business")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["international business cross cultural trade finance"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_international_business_curriculum_to_chromadb()