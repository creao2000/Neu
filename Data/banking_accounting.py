




# import chromadb

# # Initialize ChromaDB client
# chroma_client = chromadb.PersistentClient(path="./chroma_db")

# # List all collections first to confirm
# collections = chroma_client.list_collections()
# print("Current collections:", [col.name for col in collections])

# # Delete the specific collection
# try:
#     chroma_client.delete_collection(name="neu_banking_accounting")
#     print("✅ Collection 'neu_banking_accounting' deleted successfully!")
# except Exception as e:
#     print(f"❌ Error deleting collection: {e}")

# # Verify it's gone
# collections = chroma_client.list_collections()
# print("Remaining collections:", [col.name for col in collections])






import chromadb
from chromadb.utils import embedding_functions

def add_banking_accounting_curriculum_to_chromadb():
    """Add Banking and Accounting curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_banking_accounting",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_banking_accounting",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_banking_accounting")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF ECONOMICS AND ADMINISTRATIVE SCIENCES
DEPARTMENT OF BANKING AND ACCOUNTING
Bachelor of Arts in Banking and Accounting


Main website: https://iktisat.neu.edu.tr/?lang=en
Curriculum link: https://iktisat.neu.edu.tr/academic/academic-programmes/department-of-banking-and-accounting-2/courses/?lang=en

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
BANK303, Principles of Banking I, C, Credit:3, ECTS:6, Hours:3
EAS301, Financial Management I, C, Credit:3, ECTS:6, Hours:3
EAS306, Money and Banking, C, Credit:3, ECTS:6, Hours:3
FIN304, Investment Fundamentals, C, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 3rd Year - 2nd Semester
        """Third Year - Second Semester - Compulsory Courses:
BANK304, Principles of Banking II, C, Credit:3, ECTS:6, Hours:3
EAS302, Financial Management II, C, Credit:3, ECTS:6, Hours:3
FIN403, Portfolio Management, C, Credit:3, ECTS:6, Hours:3
BANK310, Bank Training, C, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 4th Year - 1st Semester
        """Fourth Year - First Semester - Compulsory Courses:
BANK405, Risk Management, C, Credit:3, ECTS:6, Hours:3
FIN404, International Finance, C, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 4th Year - 2nd Semester
        """Fourth Year - Second Semester - Compulsory Courses:
BANK408, International Banking, C, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # Elective Courses
        """Elective Course Options for Banking and Accounting:

Banking Specialization Electives:
BANK401, Commercial Banking Operations
BANK402, Retail Banking
BANK403, Corporate Banking
BANK404, Islamic Banking and Finance
BANK406, Bank Credit Analysis
BANK407, Central Banking
BANK409, Banking Regulations and Compliance
BANK410, Digital Banking and FinTech

Accounting and Finance Electives:
EAS303, Cost Accounting
EAS304, Managerial Accounting
EAS305, Auditing
EAS307, Tax Accounting
EAS308, Advanced Financial Accounting
FIN401, Corporate Finance
FIN402, Financial Markets and Institutions
FIN405, Derivatives and Risk Management

Economics and Business Electives:
EAS309, International Economics
EAS310, Econometrics
EAS311, Public Finance
MAN301, Organizational Behavior
MAN302, Human Resource Management
MAN303, Strategic Management
MAN304, Marketing Management

Special Topics and Applications:
BANK411, Bank Internship and Case Studies
BANK412, Financial Statement Analysis
BANK413, Banking Software Applications
BANK414, Ethical Issues in Banking
BANK415, Crisis Management in Banking""",

        # Core Course Descriptions
        """Core Course Descriptions - Banking and Accounting Focus:

BANK303/304 - Principles of Banking I & II:
Banking operations, financial intermediation, banking products and services, regulatory framework.

EAS203/204 - Financial Accounting I & II:
Accounting principles, financial statements, transaction recording, accounting cycle, and reporting standards.

EAS301/302 - Financial Management I & II:
Corporate finance, capital budgeting, working capital management, financial analysis, and decision-making.

EAS306 - Money and Banking:
Monetary systems, central banking, money supply, interest rates, and financial markets.

FIN304 - Investment Fundamentals:
Investment principles, security analysis, risk-return tradeoff, and investment vehicles.

FIN403 - Portfolio Management:
Portfolio theory, asset allocation, performance measurement, and investment strategies.

BANK310 - Bank Training:
Practical banking operations, customer service, banking software, and professional development.

BANK405 - Risk Management:
Credit risk, market risk, operational risk, risk assessment techniques, and mitigation strategies.

FIN404 - International Finance:
Foreign exchange markets, international capital flows, multinational corporate finance.

BANK408 - International Banking:
Cross-border banking operations, international regulations, correspondent banking, and global financial services.

MAN201/202 - Communication for Business I & II:
Business communication skills, professional writing, presentations, and interpersonal communication.""",

        # Program Summary and Career Opportunities
        """Banking and Accounting Program Summary:
Degree: Bachelor of Arts in Banking and Accounting
Duration: 4 years (8 semesters)
Total ECTS: 240
Language of Instruction: English

Program Focus Areas:
- Banking Operations and Management
- Financial Accounting and Reporting
- Financial Management and Analysis
- Investment and Portfolio Management
- Risk Management and Compliance
- International Banking and Finance
- Business Law and Regulations

Core Competencies Developed:
- Financial statement analysis and interpretation
- Banking operations and product knowledge
- Financial management and investment analysis
- Risk assessment and management techniques
- Regulatory compliance understanding
- Business communication and professional skills
- Computer applications in finance and accounting

Career Opportunities:
Banking Officer
Financial Analyst
Accountant
Credit Analyst
Risk Management Specialist
Investment Advisor
Portfolio Manager
Audit Assistant
Financial Controller
Treasury Analyst
Compliance Officer
Branch Manager
Relationship Manager

Professional Settings:
Commercial Banks
Investment Banks
Accounting Firms
Financial Institutions
Insurance Companies
Corporate Finance Departments
Audit and Consulting Firms
Government Financial Agencies
Regulatory Bodies
Investment Companies
Financial Technology (FinTech) Companies""",

        # Program Structure and Specializations
        """Program Structure and Specialization Tracks:

Foundation Year (1st Year):
- Basic economics and business principles
- Mathematics and statistics foundation
- Computer applications and technology
- Language and communication skills

Core Development (2nd Year):
- Financial accounting principles
- Advanced economics (micro and macro)
- Business law and regulations
- Statistics and quantitative methods

Specialization (3rd Year):
- Banking principles and operations
- Financial management and analysis
- Investment fundamentals
- Money and banking systems
- Practical bank training

Professional Preparation (4th Year):
- Advanced risk management
- International finance and banking
- Portfolio management
- Extensive elective specialization
- Professional skill development

Specialization Tracks:
1. Commercial Banking: Retail banking, corporate banking, credit analysis, branch operations
2. Investment Banking: Securities analysis, portfolio management, investment strategies
3. Financial Accounting: Financial reporting, auditing, tax accounting, cost accounting
4. Risk Management: Credit risk, market risk, operational risk, compliance

Unique Program Features:
- Integration of banking and accounting disciplines
- Practical bank training component
- Focus on both domestic and international finance
- Strong foundation in financial regulations
- English language business communication focus"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Economics and Administrative Sciences",
            "department": "Banking and Accounting",
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
            "content_type": "banking_core_courses"
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
    ids = [f"ba_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Banking and Accounting curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["banking accounting financial management"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_banking_accounting_curriculum_to_chromadb()