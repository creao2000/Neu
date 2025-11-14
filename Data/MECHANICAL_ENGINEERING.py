import chromadb
from chromadb.utils import embedding_functions

def add_mechanical_engineering_curriculum_to_chromadb():
    """Add Mechanical Engineering curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_mechanical_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_mechanical_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_mechanical_engineering")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF ENGINEERING
DEPARTMENT OF MECHANICAL ENGINEERING
Bachelor of Science in Mechanical Engineering

Program Duration: 4 years (8 semesters)
Degree: Bachelor of Science
Total ECTS for Graduation: 240
Total Credits: 140

Main website: https://muhendislik.neu.edu.tr/?lang=en
Curriculum link: https://muhendislik.neu.edu.tr/academic/academic-programmes/department-of-mechanical-engineering/?lang=en

Legend:
PS = Problem Solving
C = Complementary
R = Reformative
T = Tutorial
LAB = Laboratory Hours
Practicum = Practical Hours""",

        # 1st Year - 1st Semester
        """First Year - First Semester (Fall) - Compulsory Courses:
CHM101, General Chemistry, Credit:4, ECTS:6, Prerequisite: None, Class:4, LAB:2, Practicum:0, PS:2, C:1, R:1, T:0
ENG101, English I, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
MTH101, Mathematics I, Credit:4, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practicum:0, PS:0, C:2, R:0, T:1
PHY101, General Physics I, Credit:4, ECTS:6, Prerequisite: None, Class:4, LAB:2, Practicum:0, PS:3, C:1, R:1, T:1
ECC103, Engineering Drawing I, Credit:3, ECTS:7, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:2, R:1, T:1

Total Semester: Credit:18, ECTS:30""",

        # 1st Year - 2nd Semester
        """First Year - Second Semester (Spring) - Compulsory Courses:
ME104, Introduction to Mechanical Engineering, Credit:2, ECTS:6, Prerequisite: None, Class:2, LAB:0, Practicum:0, PS:2, C:1, R:1, T:0
ENG102, English II, Credit:3, ECTS:5, Prerequisite: ENG101, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:1, T:0
MTH102, Mathematics II, Credit:4, ECTS:6, Prerequisite: MTH101, Class:4, LAB:0, Practicum:0, PS:2, C:1, R:1, T:0
PHY102, General Physics II, Credit:4, ECTS:6, Prerequisite: PHY101, Class:4, LAB:2, Practicum:2, PS:0, C:2, R:0, T:1
ECC101, Introduction to Computers and Programming, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:0, C:1, R:1, T:1
YIT101, Turkish for Foreign Students I, Credit:2, ECTS:2, Prerequisite: None, Class:2, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1

Total Semester: Credit:18, ECTS:30""",

        # 2nd Year - 1st Semester
        """Second Year - First Semester (Fall) - Compulsory Courses:
MTH201, Differential Equations, Credit:4, ECTS:6, Prerequisite: MTH102, Class:4, LAB:0, Practicum:0, PS:2, C:1, R:1, T:2
ECC206, Statics, Credit:4, ECTS:6, Prerequisite: PHY101, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
ECC207, Thermodynamics I, Credit:4, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:2, R:0, T:1
ECC211, Engineering Materials, Credit:4, ECTS:7, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
ENG201, English III, Credit:3, ECTS:5, Prerequisite: ENG102, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:1, T:0

Total Semester: Credit:19, ECTS:30""",

        # 2nd Year - 2nd Semester
        """Second Year - Second Semester (Spring) - Compulsory Courses:
MTH232, Mathematics for Engineers, Credit:3, ECTS:5, Prerequisite: MTH101, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
ECC222, Manufacturing Technology, Credit:4, ECTS:6, Prerequisite: ECC211, Class:3, LAB:0, Practicum:2, PS:1, C:1, R:1, T:0
ECC208, Thermodynamics II, Credit:3, ECTS:5, Prerequisite: ECC207, Class:3, LAB:0, Practicum:1, PS:0, C:2, R:0, T:1
ECC212, Dynamics, Credit:3, ECTS:5, Prerequisite: PHY101, Class:3, LAB:0, Practicum:0, PS:0, C:0, R:0, T:0
ECC224, Strength of Materials, Credit:4, ECTS:6, Prerequisite: ECC206, Class:4, LAB:0, Practicum:0, PS:1, C:1, R:1, T:1
ME200, Workshop Training, Credit:0, ECTS:1, Prerequisite: ECC222, Class:0, LAB:0, Practicum:0, PS:2, C:1, R:1, T:1
YIT102, Turkish for Foreign Students II, Credit:2, ECTS:2, Prerequisite: YIT101, Class:2, LAB:0, Practicum:0, PS:2, C:2, R:1, T:1

Total Semester: Credit:19, ECTS:30""",

        # 3rd Year - 1st Semester
        """Third Year - First Semester (Fall) - Compulsory Courses:
ECC304, Fluid Mechanics I, Credit:4, ECTS:7, Prerequisite: MTH201, Class:4, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
ECC307, Machine Design I, Credit:4, ECTS:7, Prerequisite: ECC224, Class:4, LAB:0, Practicum:0, PS:1, C:0, R:2, T:1
ECC317, Principles of CAE, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:0, C:1, R:1, T:1
FNTE, Free Non-Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:1, T:1
MTH323, Numerical Analysis, Credit:3, ECTS:6, Prerequisite: MTH102, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0

Total Semester: Credit:17, ECTS:30""",

        # 3rd Year - 2nd Semester
        """Third Year - Second Semester (Spring) - Compulsory Courses:
ECC214, Electrical Machinery, Credit:3, ECTS:5, Prerequisite: PHY102, Class:3, LAB:0, Practicum:0, PS:2, C:2, R:0, T:1
ECC308, Machine Design II, Credit:4, ECTS:6, Prerequisite: ECC307, Class:4, LAB:0, Practicum:0
ECC310, Control Systems, Credit:3, ECTS:5, Prerequisite: MTH201, Class:3, LAB:0, Practicum:0, PS:0, C:0, R:0, T:0
ECC314, Dynamics of Machine Systems, Credit:4, ECTS:6, Prerequisite: ECC212, Class:3, LAB:0, Practicum:0, PS:1, C:0, R:1, T:1
ECC316, Heat Transfer, Credit:4, ECTS:6, Prerequisite: MTH201, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:1, T:1
ME300, Industrial Training, Credit:0, ECTS:2, Prerequisite: ME200, Class:0, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1

Total Semester: Credit:18, ECTS:30""",

        # 4th Year - 1st Semester
        """Fourth Year - First Semester (Fall) - Compulsory Courses:
ECC424, Experimental Analysis of Mechanical Engineering Systems, Credit:3, ECTS:8, Prerequisite: None, Class:3, LAB:0, Practicum:0
TE, Technical Elective, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0
TE, Technical Elective, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0
TE, Technical Elective, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0
ME427, Engineering Ethics, Credit:2, ECTS:2, Prerequisite: None, Class:2, LAB:0, Practicum:0, PS:2, C:1, R:1, T:0
AIT103, Atatürk's Principles and Reform I, Credit:2, ECTS:2, Prerequisite: None, Class:2, LAB:2, Practicum:0, PS:0, C:2, R:2, T:1

Total Semester: Credit:16, ECTS:30""",

        # 4th Year - 2nd Semester
        """Fourth Year - Second Semester (Spring) - Compulsory Courses:
ME400, Graduation Project, Credit:4, ECTS:8, Prerequisite: None, Class:3, LAB:0, Practicum:0
TE, Technical Elective, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0
TE, Technical Elective, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0
RNTE, Restricted Non-Technical Elective, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0
ME450, Power Plant Training, Credit:0, ECTS:2, Prerequisite: ME300, Class:0, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
AIT104, Atatürk's Principles and Reform II, Credit:2, ECTS:2, Prerequisite: AIT103, Class:2, LAB:0, Practicum:0, PS:2, C:1, R:1, T:0

Total Semester: Credit:15, ECTS:30

Program Total: Credit:140, ECTS:240""",

        # Technical Elective Courses
        """Technical Elective Courses (TE) - 4th Year:
ME401, Hydraulic Machinery, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
ME411, Heating, Ventilating, Air Conditioning & Cooling System, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
ME416, Solar Energy, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
ME418, Refrigeration Techniques, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
ECC425, Internal Combustion Engines, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
ME423, Heat Exchanger Design, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
ME425, Machine Tools & Tool Design, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
ME426, Introduction to Finite Elements, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:2, T:0
ME429, Computer Aided Design, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
ME431, Energy Conversion Systems, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:1, T:0
ME433, Mass Transfer, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:1, T:1
ME441, Fluid Mechanics II, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
ME442, Gas Dynamics, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
ME453, Materials Engineering, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:2, T:0
ECC433, Heat Treatment, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:2, T:1
ME461, Hoisting and Conveying Machines, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:2, R:1, T:0
ECC434, Quality Control, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:2, R:1, T:0
ECC481, Sheet Metal Processes and Mould Design, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:2, R:1, T:0
ECC483, Reverse Engineering Methods, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:2, R:1, T:0""",

        # Restricted Non-Technical Elective Courses
        """Restricted Non-Technical Elective Courses (RNTE):
ECC426, Economics for Engineers, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:2, R:2, T:0
ECC427, Management for Engineers, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:2, R:2, T:0""",

        # Program Summary and Career Opportunities
        """Mechanical Engineering Program Summary:
Degree: Bachelor of Science in Mechanical Engineering
Duration: 4 years (8 semesters)
Total Credits: 140
Total ECTS: 240

Program Focus Areas:
- Thermodynamics and Heat Transfer
- Fluid Mechanics and Hydraulics
- Machine Design and Dynamics
- Manufacturing Technology
- Materials Engineering
- Control Systems and Automation
- Energy Systems and Conversion
- Computer-Aided Engineering
- Finite Element Analysis
- Mechanical Systems Design

Career Opportunities:
Mechanical Design Engineer
Thermal Systems Engineer
Manufacturing Engineer
Project Engineer
Research and Development Engineer
Quality Control Engineer
Maintenance Engineer
Energy Systems Engineer
Automotive Engineer
Aerospace Engineer
Consulting Engineer
Academic and Research Positions

Professional Recognition:
Graduates are qualified to work in various industries including automotive, aerospace, energy, manufacturing, construction, and consulting firms worldwide."""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Engineering",
            "department": "Mechanical Engineering",
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
            "elective_type": "technical",
            "document_type": "course_list",
            "content_type": "technical_electives"
        },
        {
            "course_type": "elective",
            "elective_type": "non_technical",
            "document_type": "course_list",
            "content_type": "restricted_non_technical_electives"
        },
        {
            "document_type": "program_info",
            "content_type": "program_summary_careers"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"mechanical_eng_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Mechanical Engineering curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["thermodynamics mechanical engineering"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_mechanical_engineering_curriculum_to_chromadb()