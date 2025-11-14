import chromadb
from chromadb.utils import embedding_functions

def add_hr_management_curriculum_to_chromadb():
    """Add Human Resource Management curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_hr_management",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_hr_management",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_hr_management")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF ECONOMICS AND ADMINISTRATIVE SCIENCES
DEPARTMENT OF HUMAN RESOURCE MANAGEMENT
Bachelor of Science in Human Resource Management

Program Duration: 4 years (8 semesters)
Degree: Bachelor of Science
Total ECTS for Graduation: 240

Main website: https://iktisat.neu.edu.tr/?lang=en
Curriculum link: https://iktisat.neu.edu.tr/academic/academic-programmes/department-of-human-resource-management/courses/?lang=en

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
MRK308, Marketing Communication, C, Credit:3, ECTS:6, Hours:3
EAS206, Introduction to Law, C, Credit:3, ECTS:6, Hours:3
AİT101/103, Atatürk's Principles I/Principles of Atatürk I, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:32, Hours:17""",

        # 2nd Year - 2nd Semester
        """Second Year - Second Semester - Compulsory Courses:
MAN202, Communication for Business II, C, Credit:3, ECTS:6, Hours:3
EAS204, Financial Accounting II, C, Credit:3, ECTS:6, Hours:3
MTH262, Statistics II, C, Credit:3, ECTS:6, Hours:3
SOC100, Sociology, C, Credit:3, ECTS:6, Hours:3
EAS207, Business Law, C, Credit:3, ECTS:6, Hours:3
AİT102/104, Atatürk's Principles II/Principles of Atatürk II, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:32, Hours:17""",

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
MRK307, Consumer Behaviour, C, Credit:3, ECTS:6, Hours:3
EAS402, Human Resource Management, C, Credit:3, ECTS:6, Hours:3
EAS302, Financial Management, C, Credit:3, ECTS:6, Hours:3
EAS405, Production Management, C, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 4th Year - 1st Semester
        """Fourth Year - First Semester - Compulsory Courses:
EAS304, Marketing Management, C, Credit:3, ECTS:6, Hours:3
EAS307, Research Methods, C, Credit:3, ECTS:6, Hours:3
MRK304, Marketing and Society, C, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 4th Year - 2nd Semester
        """Fourth Year - Second Semester - Compulsory Courses:
EAS403, Marketing Research, C, Credit:3, ECTS:6, Hours:3
MRK412, Digital Marketing, C, Credit:3, ECTS:6, Hours:3
MRK423, Marketing Strategy, C, Credit:3, ECTS:6, Hours:3
MRK402, International Marketing, C, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # Elective Courses
        """Elective Course Options for Human Resource Management:

HR Specialization Electives:
EAS406, Recruitment and Selection
EAS407, Training and Development
EAS408, Performance Management
EAS409, Compensation and Benefits
EAS410, Labor Relations
EAS411, Strategic Human Resource Management
EAS412, International Human Resource Management
EAS413, HR Analytics and Metrics

Organizational Behavior Electives:
EAS414, Leadership and Motivation
EAS415, Organizational Development
EAS416, Change Management
EAS417, Conflict Management and Negotiation
EAS418, Team Dynamics
EAS419, Corporate Culture
EAS420, Ethics in Human Resources

Business and Management Electives:
EAS421, Strategic Management
EAS422, Project Management
EAS423, Entrepreneurship
EAS424, Business Ethics
EAS425, Management Information Systems
EAS426, Quality Management
EAS427, Supply Chain Management

Psychology and Sociology Electives:
EAS428, Industrial and Organizational Psychology
EAS429, Social Psychology in Organizations
EAS430, Cross-Cultural Management
EAS431, Workplace Diversity
EAS432, Occupational Health and Safety
EAS433, Career Development

Special Topics:
EAS434, HR Information Systems
EAS435, Talent Management
EAS436, Employer Branding
EAS437, HR in Digital Transformation
EAS438, HR Consulting
EAS439, HR Internship and Case Studies""",

        # Core Course Descriptions
        """Core Course Descriptions - Human Resource Management Focus:

EAS310 - Organizational Behaviour:
Individual and group behavior in organizations, motivation, leadership, communication, and organizational culture.

EAS402 - Human Resource Management:
Fundamental HR functions including recruitment, selection, training, performance management, and compensation.

EAS308 - Operations Research and Management:
Quantitative methods for business decision-making, optimization techniques, and operational efficiency.

MRK307 - Consumer Behaviour:
Psychological and sociological factors influencing consumer decision-making and buying behavior.

EAS301/302 - Business Finance & Financial Management:
Financial principles, capital budgeting, financial analysis, and corporate financial decision-making.

EAS303 - Managerial Accounting:
Cost analysis, budgeting, performance measurement, and accounting information for management decisions.

EAS305 - Principles of Marketing:
Marketing concepts, market analysis, product development, pricing, distribution, and promotion strategies.

EAS307 - Research Methods:
Research design, data collection methods, statistical analysis, and research reporting for business.

EAS403 - Marketing Research:
Market research techniques, data analysis, and application of research findings to marketing decisions.

MRK324 - Approaches to Psychology in Marketing:
Psychological principles applied to marketing strategies, consumer perception, and decision processes.

EAS405 - Production Management:
Operations management, production planning, quality control, and supply chain management.""",

        # Program Summary and Career Opportunities
        """Human Resource Management Program Summary:
Degree: Bachelor of Science in Human Resource Management
Duration: 4 years (8 semesters)
Total ECTS: 240
Language of Instruction: English

Program Focus Areas:
- Human Resource Management Functions
- Organizational Behavior and Psychology
- Business Management and Strategy
- Marketing and Consumer Behavior
- Financial and Managerial Accounting
- Research Methods and Analytics
- Operations and Production Management

Core Competencies Developed:
- HR recruitment, selection, and training processes
- Performance management and compensation systems
- Organizational behavior analysis
- Business communication and negotiation skills
- Financial and managerial decision-making
- Marketing strategy and consumer analysis
- Research methods and data analysis
- Operations and production management

Career Opportunities:
Human Resources Specialist
Recruitment Officer
Training and Development Coordinator
Compensation and Benefits Analyst
HR Business Partner
Talent Acquisition Specialist
Organizational Development Consultant
Performance Management Specialist
Labor Relations Specialist
HR Analytics Specialist
Recruitment Consultant
Training Manager
HR Project Coordinator

Professional Settings:
Corporate HR Departments
Recruitment and Staffing Agencies
Consulting Firms
Government Agencies
Non-Profit Organizations
Educational Institutions
Healthcare Organizations
Manufacturing Companies
Service Industry
Technology Companies
Financial Institutions""",

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
- Marketing communication
- Sociology and organizational context

HR Specialization (3rd Year):
- Organizational behavior and psychology
- Human resource management principles
- Financial and managerial accounting
- Marketing and consumer behavior
- Operations and production management

Professional Preparation (4th Year):
- Advanced marketing management
- Research methods and marketing research
- Digital and international marketing
- Strategic HR and management
- Extensive elective specialization

Specialization Tracks:
1. Strategic HR Management: Recruitment, training, performance management, compensation
2. Organizational Development: Organizational behavior, change management, leadership
3. HR Analytics: Research methods, data analysis, metrics, decision support
4. Talent Management: Recruitment, development, retention, career planning

Unique Program Features:
- Integration of HR with business management
- Strong foundation in organizational psychology
- Marketing and consumer behavior perspective
- Quantitative and analytical skill development
- Preparation for strategic HR roles in modern organizations"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Economics and Administrative Sciences",
            "department": "Human Resource Management",
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
            "content_type": "elective_courses"
        },
        {
            "course_type": "core",
            "document_type": "course_description",
            "content_type": "hr_core_courses"
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
    ids = [f"hrm_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Human Resource Management curriculum documents to ChromaDB!")
        print("✅ Degree correctly set as: Bachelor of Science in Human Resource Management")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["human resources organizational behavior recruitment"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_hr_management_curriculum_to_chromadb()