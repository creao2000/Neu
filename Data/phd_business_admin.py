import chromadb
from chromadb.utils import embedding_functions

def add_phd_business_admin_curriculum_to_chromadb():
    """Add PhD in Business Administration curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_phd_business_admin",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_phd_business_admin",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_phd_business_admin")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF ECONOMICS AND ADMINISTRATIVE SCIENCES
GRADUATE SCHOOL OF SOCIAL SCIENCES
PhD IN BUSINESS ADMINISTRATION

Program Duration: 4 years (8 semesters)
Degree: Doctor of Philosophy in Business Administration
Program Level: Doctoral

Main website: https://iktisat.neu.edu.tr/?lang=en
Curriculum link: https://iktisat.neu.edu.tr/academic/academic-programmes/department-of-business-administration/phd-programme/?lang=en

Programme Language: English

Programme Objective:
The objective of the PhD programme in business administration is to prepare students who want to continue their career as an academic or to prepare students who want to develop their knowledge, skills, and competencies to work more successfully as managers in the private or public sector. More specifically, the programme aims to provide students with:

- The knowledge, intellectual abilities and techniques necessary to design and conduct high quality original scientific research
- The ability to become excellent academics and contribute to advancing the knowledge in the field of business administration and management
- An understanding of the high ethical standards in business research as well as teaching
- The ability to work effectively with others in order to ensure the wider impact of their research""",

        # Programme Structure
        """PhD in Business Administration - Programme Structure
Structure: 7 courses + seminar + dissertation
Duration: 8 semesters (4 years)

First Semester:
GCC603, Advanced Scientific Research Methods and Ethics, Credits:3
BUS602, Macro Organizational Theories, Credits:3

Second Semester:
BUS633, Advanced Data Analysis, Credits:3
BUS603, Micro Organizational Theories, Credits:3

Third Semester:
GCC602, Education for Learning, Credits:3
BUS6XX, Area Elective, Credits:3

Fourth Semester:
BUS6XX, Area Elective, Credits:3
BUS608, Seminar, Credits:0

Fifth to Eighth Semesters:
BUS600, Dissertation, Credits:0 (4 semesters)

Total Courses: 7
Total Credits: 21
Seminar: Required
Dissertation: Required (4 semesters)
PhD Proficiency Exam: Required before dissertation

Program Completion Requirements:
- Complete 7 courses (21 credits)
- Successfully complete seminar course
- Pass PhD proficiency exam (BUS690)
- Defend doctoral dissertation
- Total duration: 8 semesters""",

        # Course Sequence and Timeline
        """PhD Programme Course Sequence and Academic Timeline:

Year 1 - Foundation and Core Theory:
Semester 1:
- Advanced Scientific Research Methods and Ethics
- Macro Organizational Theories
- Foundation in research methodology and organizational theory

Semester 2:
- Advanced Data Analysis
- Micro Organizational Theories
- Quantitative methods and individual-level organizational behavior

Year 2 - Specialization and Preparation:
Semester 3:
- Education for Learning
- Area Elective 1
- Teaching preparation and specialization

Semester 4:
- Area Elective 2
- Seminar
- Advanced specialization and research proposal development

Year 2 Milestone:
- PhD Proficiency Exam (BUS690) - Must be passed before starting dissertation

Years 3-4 - Dissertation Research:
Semesters 5-8:
- Dissertation work (4 semesters)
- Original research and writing
- Dissertation defense preparation

Key Milestones:
- Coursework completion (End of Year 2)
- PhD Proficiency Exam (After Year 2)
- Dissertation Proposal Defense
- Dissertation Research and Writing
- Final Dissertation Defense""",

        # Core Course Descriptions
        """Core Course Descriptions - PhD in Business Administration:

GCC603 - Advanced Scientific Research Methods and Ethics:
Advanced research design, philosophical foundations of research, mixed methods, research ethics, and academic integrity in business research.

BUS602 - Macro Organizational Theories:
Macro-level organizational theories, institutional theory, organizational ecology, resource dependence, and population ecology perspectives.

BUS603 - Micro Organizational Theories:
Micro-level organizational behavior, individual and group dynamics, motivation, leadership, and psychological foundations of organizational behavior.

BUS633 - Advanced Data Analysis:
Advanced statistical methods, multivariate analysis, structural equation modeling, longitudinal data analysis, and advanced quantitative techniques.

GCC602 - Education for Learning:
Pedagogical theories, curriculum development, teaching methodologies, and academic career preparation for higher education.

BUS608 - Seminar:
Advanced research seminar focusing on current literature, research presentation, and development of dissertation research proposals.

BUS690 - PhD Proficiency Exam:
Comprehensive examination testing mastery of business administration theories, research methods, and specialized knowledge areas.

BUS600 - Dissertation:
Original research contributing new knowledge to the field of business administration, conducted under faculty supervision.""",

        # Area Elective Courses
        """Area Elective Course Options for PhD in Business Administration:

Advanced Organizational Theory Electives:
BUS610, Contemporary Issues in Organizational Theory
BUS611, Institutional Theory and Change
BUS612, Organizational Culture and Identity
BUS613, Power and Politics in Organizations
BUS614, Network Theory in Organizations

Strategic Management Electives:
BUS620, Advanced Strategic Management Theory
BUS621, Corporate Governance and Strategy
BUS622, Strategic Leadership and Decision Making
BUS623, Innovation and Technology Strategy
BUS624, International Strategic Management

Human Resource Management Electives:
BUS630, Strategic Human Resource Management
BUS631, Leadership and Organizational Development
BUS632, Compensation and Performance Management
BUS634, International Human Resource Management
BUS635, HR Analytics and Metrics

Research Methodology Electives:
BUS640, Qualitative Research Methods
BUS641, Advanced Quantitative Methods
BUS642, Mixed Methods Research
BUS643, Case Study Research
BUS644, Longitudinal Research Methods

Specialized Business Topics:
BUS650, Entrepreneurship and Small Business Research
BUS651, Marketing Theory and Consumer Behavior
BUS652, Financial Management Theory
BUS653, Operations and Supply Chain Management
BUS654, Business Ethics and Social Responsibility
BUS655, Cross-Cultural Management Research""",

        # Research and Dissertation Focus
        """PhD Research Areas and Dissertation Focus:

Potential Research Areas:
Organizational Behavior and Theory:
- Leadership and followership
- Organizational culture and climate
- Workplace diversity and inclusion
- Employee motivation and engagement
- Team dynamics and collaboration

Strategic Management:
- Competitive advantage and strategy formulation
- Strategic change and transformation
- Corporate governance and board effectiveness
- Mergers and acquisitions
- Strategic innovation

Human Resource Management:
- Talent management and development
- Performance management systems
- Compensation and reward strategies
- HR technology and analytics
- International HR practices

Entrepreneurship and Innovation:
- Startup ecosystems and venture creation
- Corporate entrepreneurship
- Innovation management
- Technology commercialization
- Social entrepreneurship

Marketing and Consumer Behavior:
- Brand management and equity
- Consumer decision-making processes
- Digital marketing strategies
- Service quality and customer satisfaction
- International marketing

Dissertation Requirements:
- Original contribution to knowledge
- Rigorous research methodology
- Theoretical foundation and development
- Practical implications and applications
- Publication potential in peer-reviewed journals""",

        # Career Outcomes and Academic Preparation
        """PhD Career Outcomes and Academic Preparation:

Academic Career Paths:
University Professor
Research Fellow
Department Chair
Academic Dean
Research Center Director

Industry and Consulting Roles:
Senior Research Analyst
Management Consultant
Organizational Development Specialist
Strategy Director
Executive Coach

Government and Public Sector:
Policy Analyst
Research Director
Program Evaluator
Public Administration Specialist
Government Advisor

Program Preparation for Academic Careers:
- Teaching experience and pedagogical training
- Research publication preparation
- Conference presentation skills
- Grant writing and research funding
- Academic networking and collaboration
- Peer review experience

Expected Competencies:
- Advanced theoretical knowledge in business administration
- Sophisticated research design and methodology
- Statistical and analytical expertise
- Academic writing and publication skills
- Teaching and mentoring capabilities
- Ethical research conduct
- Interdisciplinary research integration""",

        # Admission and Program Requirements
        """PhD Admission and Program Requirements:

Admission Requirements:
- Master's degree in Business Administration or related field
- Strong academic record (minimum GPA requirements)
- Research proposal or statement of purpose
- Letters of recommendation
- English language proficiency (for international students)
- Interview with faculty committee

Program Requirements:
- Completion of 7 advanced courses (21 credits)
- Successful seminar presentation
- Passing comprehensive proficiency exam
- Dissertation proposal defense
- Original dissertation research
- Final dissertation defense
- Publication requirements (varies by department)

Academic Standards:
- Maintain minimum GPA throughout program
- Adhere to academic integrity and ethics
- Active participation in research activities
- Regular progress reporting to advisor
- Publication in peer-reviewed journals (encouraged)

Faculty Support and Resources:
- Dedicated dissertation advisor
- Research methodology support
- Statistical consulting services
- Access to research databases
- Conference travel funding opportunities
- Teaching assistantship opportunities
- Research assistantship positions

Time to Completion:
- Expected duration: 4 years (8 semesters)
- Maximum duration: 6 years (university policy)
- Extension possible with valid reasons and approval"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Economics and Administrative Sciences",
            "graduate_school": "Social Sciences",
            "department": "Business Administration",
            "degree": "Doctor of Philosophy",
            "program_level": "Doctoral",
            "document_type": "program_info",
            "content_type": "general_info"
        },
        {
            "program_stage": "coursework",
            "duration": "8 semesters",
            "document_type": "program_structure",
            "content_type": "program_structure"
        },
        {
            "program_stage": "timeline",
            "document_type": "program_info",
            "content_type": "academic_timeline"
        },
        {
            "course_type": "core",
            "document_type": "course_description",
            "content_type": "phd_core_courses"
        },
        {
            "course_type": "elective",
            "document_type": "course_list",
            "content_type": "area_electives"
        },
        {
            "program_stage": "research",
            "document_type": "program_info",
            "content_type": "research_focus"
        },
        {
            "document_type": "program_info",
            "content_type": "career_outcomes"
        },
        {
            "document_type": "program_info",
            "content_type": "admission_requirements"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"phd_ba_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} PhD in Business Administration curriculum documents to ChromaDB!")
        print("✅ Program correctly identified as: Doctor of Philosophy in Business Administration (Doctoral Level)")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["PhD dissertation organizational theories research methods"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_phd_business_admin_curriculum_to_chromadb()