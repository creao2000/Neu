import chromadb
from chromadb.utils import embedding_functions

def add_economics_curriculum_to_chromadb():
    """Add Economics curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_economics",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_economics",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_economics")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF ECONOMICS AND ADMINISTRATIVE SCIENCES
DEPARTMENT OF ECONOMICS
Bachelor of Science in Economics

Program Duration: 4 years (8 semesters)
Degree: Bachelor of Science
Total ECTS for Graduation: 240

Main website: https://iktisat.neu.edu.tr/?lang=en
Curriculum link: https://iktisat.neu.edu.tr/academic/academic-programmes/department-of-economics/courses/?lang=en

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
SOC100, Sociology, C, Credit:3, ECTS:6, Hours:3
AİT102/104, Atatürk's Principles II/Principles of Atatürk II, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:32, Hours:17""",

        # 3rd Year - 1st Semester
        """Third Year - First Semester - Compulsory Courses:
ECON304, Econometrics, C, Credit:3, ECTS:6, Hours:3
ECON305, History of Economic Thought, C, Credit:3, ECTS:6, Hours:3
EAS306, Money and Banking, C, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 3rd Year - 2nd Semester
        """Third Year - Second Semester - Compulsory Courses:
ECON308, Industrial Economics and Management, C, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 4th Year - 1st Semester
        """Fourth Year - First Semester - Compulsory Courses:
ECON401, International Economics, C, Credit:3, ECTS:6, Hours:3
ECON409, Economics of Development, C, Credit:3, ECTS:6, Hours:3
ECON414, European Economy, C, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 4th Year - 2nd Semester
        """Fourth Year - Second Semester - Compulsory Courses:
ECON402, World Economy, C, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3
Elective Course, E, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # Elective Courses
        """Elective Course Options for Economics:

Economic Theory and Analysis Electives:
ECON301, Advanced Microeconomics
ECON302, Advanced Macroeconomics
ECON303, Mathematical Economics
ECON306, Game Theory
ECON307, Behavioral Economics
ECON309, Public Economics
ECON310, Labor Economics

Applied Economics Electives:
ECON311, Environmental Economics
ECON312, Health Economics
ECON313, Urban Economics
ECON315, Agricultural Economics
ECON316, Transport Economics
ECON317, Energy Economics
ECON318, Education Economics

Finance and Banking Electives:
ECON319, Financial Economics
ECON320, Monetary Economics
ECON321, International Finance
ECON322, Banking and Financial Institutions
ECON323, Investment Analysis
ECON324, Risk Management

Policy and Development Electives:
ECON325, Economic Policy Analysis
ECON326, Development Economics
ECON327, Comparative Economic Systems
ECON328, Turkish Economy
ECON329, Middle East Economics
ECON330, Transition Economics

Research and Quantitative Methods:
ECON331, Economic Research Methods
ECON332, Time Series Analysis
ECON333, Applied Econometrics
ECON334, Economic Forecasting
ECON335, Data Analysis for Economics""",

        # Core Course Descriptions
        """Core Course Descriptions - Economics Focus:

ECON304 - Econometrics:
Application of statistical methods to economic data, regression analysis, hypothesis testing, and economic modeling.

ECON305 - History of Economic Thought:
Evolution of economic theories from classical to modern schools, major economists and their contributions.

EAS306 - Money and Banking:
Monetary systems, central banking, financial intermediation, money supply, and monetary policy.

ECON308 - Industrial Economics and Management:
Market structures, firm behavior, industrial organization, and business strategy in economic context.

ECON401 - International Economics:
International trade theory, trade policies, exchange rates, balance of payments, and global economic integration.

ECON409 - Economics of Development:
Economic growth theories, development strategies, poverty analysis, and development policy in developing countries.

ECON414 - European Economy:
Structure and performance of European economies, EU economic policies, and economic integration processes.

ECON402 - World Economy:
Global economic systems, international economic institutions, and contemporary global economic issues.

EAS201 - Microeconomics:
Individual economic behavior, market mechanisms, consumer theory, production, and market structures.

EAS202 - Macroeconomics:
Aggregate economic analysis, national income, inflation, unemployment, and macroeconomic policies.

MTH261/262 - Statistics I & II:
Probability theory, statistical inference, regression analysis, and quantitative methods for economics.""",

        # Program Summary and Career Opportunities
        """Economics Program Summary:
Degree: Bachelor of Science in Economics
Duration: 4 years (8 semesters)
Total ECTS: 240
Language of Instruction: English

Program Focus Areas:
- Economic Theory and Analysis
- Quantitative Methods and Econometrics
- International Economics
- Development Economics
- Monetary Economics
- Industrial Economics
- Economic Policy Analysis

Core Competencies Developed:
- Economic modeling and analysis
- Statistical and econometric techniques
- Policy evaluation and formulation
- Quantitative research methods
- Critical thinking and problem-solving
- Data analysis and interpretation
- Understanding of global economic systems

Career Opportunities:
Economic Analyst
Policy Analyst
Research Economist
Data Analyst
Financial Analyst
Economic Consultant
Development Specialist
International Trade Specialist
Central Bank Analyst
Government Economist
Academic Researcher
Risk Analyst
Market Research Analyst

Professional Settings:
Government Ministries and Agencies
Central Banks and Financial Institutions
International Organizations (IMF, World Bank, UN)
Research Institutes and Think Tanks
Consulting Firms
Financial Services Industry
Corporate Strategy Departments
Non-Governmental Organizations
Academic Institutions
Statistical Agencies""",

        # Program Structure and Specializations
        """Program Structure and Specialization Tracks:

Foundation Year (1st Year):
- Basic economic principles
- Mathematics and statistics foundation
- Business and management fundamentals
- Computer applications and technology

Core Development (2nd Year):
- Advanced micro and macroeconomics
- Financial accounting principles
- Statistical methods and analysis
- Business communication and law

Specialization (3rd Year):
- Econometrics and quantitative methods
- History of economic thought
- Money and banking systems
- Industrial economics
- Extensive elective course selection

Professional Preparation (4th Year):
- International and development economics
- European and world economy studies
- Advanced economic theory
- Professional skill development through electives

Specialization Tracks:
1. Economic Theory and Analysis: Advanced micro/macro, mathematical economics, game theory
2. Applied Economics: Environmental, health, labor, urban economics
3. International Economics: Trade, finance, development, global economic systems
4. Quantitative Economics: Econometrics, forecasting, data analysis, research methods

Unique Program Features:
- Strong quantitative and analytical focus
- Integration of theory and applied economics
- Emphasis on econometric and statistical methods
- Global economic perspective
- Preparation for both academic and professional careers"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Economics and Administrative Sciences",
            "department": "Economics",
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
            "content_type": "economics_core_courses"
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
    ids = [f"econ_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Economics curriculum documents to ChromaDB!")
        print("✅ Degree correctly set as: Bachelor of Science in Economics")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["econometrics microeconomics macroeconomics"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_economics_curriculum_to_chromadb()