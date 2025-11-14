import chromadb
from chromadb.utils import embedding_functions

def add_business_admin_curriculum_to_chromadb():
    """Add Business Administration curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_business_administration",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_business_administration",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_business_administration")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF ECONOMICS AND ADMINISTRATIVE SCIENCES
DEPARTMENT OF BUSINESS ADMINISTRATION
Bachelor of Science in Business Administration

Program Duration: 4 years (8 semesters)
Degree: Bachelor of Science
Total ECTS for Graduation: 240

Main website: https://iktisat.neu.edu.tr/?lang=en
Curriculum link: https://iktisat.neu.edu.tr/academic/academic-programmes/department-of-business-administration/courses/?lang=en

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
YİT/TUR101, Turkish for International Students I/Turkish Language I, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:30, Hours:17""",

        # 1st Year - 2nd Semester
        """First Year - Second Semester - Compulsory Courses:
ENG102, English II, C, Credit:3, ECTS:4, Hours:3
COM102, Computer Applications, C, Credit:3, ECTS:6, Hours:3
MTH172, Mathematics for Business & Economics II, C, Credit:3, ECTS:6, Hours:3
EAS102, Principles of Economics II, C, Credit:3, ECTS:6, Hours:3
EAS104, Principles of Management, C, Credit:3, ECTS:6, Hours:3
YİT102/TUR102, Turkish for International Students II/Turkish Language II, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:30, Hours:17""",

        # 2nd Year - 1st Semester
        """Second Year - First Semester - Compulsory Courses:
MAN201, Communication for Business I, C, Credit:3, ECTS:4, Hours:3
EAS203, Financial Accounting I, C, Credit:3, ECTS:6, Hours:3
MTH261, Statistics I, C, Credit:3, ECTS:6, Hours:3
MRK308, Marketing Communications, C, Credit:3, ECTS:6, Hours:3
EAS206, Introduction to Law, C, Credit:3, ECTS:6, Hours:3
AİT101/103, Atatürk's Principles I/Principles of Atatürk I, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:30, Hours:17""",

        # 2nd Year - 2nd Semester
        """Second Year - Second Semester - Compulsory Courses:
MAN202, Communication for Business II, C, Credit:3, ECTS:4, Hours:3
EAS204, Financial Accounting II, C, Credit:3, ECTS:6, Hours:3
MTH262, Statistics II, C, Credit:3, ECTS:6, Hours:3
SOC100, Sociology, C, Credit:3, ECTS:6, Hours:3
EAS207, Business Law, C, Credit:3, ECTS:6, Hours:3
AİT102/104, Atatürk's Principles II/Principles of Atatürk II, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:30, Hours:17""",

        # 3rd Year - 1st Semester
        """Third Year - First Semester - Compulsory Courses:
EAS310, Organizational Behaviour, C, Credit:3, ECTS:6, Hours:3
EAS305, Principles of Marketing, C, Credit:3, ECTS:6, Hours:3
EAS303, Managerial Accounting, C, Credit:3, ECTS:6, Hours:3
EAS301, Business Finance, C, Credit:3, ECTS:6, Hours:3
MRK324, Approaches to Psychology in Marketing, C, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 3rd Year - 2nd Semester
        """Third Year - Second Semester - Compulsory Courses:
EAS308, Operations Research and Management, C, Credit:3, ECTS:6, Hours:3
EAS304, Marketing Management, C, Credit:3, ECTS:6, Hours:3
EAS307, Research Methods, C, Credit:3, ECTS:6, Hours:3
EAS302, Financial Management, C, Credit:3, ECTS:6, Hours:3
MARK307, Consumer Behaviour, C, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 4th Year - 1st Semester
        """Fourth Year - First Semester - Compulsory Courses:
EAS405, Production Management, C, Credit:3, ECTS:6, Hours:3
EAS403, Marketing Research, C, Credit:3, ECTS:6, Hours:3
EAS402, Human Resource Management, C, Credit:3, ECTS:6, Hours:3
Elective Course, Area Elective, E, Credit:3, ECTS:6, Hours:3
Elective Course, Area Elective, E, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 4th Year - 2nd Semester
        """Fourth Year - Second Semester - Compulsory Courses:
MRK412, Digital Marketing, C, Credit:2, ECTS:6, Hours:3
MAN407, Strategic Management, C, Credit:3, ECTS:6, Hours:3
Elective Course, Area Elective, E, Credit:3, ECTS:6, Hours:3
Elective Course, Area Elective, E, Credit:3, ECTS:6, Hours:3
Elective Course, Area Elective, E, Credit:3, ECTS:6, Hours:3

Total: Credit:14, ECTS:30, Hours:15""",

        # Elective Courses
        """Area Elective Course Options for Business Administration:

Finance and Accounting Electives:
EAS408, Advanced Financial Management
EAS409, Investment Analysis
EAS410, International Finance
EAS411, Corporate Finance
EAS412, Financial Markets and Institutions
EAS413, Auditing
EAS414, Tax Accounting
EAS415, Cost Accounting

Marketing and Sales Electives:
EAS416, International Marketing
EAS417, Sales Management
EAS418, Brand Management
EAS419, Services Marketing
EAS420, Retail Management
EAS421, Advertising and Promotion
EAS422, E-commerce and Digital Business
EAS423, Customer Relationship Management

Management and Strategy Electives:
EAS424, Entrepreneurship and Small Business Management
EAS425, Project Management
EAS426, Quality Management
EAS427, Supply Chain Management
EAS428, International Business
EAS429, Business Ethics and Corporate Governance
EAS430, Innovation Management
EAS431, Crisis Management

Human Resources and Organizational Behavior Electives:
EAS432, Leadership and Team Management
EAS433, Compensation and Benefits Management
EAS434, Training and Development
EAS435, Organizational Development
EAS436, Labor Relations
EAS437, Cross-Cultural Management
EAS438, Talent Management
EAS439, Performance Management

Operations and Technology Electives:
EAS440, Operations Management
EAS441, Management Information Systems
EAS442, Business Analytics
EAS443, Technology Management
EAS444, Logistics Management
EAS445, Service Operations Management
EAS446, Production Planning and Control
EAS447, Quality Control Systems""",

        # Core Course Descriptions
        """Core Course Descriptions - Business Administration Focus:

EAS104 - Principles of Management:
Fundamental management concepts, planning, organizing, leading, and controlling functions in organizations.

EAS310 - Organizational Behaviour:
Individual and group behavior in organizations, motivation, leadership, communication, and organizational culture.

EAS305 - Principles of Marketing:
Marketing concepts, market analysis, product development, pricing, distribution, and promotion strategies.

EAS301/302 - Business Finance & Financial Management:
Financial principles, capital budgeting, financial analysis, and corporate financial decision-making.

EAS303 - Managerial Accounting:
Cost analysis, budgeting, performance measurement, and accounting information for management decisions.

EAS308 - Operations Research and Management:
Quantitative methods for business decision-making, optimization techniques, and operational efficiency.

EAS304 - Marketing Management:
Strategic marketing planning, implementation, and control of marketing programs and campaigns.

EAS307 - Research Methods:
Research design, data collection methods, statistical analysis, and research reporting for business.

EAS405 - Production Management:
Operations management, production planning, quality control, and supply chain management.

EAS403 - Marketing Research:
Market research techniques, data analysis, and application of research findings to marketing decisions.

EAS402 - Human Resource Management:
HR functions including recruitment, selection, training, performance management, and compensation.

MAN407 - Strategic Management:
Strategic analysis, formulation, implementation, and evaluation of business strategies.

MRK412 - Digital Marketing:
Online marketing strategies, social media marketing, SEO, and digital advertising platforms.

MARK307 - Consumer Behaviour:
Psychological and sociological factors influencing consumer decision-making and buying behavior.""",

        # Program Summary and Career Opportunities
        """Business Administration Program Summary:
Degree: Bachelor of Science in Business Administration
Duration: 4 years (8 semesters)
Total ECTS: 240
Language of Instruction: English

Program Focus Areas:
- General Management and Leadership
- Marketing and Sales Management
- Financial Management and Accounting
- Human Resource Management
- Operations and Production Management
- Strategic Planning and Business Development
- Research and Business Analytics

Core Competencies Developed:
- Strategic thinking and decision-making
- Financial analysis and management
- Marketing strategy and consumer analysis
- Organizational leadership and team management
- Operations and production management
- Business research and data analysis
- Communication and negotiation skills
- Ethical business practices

Career Opportunities:
Business Manager
Marketing Manager
Financial Analyst
Operations Manager
Human Resources Manager
Sales Manager
Project Manager
Management Consultant
Business Development Manager
Entrepreneur/Business Owner
Supply Chain Manager
Product Manager
Strategic Planner
Account Manager

Professional Settings:
Multinational Corporations
Small and Medium Enterprises
Financial Institutions
Consulting Firms
Manufacturing Companies
Service Industry
Technology Companies
Retail and Wholesale Businesses
Government Agencies
Non-Profit Organizations
Startups and Entrepreneurship
Family Businesses""",

        # Program Structure and Specializations
        """Program Structure and Specialization Tracks:

Foundation Year (1st Year):
- Basic economics and business principles
- Mathematics and statistics foundation
- Computer applications and technology
- Management fundamentals and organizational basics

Core Development (2nd Year):
- Financial accounting and business law
- Statistics and quantitative methods
- Marketing communications
- Sociology and organizational context

Functional Specialization (3rd Year):
- Organizational behavior and psychology
- Marketing principles and management
- Financial and managerial accounting
- Operations research and management
- Consumer behavior and research methods

Strategic Integration (4th Year):
- Production and operations management
- Human resource management
- Strategic management
- Digital marketing
- Extensive area elective specialization

Specialization Tracks through Electives:
1. Finance and Accounting: Financial management, investment analysis, corporate finance
2. Marketing Management: Brand management, digital marketing, international marketing
3. Human Resource Management: Training, compensation, organizational development
4. Operations Management: Supply chain, quality management, production planning
5. Entrepreneurship and Strategy: Innovation, project management, business development

Unique Program Features:
- Comprehensive business education covering all functional areas
- Strong analytical and quantitative foundation
- Integration of theory with practical business applications
- Preparation for leadership roles in diverse business environments
- Flexibility to specialize through extensive elective options"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Economics and Administrative Sciences",
            "department": "Business Administration",
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
            "content_type": "area_electives"
        },
        {
            "course_type": "core",
            "document_type": "course_description",
            "content_type": "business_core_courses"
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
        print(f"Successfully added {len(documents)} Business Administration curriculum documents to ChromaDB!")
        print("✅ Degree correctly set as: Bachelor of Science in Business Administration")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["business management marketing finance strategy"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_business_admin_curriculum_to_chromadb()