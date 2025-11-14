import chromadb
from chromadb.utils import embedding_functions

def add_petroleum_gas_engineering_curriculum_to_chromadb():
    """Add Petroleum and Natural Gas Engineering curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_petroleum_gas_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_petroleum_gas_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_petroleum_gas_engineering")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF ENGINEERING
DEPARTMENT OF PETROLEUM AND NATURAL GAS ENGINEERING
Bachelor of Science in Petroleum and Natural Gas Engineering

Program Duration: 4 years (8 semesters)
Degree: Bachelor of Science
Total ECTS for Graduation: 240
Total Credits: 149

Main website: https://muhendislik.neu.edu.tr/?lang=en
Curriculum link: https://muhendislik.neu.edu.tr/academic/academic-programmes/department-of-petroleum-and-natural-gas-engineering/?lang=en

Legend:
PS = Problem Solving
C = Complementary
R = Reformative
T = Tutorial
LAB = Laboratory Hours
Practicum = Practical Hours""",

        # 1st Year - 1st Semester
        """First Year - First Semester (Fall) - Compulsory Courses:
CHM101, General Chemistry, Credit:4, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:0, C:2, R:2, T:1
ENG101, English I, Credit:3, ECTS:3, Prerequisite: None, Class:0, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
MTH101, Mathematics I, Credit:4, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practicum:0, PS:2, C:1, R:1, T:0
PGE101, Introduction to Petroleum Engineering, Credit:3, ECTS:4, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
PHY101, General Physics I, Credit:4, ECTS:5, Prerequisite: None, Class:4, LAB:2, Practicum:0, PS:2, C:1, R:1, T:0
ECC101, Introduction to Programming, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:1, Practicum:0, PS:2, C:1, R:1, T:0
YIT101/TUR101, Turkish for Foreign Students I/Turkish Language I, Credit:2, ECTS:2, Prerequisite: None, Class:2, LAB:0, Practicum:0, PS:0, C:2, R:0, T:1

Total Semester: Credit:23, ECTS:30""",

        # 1st Year - 2nd Semester
        """First Year - Second Semester (Spring) - Compulsory Courses:
CHM102, Physical Chemistry, Credit:3, ECTS:6, Prerequisite: CHM101, Class:3, LAB:0, Practicum:0, PS:3, C:1, R:1, T:1
ENG102, English II, Credit:3, ECTS:3, Prerequisite: ENG101, Class:0, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
MTH102, Mathematics II, Credit:4, ECTS:6, Prerequisite: MTH101, Class:4, LAB:0, Practicum:0, PS:2, C:1, R:1, T:0
PHY102, General Physics II, Credit:4, ECTS:5, Prerequisite: PHY101, Class:4, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
TDE102, Technical Drawing, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
YIT102/TUR102, Turkish for Foreign Students II/Turkish Language II, Credit:2, ECTS:2, Prerequisite: YIT101/TUR101, Class:2, LAB:0, Practicum:0, PS:0, C:2, R:0, T:1
AIT103/AIT101, Principles of Ataturk and the History of Turkish Revolution I, Credit:2, ECTS:2, Prerequisite: None, Class:2, LAB:0, Practicum:0, PS:0, C:2, R:0, T:1

Total Semester: Credit:21, ECTS:30""",

        # 2nd Year - 1st Semester
        """Second Year - First Semester (Fall) - Compulsory Courses:
ECC207, Thermodynamics, Credit:4, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practicum:0, PS:2, C:1, R:1, T:0
ECC211, Engineering Materials, Credit:4, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practicum:0, PS:2, C:1, R:1, T:1
MTH201, Differential Equations, Credit:4, ECTS:6, Prerequisite: MTH102, Class:4, LAB:0, Practicum:0, PS:2, C:1, R:1, T:0
PGE201, General Geology, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:1, Practicum:0, PS:1, C:1, R:1, T:1
PGE221, Engineering Mechanics, Credit:3, ECTS:5, Prerequisite: PHY101, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
AIT104/AIT102, Principles of Ataturk and the History of Turkish Revolution II, Credit:2, ECTS:2, Prerequisite: AIT103/AIT101, Class:2, LAB:0, Practicum:0, PS:0, C:2, R:0, T:1

Total Semester: Credit:20, ECTS:30""",

        # 2nd Year - 2nd Semester
        """Second Year - Second Semester (Spring) - Compulsory Courses:
PGE202, Petroleum Geology, Credit:3, ECTS:5, Prerequisite: PGE201, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE204, Applied Mathematics for Petroleum Engineers, Credit:3, ECTS:5, Prerequisite: MTH101, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE218, Rock Properties, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE220, Fluid Properties, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
ECC213, Strength of Materials, Credit:3, ECTS:5, Prerequisite: PGE221, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
NTE, Non-Technical Elective, Credit:3, ECTS:3, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:0, R:0, T:0

Total Semester: Credit:18, ECTS:30""",

        # 3rd Year - 1st Semester
        """Third Year - First Semester (Fall) - Compulsory Courses:
PGE300, Summer Practice I, Credit:0, ECTS:4, Prerequisite: None, Class:0, LAB:0, Practicum:0, PS:0, C:0, R:0, T:0
PGE301, Introduction to Fluid Mechanics, Credit:4, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practicum:0, PS:2, C:1, R:1, T:0
PGE303, Petroleum Production Engineering I, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE305, Petroleum Reservoir Engineering I, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:0, R:2, T:1
PGE307, Drilling Engineering I, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0
MTH309, Statistics and Probability for Petroleum Engineers, Credit:3, ECTS:5, Prerequisite: MTH102, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0

Total Semester: Credit:16, ECTS:30""",

        # 3rd Year - 2nd Semester
        """Third Year - Second Semester (Spring) - Compulsory Courses:
PGE304, Petroleum Production Engineering II, Credit:3, ECTS:5, Prerequisite: PGE303, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE306, Petroleum Reservoir Engineering II, Credit:3, ECTS:5, Prerequisite: PGE305, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE308, Drilling Engineering II, Credit:4, ECTS:5, Prerequisite: PGE307, Class:4, LAB:0, Practicum:0, PS:2, C:1, R:1, T:0
PGE310, Oil and Gas Pipeline System, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE312, Well Logging, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
UTE, Unrestricted Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3

Total Semester: Credit:19, ECTS:30""",

        # 4th Year - 1st Semester
        """Fourth Year - First Semester (Fall) - Compulsory Courses:
PGE400, Summer Practice II, Credit:0, ECTS:4, Prerequisite: PGE300, Class:0, LAB:0, Practicum:0, PS:0, C:0, R:0, T:0
PGE403, Natural Gas Engineering, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE405, Petroleum Engineering Design, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:0, T:1
PGE411, Petroleum Property Valuation, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
TE, Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3
TE, Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3

Total Semester: Credit:15, ECTS:30""",

        # 4th Year - 2nd Semester
        """Fourth Year - Second Semester (Spring) - Compulsory Courses:
PGE402, Graduation Project, Credit:3, ECTS:5, Prerequisite: PGE405, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
ECC426, Economics For Engineering, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
TE, Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3
TE, Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3
TE, Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3
TE, Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3

Total Semester: Credit:18, ECTS:30

Program Total: Credit:149, ECTS:240""",

        # Technical Elective Courses
        """Technical Elective Courses (TE) - Petroleum and Natural Gas Engineering Specializations:
PGE407, Reservoir Characterization, Credit:3, ECTS:5, Prerequisite: PGE305, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE408, Geophysics for Petroleum Engineers, Credit:3, ECTS:5, Prerequisite: PGE201, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE409, Process Control and Instrumentation, Credit:3, ECTS:5, Prerequisite: ECC207, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE413, Globalization and Petroleum Politics, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE416, Environmental Control in Petroleum Engineering Operations, Credit:3, ECTS:5, Prerequisite: PGE303, PGE307, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE417, Petroleum and Natural Refining Processes, Credit:3, ECTS:5, Prerequisite: ECC207, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE418, Oil Transportation and Storage, Credit:3, ECTS:5, Prerequisite: PGE301, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE419, Health and Safety for Oil Industry, Credit:3, ECTS:5, Prerequisite: PGE303, PGE307, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE420, Project Management, Credit:3, ECTS:5, Prerequisite: PGE303, PGE305, PGE307, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE421, Introduction to Geothermal Reservoir Engineering, Credit:3, ECTS:5, Prerequisite: ECC207, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE422, Enhanced Oil Recovery, Credit:3, ECTS:5, Prerequisite: PGE303, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE423, Pressure Control, Credit:3, ECTS:5, Prerequisite: PGE307, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE424, Physical and Engineering Properties of Rock, Credit:3, ECTS:5, Prerequisite: PGE201, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
PGE425, Directional Drilling, Credit:3, ECTS:5, Prerequisite: PGE307, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE426, Petroleum Geochemistry, Credit:3, ECTS:5, Prerequisite: ECC207, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE427, Well Stimulation, Credit:3, ECTS:5, Prerequisite: PGE303, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE428, Transportation and Storage of Natural Gas, Credit:3, ECTS:5, Prerequisite: PGE301, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE429, Well Design Control, Credit:3, ECTS:5, Prerequisite: PGE307, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE430, Hydrocarbon Geophysics, Credit:3, ECTS:5, Prerequisite: PGE202, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE431, Geological Maps and Cartography, Credit:3, ECTS:5, Prerequisite: PGE201, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE432, Safety & Environmental Protection, Credit:3, ECTS:5, Prerequisite: PGE303, PGE307, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE433, Well Design, Credit:3, ECTS:5, Prerequisite: PGE303, PGE307, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE434, Individual Study, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE435, Petroleum Fuels Market & Segment, Credit:3, ECTS:5, Prerequisite: PGE303, PGE305, PGE307, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE436, Simulating of Geosystems, Credit:3, ECTS:5, Prerequisite: MTH201, Class:2, LAB:1, Practicum:0, PS:0, C:1, R:1, T:1
PGE437, Well Test Analysis, Credit:3, ECTS:5, Prerequisite: PGE306, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
PGE438, Special Operations in Drilling, Credit:3, ECTS:5, Prerequisite: PGE308, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:1
PGE439, LPG Technology and Sector, Credit:3, ECTS:5, Prerequisite: PGE305, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:1""",

        # Program Summary and Career Opportunities
        """Petroleum and Natural Gas Engineering Program Summary:
Degree: Bachelor of Science in Petroleum and Natural Gas Engineering
Duration: 4 years (8 semesters)
Total Credits: 149
Total ECTS: 240

Program Focus Areas:
- Drilling Engineering and Operations
- Reservoir Engineering and Characterization
- Production Engineering and Optimization
- Natural Gas Engineering and Processing
- Petroleum Geology and Geophysics
- Well Logging and Formation Evaluation
- Enhanced Oil Recovery Techniques
- Pipeline and Transportation Systems
- Health, Safety and Environmental Management
- Petroleum Economics and Project Management

Career Opportunities:
Petroleum Engineer
Drilling Engineer
Reservoir Engineer
Production Engineer
Natural Gas Engineer
Well Logging Engineer
Petroleum Geologist
Pipeline Engineer
Project Manager
Field Engineer
Research and Development Engineer
Academic and Research Positions

Professional Recognition:
Graduates are qualified to work in oil and gas companies, energy corporations, consulting firms, research institutions, and government agencies worldwide."""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Engineering",
            "department": "Petroleum and Natural Gas Engineering",
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
            "document_type": "program_info",
            "content_type": "program_summary_careers"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"petroleum_gas_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Petroleum and Natural Gas Engineering curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["petroleum drilling reservoir engineering"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_petroleum_gas_engineering_curriculum_to_chromadb()