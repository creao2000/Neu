import chromadb
from chromadb.utils import embedding_functions

def add_materials_nanotechnology_curriculum_to_chromadb():
    """Add Materials Science and Nanotechnology Engineering curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_materials_nanotechnology_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_materials_nanotechnology_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_materials_nanotechnology_engineering")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF ENGINEERING
DEPARTMENT OF MATERIALS SCIENCE AND NANOTECHNOLOGY ENGINEERING
Bachelor of Science in Materials Science and Nanotechnology Engineering

Program Duration: 4 years (8 semesters)
Degree: Bachelor of Science
Total ECTS for Graduation: 240
Total Credits: 149

Main website: https://muhendislik.neu.edu.tr/?lang=en
Curriculum link: https://muhendislik.neu.edu.tr/academic/academic-programmes/department-of-materials-science-and-nanotechnology-engineering/?lang=en

Legend:
PS = Problem Solving
C = Complementary
R = Reformative
T = Tutorial
LAB = Laboratory Hours
Practicum = Practical Hours""",

        # 1st Year - 1st Semester
        """First Year - First Semester (Fall) - Compulsory Courses:
PHY101, General Physics I, Credit:4, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:2, C:1, R:1, T:1
CHM101, General Chemistry I, Credit:4, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:0, C:2, R:2, T:1
MTH101, Calculus I, Credit:4, ECTS:5, Prerequisite: None, Class:4, LAB:0, Practicum:0, PS:2, C:1, R:1, T:0
ENG101, English I, Credit:3, ECTS:5, Prerequisite: None, Class:0, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
ECC103, Technical Drawing I, Credit:3, ECTS:5, Prerequisite: None, Class:4, LAB:0, Practicum:0, PS:0, C:0, R:0, T:4
MSN101, Introduction to Materials Science and Nanotechnology Engineering, Credit:2, ECTS:3, Prerequisite: None, Class:2, LAB:0, Practicum:0, PS:0, C:1, R:0, T:2
YIT101, Turkish for Foreign Students I, Credit:2, ECTS:2, Prerequisite: None, Class:2, LAB:0, Practicum:0, PS:0, C:2, R:0, T:1
TUR101, Turkish Language I, Credit:2, ECTS:2, Prerequisite: None, Class:0, LAB:0, Practicum:0, PS:2, C:0, R:0, T:2

Total Semester: Credit:24, ECTS:32""",

        # 1st Year - 2nd Semester
        """First Year - Second Semester (Spring) - Compulsory Courses:
PHY102, General Physics II, Credit:4, ECTS:5, Prerequisite: PHY101, Class:3, LAB:2, Practicum:0, PS:2, C:2, R:1, T:0
MTH102, Calculus II, Credit:4, ECTS:5, Prerequisite: MTH101, Class:4, LAB:0, Practicum:0, PS:2, C:1, R:1, T:0
CHM122, Organic Chemistry, Credit:3, ECTS:5, Prerequisite: CHM101, Class:3, LAB:1, Practicum:0, PS:0, C:1, R:1, T:2
ENG102, English II, Credit:3, ECTS:3, Prerequisite: ENG101, Class:0, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
ECC101, Computer Programming, Credit:3, ECTS:5, Prerequisite: None, Class:4, LAB:1, Practicum:0, PS:3, C:1, R:1, T:0
YIT102, Turkish for Foreign Students II, Credit:2, ECTS:2, Prerequisite: YIT101, Class:2, LAB:0, Practicum:0, PS:0, C:2, R:0, T:1
TUR102, Turkish Language II, Credit:2, ECTS:2, Prerequisite: TUR101, Class:0, LAB:0, Practicum:0, PS:2, C:0, R:0, T:2
CHM112, General Chemistry II, Credit:4, ECTS:5, Prerequisite: CHM101, Class:3, LAB:2, Practicum:0, PS:0, C:2, R:2, T:1

Total Semester: Credit:25, ECTS:32""",

        # 2nd Year - 1st Semester
        """Second Year - First Semester (Fall) - Compulsory Courses:
MTH201, Differential Equations, Credit:4, ECTS:5, Prerequisite: MTH102, Class:4, LAB:0, Practicum:0, PS:2, C:2, R:0, T:0
ENG201, Communication Skills, Credit:3, ECTS:3, Prerequisite: ENG102, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
AIT101, Atatürk Principles and the History of Turkish Revolution I, Credit:2, ECTS:2, Prerequisite: None, Class:2, LAB:0, Practicum:0, PS:0, C:2, R:0, T:1
AIT103, Principles of Atatürk and the History of Turkish Revolution I, Credit:2, ECTS:2, Prerequisite: None, Class:0, LAB:0, Practicum:0, PS:2, C:0, R:0, T:2
MSN201, Material Sciences I, Credit:3, ECTS:5, Prerequisite: CHM101, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:2
MSN203, Foundations of Nanotechnology, Credit:3, ECTS:5, Prerequisite: MSN101/CHM112, Class:3, LAB:0, Practicum:0, PS:0, C:2, R:2, T:1
CHM201, Inorganic Chemistry, Credit:3, ECTS:5, Prerequisite: CHM112, Class:3, LAB:0, Practicum:0, PS:0, C:2, R:2, T:1
MSN205, Physical Chemistry and Thermodynamics, Credit:3, ECTS:5, Prerequisite: CHM112/MTH102, Class:3, LAB:0, Practicum:0, PS:0, C:2, R:2, T:1

Total Semester: Credit:23, ECTS:32""",

        # 2nd Year - 2nd Semester
        """Second Year - Second Semester (Spring) - Compulsory Courses:
AIT102, Principles of Atatürk and Recent Turkish History II, Credit:2, ECTS:2, Prerequisite: AIT101, Class:2, LAB:0, Practicum:0, PS:0, C:2, R:0, T:1
AIT104, Principles of Atatürk and the History of Turkish Revolution II, Credit:2, ECTS:2, Prerequisite: AIT103, Class:0, LAB:0, Practicum:0, PS:2, C:0, R:0, T:2
MSN200, Summer Practice I, Credit:0, ECTS:1, Prerequisite: None, Class:2, LAB:0, Practicum:0, PS:0, C:2, R:0, T:1
MSN202, Material Sciences II, Credit:3, ECTS:5, Prerequisite: MSN201, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:2
MSN204, Mechanics of Nanomaterials, Credit:3, ECTS:5, Prerequisite: MSN201, Class:4, LAB:0, Practicum:2, PS:2, C:2, R:0, T:2
MSN206, Materials for Biological and Medical Applications, Credit:3, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practicum:0, PS:2, C:1, R:1, T:0
MSN208, Nanomaterials, Credit:3, ECTS:6, Prerequisite: CHM101/PHY101, Class:3, LAB:1, Practicum:0, PS:0, C:1, R:1, T:2
PHY201, Introduction to Quantum Physics, Credit:3, ECTS:6, Prerequisite: MTH201/PHY102, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1

Total Semester: Credit:19, ECTS:33""",

        # 3rd Year - 1st Semester
        """Third Year - First Semester (Fall) - Compulsory Courses:
MSN301, Synthesis and Fabrication of Nanoengineering Systems, Credit:4, ECTS:6, Prerequisite: MSN202, Class:4, LAB:0, Practicum:0, PS:2, C:1, R:1, T:0
MSN307, Crystallography of Materials, Credit:3, ECTS:6, Prerequisite: MSN201, Class:4, LAB:0, Practicum:2, PS:3, C:2, R:1, T:0
MSN309, Research Skills in Science, Credit:3, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practicum:0, PS:2, C:1, R:1, T:0
MSN303, Introduction to Solid State Chemistry, Credit:3, ECTS:6, Prerequisite: CHM112, Class:3, LAB:0, Practicum:0, PS:0, C:3, R:1, T:0
MSN305, Phase Transformations and Kinetics, Credit:3, ECTS:6, Prerequisite: CHM112, Class:3, LAB:0, Practicum:0, PS:0, C:3, R:1, T:0

Total Semester: Credit:16, ECTS:30""",

        # 3rd Year - 2nd Semester
        """Third Year - Second Semester (Spring) - Compulsory Courses:
MSN302, Materials Selection in Engineering Design, Credit:3, ECTS:5, Prerequisite: MSN202, Class:3, LAB:0, Practicum:0, PS:1, C:0, R:1, T:1
MSN304, Nanomaterials and Production Methods, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:2
MSN306, Instrumental Methods for Materials Science and Nanoengineering, Credit:4, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practicum:0, PS:0, C:1, R:1, T:2
MSN308, Composite Materials, Credit:3, ECTS:6, Prerequisite: None, Class:4, LAB:2, Practicum:0, PS:1, C:1, R:1, T:2
TOSD-1, Nontechnical Electives, Credit:3, ECTS:6, Prerequisite: None, Class:3
MSN300, Summer Practice II, Credit:0, ECTS:1, Prerequisite: None, Class:0, LAB:0, Practicum:0, PS:0, C:0, R:0, T:0

Total Semester: Credit:16, ECTS:30""",

        # 4th Year - 1st Semester
        """Fourth Year - First Semester (Fall) - Compulsory Courses:
MSN401, Characterization of Nanoengineering Systems, Credit:3, ECTS:6, Prerequisite: None, Class:2, LAB:3, Practicum:0, PS:0, C:1, R:1, T:2
MSN403, Experimental Methods in Materials Science, Credit:3, ECTS:6, Prerequisite: MSN201, Class:3, LAB:1, Practicum:0, PS:0, C:1, R:1, T:2
TOSD-2, Nontechnical Elective Course, Credit:3, ECTS:6, Prerequisite: None, Class:3
BSD-1, Elective Courses, Credit:3, ECTS:4, Prerequisite: None
BSD-2, Elective Courses, Credit:3, ECTS:4, Prerequisite: None
BSD-3, Elective Courses, Credit:3, ECTS:4, Prerequisite: None

Total Semester: Credit:18, ECTS:30""",

        # 4th Year - 2nd Semester
        """Fourth Year - Second Semester (Spring) - Compulsory Courses:
MSN400, Graduation Project, Credit:4, ECTS:12, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
TOSD-3, Nontechnical Elective Course, Credit:3, ECTS:6, Prerequisite: None, Class:3
BSD-4, Elective Courses, Credit:3, ECTS:4, Prerequisite: None, Class:4, LAB:0, Practicum:0, PS:1, C:2, R:1, T:0
BSD-5, Elective Courses, Credit:3, ECTS:4, Prerequisite: None
BSD-6, Elective Courses, Credit:3, ECTS:4, Prerequisite: None

Total Semester: Credit:16, ECTS:30

Program Total: Credit:149, ECTS:240""",

        # Technical Elective Courses
        """Technical Elective Courses (BSD) - Materials Science and Nanotechnology Specializations:
MSN451, Surface Science, Credit:3, ECTS:4, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
MSN452, Polymeric Engineering Materials, Credit:3, ECTS:4, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:2, C:1, R:1, T:1
MSN453, Introduction to Biomaterials, Credit:3, ECTS:4, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
MSN454, Materials Science of Energy Technologies, Credit:3, ECTS:4, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
MSN455, Fundamentals of Solar Cells, Credit:3, ECTS:4, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
MSN456, Materials Science of Thin Films, Credit:3, ECTS:4, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
MSN457, Micro and Nano Structural Materials and Devices, Credit:3, ECTS:4, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
MSN458, Advanced Technology Materials, Credit:3, ECTS:4, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
MSN459, Electrical, Dielectric, and Magnetic Properties of Engineering Materials, Credit:3, ECTS:4, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:1, C:1, R:2, T:1
ME453, Material Engineering, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:2, C:1, R:1, T:1
ECC433, Heat Treatment, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:2, C:1, R:1, T:1
EE432, Mechatronics, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:2, C:1, R:1, T:1
ECC419, Image Processing, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
BME448, Micro and Nano Technologies in Biomedical Engineering, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:2, C:1, R:1, T:1
ECC427, Management for Engineering, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:2, R:2, T:0
ECC426, Economics for Engineering, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:2, R:2, T:0""",

        # Restricted Non-Technical Elective Courses
        """Restricted Non-Technical Elective Courses (TOSD):
FRE101, French I, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
FRE102, French II, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
GER101, German I, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
GER102, German II, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:1, C:1, R:2, T:1
POL101, Political Science I, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:2, C:1, R:1, T:1
SOC101, Sociology, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
GRE101, Greek, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:1, C:1, R:2, T:1
ARB101, Arabic, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:2, C:1, R:1, T:1
RUS101, Russian, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:2, C:1, R:1, T:1
DBT301, Debate Club, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1""",

        # Program Summary and Career Opportunities
        """Materials Science and Nanotechnology Engineering Program Summary:
Degree: Bachelor of Science in Materials Science and Nanotechnology Engineering
Duration: 4 years (8 semesters)
Total Credits: 149
Total ECTS: 240

Program Focus Areas:
- Nanomaterials Synthesis and Characterization
- Materials Science and Engineering
- Solid State Chemistry and Physics
- Materials for Energy Applications
- Biomaterials and Medical Applications
- Composite Materials and Polymers
- Surface Science and Thin Films
- Materials Characterization Techniques
- Quantum Physics Applications

Career Opportunities:
Materials Engineer
Nanotechnology Engineer
Research and Development Engineer
Quality Control Engineer
Process Engineer
Materials Scientist
Product Development Engineer
Biomaterials Specialist
Energy Materials Engineer
Academic and Research Positions
Manufacturing Engineer

Professional Recognition:
Graduates are qualified to work in materials manufacturing, nanotechnology companies, research institutions, biomedical industries, energy sectors, and various high-tech industries worldwide."""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Engineering",
            "department": "Materials Science and Nanotechnology Engineering",
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
            "content_type": "non_technical_electives"
        },
        {
            "document_type": "program_info",
            "content_type": "program_summary_careers"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"materials_nano_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Materials Science and Nanotechnology Engineering curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["nanomaterials materials science characterization"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_materials_nanotechnology_curriculum_to_chromadb()