import chromadb
from chromadb.utils import embedding_functions

def add_marketing_curriculum_to_chromadb():
    """Add Marketing curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_marketing",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_marketing",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_marketing")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF ECONOMICS AND ADMINISTRATIVE SCIENCES
DEPARTMENT OF MARKETING
Bachelor of Science in Marketing

Program Duration: 4 years (8 semesters)
Degree: Bachelor of Science in Marketing
Total ECTS for Graduation: 240

Main website: https://iktisat.neu.edu.tr/?lang=en
Curriculum link: https://iktisat.neu.edu.tr/academic/academic-programmes/department-of-marketing/courses/?lang=en

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
MAN201, Communication for Business I, C, Credit:3, ECTS:4, Hours:3
EAS203, Financial Accounting I, C, Credit:3, ECTS:6, Hours:3
MTH261, Statistics I, C, Credit:3, ECTS:6, Hours:3
EAS201, Microeconomics, C, Credit:3, ECTS:6, Hours:3
EAS206, Introduction to Law, C, Credit:3, ECTS:6, Hours:3
AİT101/103, Atatürk's Principles I/Principles of Atatürk I, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:30, Hours:17""",

        # 2nd Year - 2nd Semester
        """Second Year - Second Semester - Compulsory Courses:
MAN202, Communication for Business II, C, Credit:3, ECTS:4, Hours:3
EAS204, Financial Accounting II, C, Credit:3, ECTS:6, Hours:3
MTH262, Statistics II, C, Credit:3, ECTS:6, Hours:3
EAS202, Macroeconomics, C, Credit:3, ECTS:6, Hours:3
EAS207, Business Law, C, Credit:3, ECTS:6, Hours:3
AİT102/104, Atatürk's Principles II/Principles of Atatürk II, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:30, Hours:17""",

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
SOC100, Sociology, C, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 4th Year - 1st Semester
        """Fourth Year - First Semester - Compulsory Courses:
EAS405, Production Management, C, Credit:3, ECTS:6, Hours:3
EAS403, Marketing Research, C, Credit:3, ECTS:6, Hours:3
EAS402, Human Resource Management, C, Credit:3, ECTS:6, Hours:3
Area Elective, Marketing Elective, E, Credit:3, ECTS:6, Hours:3
Area Elective, Marketing Elective, E, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 4th Year - 2nd Semester
        """Fourth Year - Second Semester - Compulsory Courses:
EAS401, International Business, C, Credit:3, ECTS:6, Hours:3
MAN407, Strategic Management, C, Credit:3, ECTS:6, Hours:3
Area Elective, Marketing Elective, E, Credit:3, ECTS:6, Hours:3
Area Elective, Marketing Elective, E, Credit:3, ECTS:6, Hours:3
Area Elective, Marketing Elective, E, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # Area Elective Courses
        """Area Elective Course Options for Marketing:

Digital Marketing Electives:
MRK410, Digital Marketing and E-commerce
MRK411, Social Media Marketing
MRK412, Search Engine Optimization (SEO)
MRK413, Content Marketing Strategy
MRK414, Mobile Marketing
MRK415, Web Analytics and Metrics
MRK416, Digital Advertising Campaigns

Strategic Marketing Electives:
MRK420, Brand Management and Strategy
MRK421, Product Management and Development
MRK422, Pricing Strategies
MRK423, Distribution Channel Management
MRK424, Marketing Strategy and Planning
MRK425, Competitive Marketing Analysis
MRK426, Marketing Metrics and ROI

Consumer Behavior and Research Electives:
MRK430, Consumer Behavior Analysis
MRK431, Market Research Techniques
MRK432, Customer Relationship Management (CRM)
MRK433, Customer Experience Management
MRK434, Psychographics and Lifestyle Marketing
MRK435, Neuromarketing
MRK436, Qualitative Research Methods

International and Services Marketing:
MRK440, International Marketing
MRK441, Cross-Cultural Marketing
MRK442, Services Marketing
MRK443, Tourism and Hospitality Marketing
MRK444, Export Marketing
MRK445, Global Brand Management
MRK446, International Market Entry Strategies

Advertising and Promotion Electives:
MRK450, Advertising Management
MRK451, Public Relations and Corporate Communication
MRK452, Sales Promotion Techniques
MRK453, Event Marketing and Sponsorship
MRK454, Creative Strategy in Advertising
MRK455, Media Planning and Buying
MRK456, Integrated Marketing Communications

Specialized Marketing Areas:
MRK460, Retail Marketing
MRK461, Business-to-Business (B2B) Marketing
MRK462, Non-Profit Marketing
MRK463, Social Marketing
MRK464, Sports Marketing
MRK465, Fashion and Luxury Marketing
MRK466, Healthcare Marketing""",

        # Core Marketing Course Descriptions
        """Core Course Descriptions - Marketing Focus:

EAS305 - Principles of Marketing:
Fundamental marketing concepts, market analysis, consumer behavior, marketing mix, and marketing environment.

EAS304 - Marketing Management:
Strategic marketing planning, implementation, control of marketing programs, and marketing decision-making.

EAS403 - Marketing Research:
Research design, data collection methods, statistical analysis, and application of research findings to marketing decisions.

EAS307 - Research Methods:
Research methodology, survey design, experimental research, and data analysis techniques for business research.

MAN407 - Strategic Management:
Strategic analysis, competitive advantage, corporate strategy, and strategic planning in business context.

EAS401 - International Business:
Global business environment, international trade, foreign market entry strategies, and cross-cultural management.

EAS310 - Organizational Behaviour:
Individual and group behavior in organizations, motivation, leadership, and organizational culture.

EAS405 - Production Management:
Operations management, production planning, quality control, and supply chain management.

EAS402 - Human Resource Management:
HR functions including recruitment, training, performance management, and organizational development.

EAS301/302 - Business Finance & Financial Management:
Financial principles, capital budgeting, financial analysis, and corporate financial decision-making.""",

        # Program Summary and Career Opportunities
        """Marketing Program Summary:
Degree: Bachelor of Science in Marketing
Duration: 4 years (8 semesters)
Total ECTS: 240
Language of Instruction: English

Program Focus Areas:
- Marketing Strategy and Planning
- Consumer Behavior and Market Research
- Digital and Social Media Marketing
- Brand Management and Development
- Advertising and Promotion
- International Marketing
- Marketing Analytics and Metrics

Core Competencies Developed:
- Market analysis and segmentation
- Marketing strategy development
- Consumer behavior understanding
- Marketing research and data analysis
- Digital marketing techniques
- Brand management skills
- Advertising and promotion planning
- International marketing knowledge

Career Opportunities:
Marketing Manager
Brand Manager
Digital Marketing Specialist
Market Research Analyst
Advertising Manager
Social Media Manager
Product Manager
Sales Manager
Marketing Consultant
Public Relations Specialist
Content Marketing Manager
E-commerce Manager
Customer Relationship Manager
Media Planner

Professional Settings:
Advertising Agencies
Marketing Departments in Corporations
Market Research Firms
Digital Marketing Agencies
Public Relations Firms
Retail and E-commerce Companies
Media and Entertainment Industry
Consumer Goods Companies
Technology and Software Companies
Healthcare and Pharmaceutical Industry
Hospitality and Tourism Sector
Non-Profit Organizations""",

        # Program Structure and Specializations
        """Program Structure and Specialization Tracks:

Foundation Year (1st Year):
- Basic economics and business principles
- Mathematics and statistics foundation
- Computer applications and technology
- Management and organizational basics

Core Development (2nd Year):
- Financial accounting and business law
- Statistics and quantitative methods
- Micro and macroeconomics
- Business communication skills

Marketing Specialization (3rd Year):
- Marketing principles and management
- Organizational behavior and psychology
- Financial and managerial accounting
- Research methods and money systems
- Operations and production management

Professional Preparation (4th Year):
- Advanced marketing research
- International business strategies
- Strategic management
- Production and HR management
- Extensive marketing elective specialization

Specialization Tracks through Electives:
1. Digital Marketing: Social media, SEO, content marketing, web analytics
2. Brand Management: Brand strategy, product management, pricing, distribution
3. Market Research: Consumer behavior, research methods, analytics, CRM
4. Advertising and Promotion: Advertising management, PR, media planning, IMC
5. International Marketing: Global marketing, cross-cultural strategies, export marketing

Unique Program Features:
- Strong analytical and research foundation
- Integration of traditional and digital marketing
- Global marketing perspective
- Practical application through projects and case studies
- Preparation for diverse marketing career paths"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Economics and Administrative Sciences",
            "department": "Marketing",
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
            "content_type": "marketing_electives"
        },
        {
            "course_type": "core",
            "document_type": "course_description",
            "content_type": "marketing_core_courses"
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
    ids = [f"mkt_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Marketing curriculum documents to ChromaDB!")
        print("✅ Degree correctly set as: Bachelor of Science in Marketing")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["marketing management digital advertising brand"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_marketing_curriculum_to_chromadb()