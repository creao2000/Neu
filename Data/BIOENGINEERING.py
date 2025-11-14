import chromadb
from chromadb.utils import embedding_functions

def add_bioengineering_curriculum_to_chromadb():
    """Add Bioengineering curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_bioengineering",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_bioengineering",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_bioengineering")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF ENGINEERING
DEPARTMENT OF BIOENGINEERING
Bachelor of Science in Bioengineering

Program Duration: 4 years (8 semesters)
Degree: Bachelor of Science
Total ECTS for Graduation: 240
Total Credits: 143

Main website: https://muhendislik.neu.edu.tr/?lang=en
Curriculum link: https://muhendislik.neu.edu.tr/academic/academic-programmes/department-of-bioengineering/?lang=en

Legend:
PS = Problem Solving
C = Complementary
R = Reformative
T = Tutorial
LAB = Laboratory Hours
Practicum = Practical Hours""",

        # 1st Year - 1st Semester
        """First Year - First Semester (Fall) - Compulsory Courses:
PHY101, General Physics I, Credit:4, ECTS:6, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:2, C:1, R:1, T:1
MTH101, Calculus I, Credit:4, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practicum:0, PS:2, C:1, R:1, T:0
ENG101, English I, Credit:3, ECTS:5, Prerequisite: None, Class:0, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
BIOE101, Introduction to Bioengineering, Credit:3, ECTS:3, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:0, T:0
CHM104, Chemistry For Biological Sciences, Credit:4, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:2, C:2, R:0, T:0
ECC107, Biology, Credit:3, ECTS:3, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:0, R:0, T:1
YIT101, Turkish for Foreign Students I, Credit:2, ECTS:2, Prerequisite: None, Class:2, LAB:0, Practicum:0, PS:0, C:2, R:0, T:1
TUR101, Turkish Language I, Credit:2, ECTS:2, Prerequisite: None, Class:0, LAB:0, Practicum:0, PS:2, C:0, R:0, T:2
AIT101, Principles of Atatürk and the History of Turkish Revolution I, Credit:2, ECTS:2, Prerequisite: None, Class:2, LAB:0, Practicum:0, PS:0, C:2, R:0, T:1
AIT103, Principles of Atatürk and the History of Turkish Revolution I, Credit:2, ECTS:2, Prerequisite: None, Class:0, LAB:0, Practicum:0, PS:2, C:0, R:0, T:2

Total Semester: Credit:29, ECTS:36""",

        # 1st Year - 2nd Semester
        """First Year - Second Semester (Spring) - Compulsory Courses:
PHY102, General Physics II, Credit:4, ECTS:5, Prerequisite: PHY101, Class:3, LAB:2, Practicum:0, PS:2, C:2, R:1, T:0
MTH102, Calculus II, Credit:4, ECTS:5, Prerequisite: MTH101, Class:4, LAB:0, Practicum:0, PS:2, C:1, R:1, T:0
ENG102, English II, Credit:3, ECTS:5, Prerequisite: ENG101, Class:0, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
MTH113, Linear Algebra, Credit:3, ECTS:5, Prerequisite: MTH101, Class:3, LAB:0, Practicum:0, PS:2, C:0, R:1, T:0
CHM122, Organic Chemistry, Credit:4, ECTS:5, Prerequisite: CHM104, Class:3, LAB:2, Practicum:0, PS:2, C:2, R:0, T:0
YIT102, Turkish for Foreign Students II, Credit:2, ECTS:2, Prerequisite: YIT101, Class:2, LAB:0, Practicum:0, PS:0, C:2, R:0, T:1
TUR102, Turkish Language II, Credit:2, ECTS:2, Prerequisite: TUR101, Class:0, LAB:0, Practicum:0, PS:2, C:0, R:0, T:2
AIT102, Principles of Atatürk and the History of Turkish Revolution II, Credit:2, ECTS:2, Prerequisite: AIT101, Class:2, LAB:0, Practicum:0, PS:0, C:2, R:0, T:1
AIT104, Principles of Atatürk and the History of Turkish Revolution II, Credit:2, ECTS:2, Prerequisite: AIT103, Class:0, LAB:0, Practicum:0, PS:2, C:0, R:0, T:2

Total Semester: Credit:26, ECTS:33""",

        # 2nd Year - 1st Semester
        """Second Year - First Semester (Fall) - Compulsory Courses:
ECC217, Microbiology, Credit:3, ECTS:6, Prerequisite: ECC107, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:0, T:0
BME102, Biochemistry, Credit:4, ECTS:4, Prerequisite: CHM104, Class:3, LAB:1, Practicum:0, PS:0, C:1, R:1, T:2
ENG201, Academic English Writing Techniques II, Credit:3, ECTS:3, Prerequisite: ENG102, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
BIOE205, Principles and Applications of Ecology, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:0, R:0, T:1
NTE, Nontechnical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3

Total Semester: Credit:16, ECTS:24""",

        # 2nd Year - 2nd Semester
        """Second Year - Second Semester (Spring) - Compulsory Courses:
BIOE202, Polymer Technologies, Credit:3, ECTS:5, Prerequisite: CHM122, Class:3, LAB:0, Practicum:0, PS:2, C:0, R:1, T:0
BME250, Biostatistics, Credit:3, ECTS:4, Prerequisite: MTH101, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:0, T:0
BIOE200, Internship I, Credit:0, ECTS:6, Prerequisite: None, Class:0, LAB:0, Practicum:0, PS:0, C:0, R:0, T:0
BIOE204, Thermodynamics, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:0, R:1, T:0
BIOE208, Genetics, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:0, R:1, T:0
NTE, Nontechnical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3

Total Semester: Credit:15, ECTS:30""",

        # 3rd Year - 1st Semester
        """Third Year - First Semester (Fall) - Compulsory Courses:
BME202, Biomaterials, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:0, R:0, T:1
BME301, Biomedical Sensors, Credit:4, ECTS:6, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:2, C:1, R:1, T:0
ECC106, Introduction to Programming, Credit:4, ECTS:6, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:2, C:1, R:1, T:0
BME320, Biomechanics, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:0, T:0
BIOE301, Mass and Heat Transfer, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:0, T:0

Total Semester: Credit:17, ECTS:28""",

        # 3rd Year - 2nd Semester
        """Third Year - Second Semester (Spring) - Compulsory Courses:
BIOE302, Bioenergy Resources, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:0, T:0
BIOE304, Nanotechnology, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:0, T:0
BIOE306, System Design on Bioengineering, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:0, T:0
BME300, Internship II, Credit:0, ECTS:6, Prerequisite: None, Class:0, LAB:0, Practicum:0, PS:0, C:0, R:0, T:0
BME340, Modeling of Biological Systems, Credit:3, ECTS:5, Prerequisite: BME250, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
BME321, Artificial Organs, Credit:3, ECTS:4, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:0, R:0, T:1

Total Semester: Credit:15, ECTS:30""",

        # 4th Year - 1st Semester
        """Fourth Year - First Semester (Fall) - Compulsory Courses:
BIOE400, Graduation Project I, Credit:3, ECTS:10, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
BME401, Instrumental Analysis, Credit:4, ECTS:6, Prerequisite: None, Class:3, LAB:1, Practicum:0, PS:2, C:1, R:1, T:0
TE, Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0
TE, Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0
TE, Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0

Total Semester: Credit:16, ECTS:31""",

        # 4th Year - 2nd Semester
        """Fourth Year - Second Semester (Spring) - Compulsory Courses:
BIOE402, Graduation Project II, Credit:3, ECTS:10, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:1, R:1, T:1
BME435, Bioinformatics, Credit:3, ECTS:5, Prerequisite: BME250, Class:3, LAB:0, Practicum:0, PS:1, C:1, R:1, T:0
TE, Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0
TE, Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0
TE, Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0

Total Semester: Credit:15, ECTS:30

Program Total: Credit:143, ECTS:240""",

        # Technical Elective Courses
        """Technical Elective Courses (TE) - Bioengineering Specializations:
BME432, Fundamental Applications of Computed Tomography, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:0, T:0
BME443, Introduction to Tissue Engineering, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:0, T:0
BME333, Biomedical Computer Applications, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:0, T:0
BME405, Nuclear Medicine, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:0, T:0
BME409, Clinical Engineering, Credit:3, ECTS:5
BME304, Introduction to Nanotechnology, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:0, T:0
BME437, X-Ray Based Systems, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:0, T:0
BME453, Medical Ethics, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:0, T:0
BME458, Biomedical Equipment Design, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:0, T:0
BME482, Maintenance and Operation of Medical Devices, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:0, T:0
BME431, Cardiac Biomechanics and ECG Systems, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:0, T:0
BME407, Ultrasound Imaging, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:0, T:0
ECC413, Introduction to Artificial Intelligence, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:0, T:0
ECC419, Digital Image Processing, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:2, C:1, R:0, T:0
ECC426, Economics for Engineers, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:2, C:1, R:1, T:1
ECC427, Management for Engineers, Credit:3, ECTS:6, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:2, C:1, R:1, T:1""",

        # Restricted Non-Technical Elective Courses
        """Restricted Non-Technical Elective Courses (NTE):
MAN101, Introduction to Management, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:2, R:0, T:0
ECON101, Introduction to Economics, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:1, C:2, R:0, T:0
FRE101, French I, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:2, R:1, T:2
FRE102, French II, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:2, R:1, T:2
GER101, German I, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practicum:0, PS:0, C:2, R:1, T:2
GER102, German II, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:0, C:2, R:2, T:2
ARB101, Arabic, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:0, C:2, R:2, T:2
GRE101, Greek, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:0, C:2, R:2, T:2
RUS101, Russian, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:0, C:2, R:2, T:2
DBT301, Debate Club, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:0, C:2, R:2, T:2
PHIL101, Introduction to Philosophy, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:0, C:2, R:0, T:2
HIST103, History of Civilization, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:0, C:2, R:0, T:2
POL101, Political Science I, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:0, C:2, R:0, T:2
SOC101, Sociology, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practicum:0, PS:0, C:2, R:0, T:2""",

        # Program Summary and Career Opportunities
        """Bioengineering Program Summary:
Degree: Bachelor of Science in Bioengineering
Duration: 4 years (8 semesters)
Total Credits: 143
Total ECTS: 240

Program Focus Areas:
- Biomaterials and Polymer Technologies
- Biomedical Sensors and Instrumentation
- Biomechanics and Artificial Organs
- Bioenergy and Environmental Applications
- Nanotechnology in Bioengineering
- Bioinformatics and Computational Biology
- Medical Imaging and Diagnostics
- Tissue Engineering and Regenerative Medicine
- Ecological Applications of Bioengineering

Career Opportunities:
Bioengineer
Biomedical Engineer
Biomaterials Engineer
Biomechanics Engineer
Bioenergy Specialist
Environmental Bioengineer
Research and Development Engineer
Medical Device Designer
Quality Control Engineer
Process Engineer in Biotech
Academic and Research Positions
Regulatory Affairs Specialist

Professional Recognition:
Graduates are qualified to work in biomedical companies, biotechnology firms, pharmaceutical companies, research institutions, environmental agencies, and healthcare organizations worldwide."""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Engineering",
            "department": "Bioengineering",
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
    ids = [f"bioengineering_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Bioengineering curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["bioengineering biomaterials nanotechnology"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_bioengineering_curriculum_to_chromadb()