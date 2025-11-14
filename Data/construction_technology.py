import chromadb
from chromadb.utils import embedding_functions

def add_construction_technology_curriculum_to_chromadb():
    """Add Construction Technology Department curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_construction_technology",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_construction_technology",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_construction_technology")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF CIVIL AND ENVIRONMENTAL ENGINEERING
DEPARTMENT OF CONSTRUCTION TECHNOLOGY
Associate Degree in Construction Technology

Program Duration: 2 years (4 semesters)
Degree: Associate Degree
Total ECTS for Graduation: 120
Total Credits: 76

Main website: https://insaatvecevre.neu.edu.tr/?lang=en
Curriculum link: https://insaatvecevre.neu.edu.tr/wp-content/uploads/sites/136/2023/11/23/Insaat-ve-Cevre-Muhendisligi-Fakultesi-Insaat-Teknolojisi-MYO-2-TR-DONEMLIK.pdf

Legend:
Z = Compulsory Course (Zorunlu)
S = Elective Course (Seçmeli)
T = Theoretical Hours
P = Practical Hours
K = Credit (Kredi)
A = ECTS Credits (AKTS)""",

        # 1st Semester
        """First Year - First Semester - Compulsory Courses:
İNG101, English I, Z, T:2, P:2, K:3, A:3
MAT101, Mathematics I, Z, T:2, P:2, K:3, A:3
TR101, Technical Drawing, Z, T:2, P:2, K:3, A:5
İNT144, Construction Materials, Z, T:2, P:2, K:3, A:5
İNT121, Statics, Z, T:3, P:0, K:3, A:5
BİL101, Computer and Office Applications, Z, T:2, P:2, K:3, A:4
AİT101, Atatürk's Principles and Revolutionary History I, Z, T:2, P:0, K:2, A:2
KAM100, Campus Orientation, Z, T:0, P:0, K:0, A:0

Total: T:15, P:8, K:20, ECTS:27""",

        # 2nd Semester
        """First Year - Second Semester - Compulsory Courses:
İNG102, English II, Z, T:2, P:2, K:3, A:3
MAT102, Mathematics II, Z, T:2, P:2, K:3, A:3
TR102, Computer Aided Drawing, Z, T:2, P:2, K:3, A:5
İNT104, Surveying I, Z, T:2, P:3, K:3, A:5
İNT122, Strength of Materials, Z, T:3, P:0, K:3, A:5
İNT145, Concrete Technology I, Z, T:2, P:2, K:3, A:5
TUR101, Turkish Language I, Z, T:2, P:0, K:2, A:2
KAR100, Career Planning, Z, T:0, P:0, K:0, A:2

Total: T:15, P:9, K:20, ECTS:30""",

        # 3rd Semester
        """Second Year - Third Semester - Compulsory Courses:
İNT251, Highway Construction, Z, T:3, P:0, K:3, A:5
İNT284, Steel Construction, Z, T:3, P:0, K:3, A:5
İNT271, Hydraulics and Hydrology, Z, T:2, P:2, K:3, A:5
İNT281, Reinforced Concrete I, Z, T:2, P:2, K:3, A:5
İNT201, Computer Aided Design I, Z, T:2, P:2, K:3, A:5
İNT261, Soil Mechanics I, Z, T:2, P:2, K:3, A:5
İNT200, Summer Practice, Z, T:0, P:0, K:0, A:0

Total: T:14, P:6, K:18, ECTS:30""",

        # 4th Semester
        """Second Year - Fourth Semester - Compulsory Courses:
İNT233, Quantity Surveying and Cost Estimation, Z, T:2, P:2, K:3, A:5
İNT231, Construction Management, Z, T:2, P:2, K:3, A:5
İNT262, Soil Mechanics II, Z, T:2, P:2, K:3, A:5
İNT282, Reinforced Concrete II, Z, T:2, P:2, K:3, A:5
İNT245, Concrete Technology II, Z, T:2, P:2, K:3, A:5
İNT236, Occupational Health and Safety in Construction Works, Z, T:3, P:0, K:3, A:5

Total: T:13, P:8, K:18, ECTS:30""",

        # Course Descriptions - Technical Courses
        """Course Descriptions - Technical Construction Courses:

İNT144 - Construction Materials:
Study of building materials including concrete, steel, wood, and composites. Material properties, testing methods, and quality control.

İNT121 - Statics:
Fundamental principles of statics, force systems, equilibrium, centroids, and moments of inertia for construction applications.

İNT122 - Strength of Materials:
Stress and strain analysis, mechanical properties of materials, bending, torsion, and deflection of structural elements.

İNT145 - Concrete Technology I:
Concrete composition, mixing, placing, curing, and testing. Properties of fresh and hardened concrete.

TR101 - Technical Drawing:
Basic technical drawing principles, orthographic projections, sections, and dimensioning for construction.

TR102 - Computer Aided Drawing:
CAD software applications for construction drawings, 2D and basic 3D modeling.

İNT104 - Surveying I:
Basic surveying principles, leveling, distance measurement, and basic surveying equipment operation.

BİL101 - Computer and Office Applications:
Computer fundamentals, word processing, spreadsheets, and presentation software for construction documentation.""",

        # Course Descriptions - Advanced Technical Courses
        """Course Descriptions - Advanced Technical Courses:

İNT251 - Highway Construction:
Highway design principles, earthworks, pavement construction, drainage systems, and construction methods.

İNT284 - Steel Construction:
Steel structural systems, connections, fabrication, erection procedures, and design considerations.

İNT271 - Hydraulics and Hydrology:
Fluid mechanics principles, pipe flow, open channel flow, hydrologic cycle, and drainage design.

İNT281 - Reinforced Concrete I:
Reinforced concrete design fundamentals, beam design, slab design, and construction detailing.

İNT201 - Computer Aided Design I:
Advanced CAD applications for structural design, building information modeling basics.

İNT261 - Soil Mechanics I:
Soil properties, classification, compaction, permeability, and basic foundation principles.

İNT233 - Quantity Surveying and Cost Estimation:
Measurement of construction works, quantity take-off, cost estimation, and bidding procedures.

İNT231 - Construction Management:
Project planning, scheduling, resource management, quality control, and construction supervision.

İNT262 - Soil Mechanics II:
Advanced soil mechanics, slope stability, earth pressure, and foundation design principles.

İNT282 - Reinforced Concrete II:
Advanced reinforced concrete design, columns, foundations, and structural systems.

İNT245 - Concrete Technology II:
Advanced concrete technology, mix design, special concretes, and quality control systems.

İNT236 - Occupational Health and Safety:
Construction safety regulations, hazard identification, risk assessment, and safety management.""",

        # Program Summary and Career Opportunities
        """Construction Technology Program Summary:
Degree: Associate Degree in Construction Technology
Duration: 2 years (4 semesters)
Total Credits: 76
Total ECTS: 120
Percentage of Electives: 7%

Program Focus Areas:
- Construction Materials and Methods
- Structural Systems and Design
- Construction Management
- Surveying and CAD Applications
- Concrete Technology
- Occupational Health and Safety

Core Competencies Developed:
- Technical drawing and CAD skills
- Construction material testing and quality control
- Structural analysis and design basics
- Construction project management
- Quantity surveying and cost estimation
- Occupational health and safety practices
- Field surveying and measurement

Career Opportunities:
Construction Technician
Site Supervisor
Quality Control Technician
CAD Technician
Surveying Assistant
Construction Inspector
Cost Estimator
Safety Officer
Concrete Technician
Construction Materials Tester
Project Coordinator

Industry Sectors:
Construction Companies
Engineering Consultancy Firms
Government Construction Departments
Construction Material Suppliers
Testing Laboratories
Infrastructure Development Companies
Real Estate Development Companies
Municipal Construction Departments

Further Education Pathways:
- Bachelor's degree completion in Civil Engineering
- Bachelor's degree in Construction Management
- Advanced diplomas in specialized construction fields""",

        # Program Structure and Practical Components
        """Program Structure and Practical Components:

Year 1 - Foundation:
- Basic mathematics and technical drawing
- Construction materials and statics
- Computer applications and surveying
- Language and general education

Year 2 - Specialization:
- Structural systems (concrete and steel)
- Construction management and cost estimation
- Advanced technical courses
- Summer practical training

Practical Training Components:
- Summer practice between 2nd and 3rd semesters
- Laboratory work in materials testing
- CAD and technical drawing workshops
- Field surveying exercises
- Construction site visits

Technical Skills Development:
- AutoCAD and CAD software proficiency
- Construction material testing
- Structural detailing
- Quantity surveying
- Construction safety procedures
- Project documentation

Graduate Profile:
Graduates are technical professionals capable of assisting engineers in construction projects, supervising construction activities, conducting quality control tests, and managing construction documentation.""",

        # Comparison with 4-year Civil Engineering
        """Comparison with 4-year Civil Engineering Program:

Construction Technology (2-year):
- Focus on practical applications and field work
- Technical and supervisory roles
- Associate degree level
- Direct entry to workforce
- 76 credits, 120 ECTS

Civil Engineering (4-year):
- Focus on engineering design and analysis
- Engineering and management roles
- Bachelor's degree level
- Professional engineering qualification
- 158+ credits, 240 ECTS

Career Path Differences:
Construction Technology Graduates:
- Construction Technician
- Site Supervisor
- Quality Control Inspector
- CAD Operator

Civil Engineering Graduates:
- Civil Engineer
- Project Manager
- Structural Designer
- Consulting Engineer

Articulation Opportunities:
Construction Technology graduates can continue to:
- Bachelor's in Civil Engineering (with bridging courses)
- Bachelor's in Construction Management
- Advanced technical certifications"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Civil and Environmental Engineering",
            "department": "Construction Technology",
            "degree": "Associate",
            "duration": "2 years",
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
            "course_type": "technical",
            "document_type": "course_description",
            "content_type": "basic_technical_courses"
        },
        {
            "course_type": "technical",
            "document_type": "course_description",
            "content_type": "advanced_technical_courses"
        },
        {
            "document_type": "program_info",
            "content_type": "program_summary_careers"
        },
        {
            "document_type": "program_info",
            "content_type": "program_structure"
        },
        {
            "document_type": "program_info",
            "content_type": "program_comparison"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"ct_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Construction Technology curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["construction materials concrete technology"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_construction_technology_curriculum_to_chromadb()