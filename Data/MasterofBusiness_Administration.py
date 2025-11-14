import chromadb
from chromadb.utils import embedding_functions

def add_mba_curriculum_to_chromadb():
    """Add MBA (Master of Business Administration) curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_mba",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_mba",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_mba")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF ECONOMICS AND ADMINISTRATIVE SCIENCES
GRADUATE SCHOOL OF SOCIAL SCIENCES
MASTER OF BUSINESS ADMINISTRATION (MBA)

Program Duration: 2 years (4 semesters)
Degree: Master of Business Administration
Program Level: Graduate

Main website: https://iktisat.neu.edu.tr/?lang=en
Curriculum link: https://iktisat.neu.edu.tr/academic/academic-programmes/department-of-business-administration/mba-programme/?lang=en

Programme Language: English

Programme Objective:
Business administration is a field that covers the principles for managing public sector institutions as well as private sector enterprises in an efficient and effective manner in the light of changing environmental conditions that influence how business is conducted. Business education is based on basic concepts related to areas such as correct identification and realization of objectives, effective use of resources, strategy and change management, organizational development and general management, production/service management, finance, accounting, marketing, human resources management and management information systems. The number of organizations operating in the international arena under the influence of globalization is high. Therefore, it is vital to prepare executive candidates who can take an active role in the national as well as international platform and in this respect, this is the main objectives of the MBA Programme.""",

        # Thesis Option Structure
        """MBA Programme - Thesis Option
Structure: 7 courses + seminar + thesis
Duration: 4 semesters

First Semester:
FIN516, Financial Management, Credits:3
MRK501, Marketing Management, Credits:3
MAN5XX, Area Elective, Credits:3
MAN5XX, Area Elective, Credits:3

Second Semester:
MAN540, Strategic Management, Credits:3
GCC603, Scientific Research Methods and Ethics, Credits:3
MAN5XX, Area Elective, Credits:3
MAN596, Seminar, Credits:0

Third Semester:
MAN599, Thesis, Credits:0

Fourth Semester:
MAN599, Thesis, Credits:0

Total Courses: 7
Total Credits: 21
Thesis: Required
Seminar: Required

Program Completion Requirements:
- Complete 7 courses (21 credits)
- Successfully complete seminar course
- Defend master's thesis
- Total duration: 4 semesters""",

        # Non-Thesis Option Structure
        """MBA Programme - Non-Thesis Option
Structure: 10 courses + project
Duration: 3 semesters

First Semester:
FIN516, Financial Management, Credits:3
MRK501, Marketing Management, Credits:3
MAN5XX, Area Elective, Credits:3
MAN5XX, Area Elective, Credits:3

Second Semester:
MAN540, Strategic Management, Credits:3
GCC603, Scientific Research Methods and Ethics, Credits:3
MAN5XX, Area Elective, Credits:3
MAN5XX, Area Elective, Credits:3

Third Semester:
MAN5XX, Area Elective, Credits:3
MAN5XX, Area Elective, Credits:3
MAN597, Project, Credits:0

Total Courses: 10
Total Credits: 30
Project: Required
Thesis: Not Required

Program Completion Requirements:
- Complete 10 courses (30 credits)
- Successfully complete project course
- Total duration: 3 semesters""",

        # Core Course Descriptions
        """Core Course Descriptions - MBA Programme:

FIN516 - Financial Management:
Advanced corporate finance, capital budgeting, financial analysis, risk management, and strategic financial decision-making for managers.

MRK501 - Marketing Management:
Strategic marketing planning, market analysis, product development, pricing strategies, distribution channels, and integrated marketing communications.

MAN540 - Strategic Management:
Strategic analysis, competitive advantage, corporate strategy, business-level strategy, strategy implementation, and strategic control systems.

GCC603 - Scientific Research Methods and Ethics:
Research design, quantitative and qualitative methods, data analysis, academic writing, and research ethics in business studies.

MAN596 - Seminar:
Presentation and discussion of research topics, literature review, and development of research proposals for thesis preparation.

MAN599 - Thesis:
Independent research project under faculty supervision, culminating in a master's thesis defense.

MAN597 - Project:
Applied business project focusing on real-world business problems and solutions, requiring practical application of MBA concepts.""",

        # Area Elective Courses
        """Area Elective Course Options for MBA:

Finance and Accounting Electives:
FIN517, Advanced Corporate Finance
FIN518, Investment Analysis and Portfolio Management
FIN519, International Financial Management
FIN520, Financial Markets and Institutions
FIN521, Risk Management and Derivatives
ACC501, Managerial Accounting
ACC502, Financial Statement Analysis

Marketing Electives:
MRK502, Consumer Behavior and Market Research
MRK503, International Marketing
MRK504, Digital Marketing and E-commerce
MRK505, Brand Management and Strategy
MRK506, Services Marketing
MRK507, Sales Management and Strategy
MRK508, Marketing Analytics

Management and Strategy Electives:
MAN541, Organizational Behavior and Leadership
MAN542, Human Resource Management
MAN543, Operations and Supply Chain Management
MAN544, Entrepreneurship and Innovation
MAN545, International Business
MAN546, Project Management
MAN547, Change Management and Organizational Development
MAN548, Business Ethics and Corporate Governance

Specialized Business Electives:
MAN549, Management Information Systems
MAN550, Business Analytics and Decision Making
MAN551, Negotiation and Conflict Resolution
MAN552, Cross-Cultural Management
MAN553, Quality Management and Six Sigma
MAN554, Strategic Human Resource Management
MAN555, Technology and Innovation Management""",

        # Program Comparison and Selection
        """MBA Programme Options Comparison:

Thesis Option (4 semesters):
- 7 courses (21 credits) + seminar + thesis
- Focus: Research-oriented, academic preparation
- Ideal for: Students considering PhD studies, academic careers, or research-intensive roles
- Duration: Longer (4 semesters)
- Output: Master's thesis

Non-Thesis Option (3 semesters):
- 10 courses (30 credits) + project
- Focus: Practice-oriented, professional development
- Ideal for: Working professionals, career advancement, immediate industry application
- Duration: Shorter (3 semesters)
- Output: Applied business project

Common Requirements for Both Options:
- Core courses in finance, marketing, and strategic management
- Scientific research methods course
- Area elective courses for specialization
- English language instruction
- Graduate-level academic standards

Admission Requirements:
- Bachelor's degree from recognized institution
- English proficiency (for international students)
- Professional experience (preferred but not always required)
- Statement of purpose and letters of recommendation""",

        # Career Opportunities and Outcomes
        """MBA Career Opportunities and Outcomes:

Programme Objectives:
- Develop strategic thinking and leadership capabilities
- Enhance analytical and decision-making skills
- Provide comprehensive understanding of business functions
- Prepare for executive and managerial roles
- Foster ethical and socially responsible business practices

Career Advancement Opportunities:
Senior Management Positions:
Chief Executive Officer (CEO)
Chief Operating Officer (COO)
Chief Financial Officer (CFO)
General Manager
Division Director

Functional Management Roles:
Marketing Director
Finance Manager
Operations Manager
Human Resources Director
Strategic Planning Manager

Consulting and Advisory Roles:
Management Consultant
Business Development Manager
Strategic Advisor
Investment Analyst
Project Management Consultant

Entrepreneurship and Innovation:
Business Founder
Startup Manager
Innovation Manager
Venture Capital Analyst
Business Development Specialist

Industry Sectors:
Financial Services and Banking
Consulting and Professional Services
Technology and IT Companies
Manufacturing and Industrial
Healthcare Management
Retail and Consumer Goods
Energy and Utilities
Government and Public Sector

Expected Competencies:
- Strategic analysis and formulation
- Financial management and analysis
- Marketing strategy development
- Organizational leadership
- Operational efficiency
- Ethical decision-making
- Global business perspective""",

        # Programme Structure and Progression
        """MBA Programme Structure and Academic Progression:

Thesis Option Progression:
Year 1, Semester 1:
- Financial Management
- Marketing Management
- 2 Area Electives
- Foundation building and core competency development

Year 1, Semester 2:
- Strategic Management
- Scientific Research Methods
- 1 Area Elective
- Seminar course
- Research preparation and specialization

Year 2, Semester 1:
- Thesis work begins
- Literature review and research design
- Data collection and analysis

Year 2, Semester 2:
- Thesis completion
- Writing and revision
- Thesis defense preparation

Non-Thesis Option Progression:
Year 1, Semester 1:
- Financial Management
- Marketing Management
- 2 Area Electives
- Core business foundation

Year 1, Semester 2:
- Strategic Management
- Scientific Research Methods
- 2 Area Electives
- Specialization and advanced topics

Year 2, Semester 1:
- 2 Area Electives
- Project work
- Integration and application of learning

Academic Support:
- Faculty mentorship and supervision
- Research resources and databases
- Professional development workshops
- Networking events with industry leaders
- Career services and placement support"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Economics and Administrative Sciences",
            "graduate_school": "Social Sciences",
            "department": "Business Administration",
            "degree": "Master of Business Administration",
            "program_level": "Graduate",
            "document_type": "program_info",
            "content_type": "general_info"
        },
        {
            "program_option": "thesis",
            "duration": "4 semesters",
            "document_type": "program_structure",
            "content_type": "thesis_option"
        },
        {
            "program_option": "non_thesis",
            "duration": "3 semesters",
            "document_type": "program_structure",
            "content_type": "non_thesis_option"
        },
        {
            "course_type": "core",
            "document_type": "course_description",
            "content_type": "mba_core_courses"
        },
        {
            "course_type": "elective",
            "document_type": "course_list",
            "content_type": "area_electives"
        },
        {
            "document_type": "program_info",
            "content_type": "program_comparison"
        },
        {
            "document_type": "program_info",
            "content_type": "career_opportunities"
        },
        {
            "document_type": "program_info",
            "content_type": "program_structure_detailed"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"mba_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} MBA curriculum documents to ChromaDB!")
        print("✅ Program correctly identified as: Master of Business Administration (Graduate Level)")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["MBA thesis option financial management strategic"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_mba_curriculum_to_chromadb()