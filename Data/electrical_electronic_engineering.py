import chromadb
from chromadb.utils import embedding_functions

def add_electrical_electronic_engineering_curriculum_to_chromadb():
    """Add Electrical and Electronic Engineering curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_electrical_electronic_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_electrical_electronic_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_electrical_electronic_engineering")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF ENGINEERING
DEPARTMENT OF ELECTRICAL AND ELECTRONIC ENGINEERING
Bachelor of Science in Electrical and Electronic Engineering

Program Duration: 4 years (8 semesters)
Degree: Bachelor of Science
Total ECTS for Graduation: 253
Total Credits: 152

Main website: https://muhendislik.neu.edu.tr/?lang=en
Curriculum link: https://muhendislik.neu.edu.tr/academic/academic-programmes/department-of-electrical-and-electronic-engineering/?lang=en

Legend:
PS = Problem Solving
C = Complementary
R = Reformative
T = Tutorial
LAB = Laboratory Hours
Practical = Practical Hours""",

        # 1st Year - 1st Semester
        """First Year - First Semester (Fall) - Compulsory Courses:
CHM101, General Chemistry, Credit:4, ECTS:5, Prerequisite: None, Class:4, LAB:2, Practical:0, PS:0, C:2, R:2, T:1
ECC101, Computer Programming, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:2
ENG101, English I, Credit:3, ECTS:4, Prerequisite: None, Class:0, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
MTH101, Calculus I, Credit:4, ECTS:6, Prerequisite: None, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
PHY101, General Physics I, Credit:4, ECTS:6, Prerequisite: None, Class:4, LAB:2, Practical:0, PS:2, C:1, R:1, T:0
YIT101, Turkish for Foreign Students I (Foreign Students), Credit:2, ECTS:2, Prerequisite: None, Class:2, LAB:0, Practical:0, PS:0, C:2, R:0, T:1
AIT101, Atatürk's Principles & Turkish Reform I (Turkish Students), Credit:2, ECTS:2, Prerequisite: None, Class:0, LAB:0, Practical:0, PS:0, C:2, R:0, T:1
TUR101, Türk Dili I (Turkish Students), Credit:2, ECTS:2, Prerequisite: None, Class:0, LAB:0, Practical:0, PS:0, C:2, R:0, T:1
AIT103, Principles of Ataturk and the History of Turkish Revolution I (Foreign Students), Credit:2, ECTS:2, Prerequisite: None, Class:0, LAB:0, Practical:0, PS:0, C:2, R:0, T:1

Total Semester: Credit:26, ECTS:34""",

        # 1st Year - 2nd Semester
        """First Year - Second Semester (Spring) - Compulsory Courses:
ENG102, English II, Credit:3, ECTS:6, Prerequisite: ENG101, Class:0, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
MTH102, Mathematics II, Credit:4, ECTS:6, Prerequisite: MTH101, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
MTH113, Linear Algebra, Credit:3, ECTS:6, Prerequisite: MTH101, Class:3, LAB:0, Practical:0, PS:1, C:1, R:1, T:0
PHY102, General Physics II, Credit:4, ECTS:6, Prerequisite: PHY101, Class:4, LAB:2, Practical:0, PS:2, C:1, R:1, T:0
TDE102, Technical Drawing and Electrical Applications, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:2, R:0, T:1
EE100, Introduction to Electrical & Electronic Engineering, Credit:1, ECTS:3, Prerequisite: None, Class:2, LAB:0, Practical:0, PS:1, C:1, R:1, T:0

Total Semester: Credit:18, ECTS:32""",

        # 2nd Year - 1st Semester
        """Second Year - First Semester (Fall) - Compulsory Courses:
ECC216, Circuit Theory I, Credit:4, ECTS:5, Prerequisite: PHY102, MTH101, Class:4, LAB:2, Practical:0, PS:2, C:1, R:1, T:0
EE210, Computer Applications, Credit:3, ECTS:6, Prerequisite: ECC101, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:2
EE241, Electrical Materials, Credit:3, ECTS:4, Prerequisite: CHM101, Class:3, LAB:0, Practical:0, PS:0, C:1, R:1, T:1
ENG201, English Communication Skills, Credit:3, ECTS:6, Prerequisite: ENG102, Class:3, LAB:0, Practical:0, PS:1, C:1, R:1, T:0
MTH201, Differential Equations, Credit:4, ECTS:6, Prerequisite: MTH102, Class:4, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
NTE, Non-technical Elective, Credit:3, ECTS:6, Prerequisite: None, Class:3

Total Semester: Credit:20, ECTS:33""",

        # 2nd Year - 2nd Semester
        """Second Year - Second Semester (Spring) - Compulsory Courses:
EE202, Circuit Theory II, Credit:4, ECTS:5, Prerequisite: ECC216, Class:4, LAB:2, Practical:0, PS:2, C:1, R:1, T:0
EE216, Electromagnetic Theory, Credit:3, ECTS:5, Prerequisite: PHY102, MTH102, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:2
EE220, Electrical Measurements, Credit:3, ECTS:5, Prerequisite: ECC216, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:2
ECC218, Electronics I, Credit:4, ECTS:6, Prerequisite: ECC216, EE241, Class:4, LAB:2, Practical:0, PS:2, C:1, R:1, T:0
MTH241, Complex Calculus, Credit:3, ECTS:5, Prerequisite: MTH102, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:2
EE200, Summer Training I, Credit:0, ECTS:6, Prerequisite: None, Class:0, LAB:0, Practical:0, PS:0, C:0, R:0, T:0

Total Semester: Credit:17, ECTS:32""",

        # 3rd Year - 1st Semester
        """Third Year - First Semester (Fall) - Compulsory Courses:
ECC001, Logic Circuit Design, Credit:4, ECTS:6, Prerequisite: ECC218, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:2
EE321, Electronics II, Credit:4, ECTS:6, Prerequisite: ECC218, Class:4, LAB:2, Practical:0, PS:2, C:1, R:1, T:0
EE331, Electromechanical Energy Conversion I, Credit:4, ECTS:5, Prerequisite: EE202, EE216, Class:4, LAB:2, Practical:0, PS:2, C:1, R:1, T:0
ECC008, Signals and Systems, Credit:4, ECTS:7, Prerequisite: EE202, Class:4, LAB:2, Practical:0, PS:2, C:1, R:1, T:0
MTH251, Probability and Random Variables, Credit:3, ECTS:6, Prerequisite: MTH102, Class:3, LAB:0, Practical:0, PS:1, C:1, R:1, T:0

Total Semester: Credit:19, ECTS:30""",

        # 3rd Year - 2nd Semester
        """Third Year - Second Semester (Spring) - Compulsory Courses:
ECC301, Microprocessors, Credit:4, ECTS:6, Prerequisite: ECC001, Class:4, LAB:2, Practical:0, PS:2, C:1, R:1, T:2
EE324, Linear Control Systems, Credit:3, ECTS:5, Prerequisite: MTH201, MTH113, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:2
EE346, Communication Systems, Credit:4, ECTS:6, Prerequisite: ECC008, Class:4, LAB:2, Practical:0, PS:2, C:1, R:1, T:2
MTH323, Numerical Analysis, Credit:3, ECTS:6, Prerequisite: MTH201, Class:3, LAB:0, Practical:0, PS:1, C:1, R:1, T:0
EE332, Electromechanical Energy Conversion II, Credit:3, ECTS:5, Prerequisite: EE331, Class:4, LAB:2, Practical:0, PS:2, C:1, R:1, T:0
EE300, Summer Training II, Credit:0, ECTS:6, Prerequisite: EE200, Class:0, LAB:0, Practical:0, PS:0, C:0, R:0, T:0

Total Semester: Credit:17, ECTS:34""",

        # 4th Year - 1st Semester
        """Fourth Year - First Semester (Fall) - Compulsory Courses:
RNTE, Restricted Non-Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3
EE4xx, Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3
EE4xx, Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3
EE4xx, Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3
EE4xx, Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3
EE401, Engineering Design I, Credit:4, ECTS:5, Prerequisite: None, Class:3

Total Semester: Credit:19, ECTS:30""",

        # 4th Year - 2nd Semester
        """Fourth Year - Second Semester (Spring) - Compulsory Courses:
EE402, Engineering Design II, Credit:4, ECTS:5, Prerequisite: EE401, Class:0, LAB:0, Practical:0, PS:0, C:0, R:0, T:0
EE4xx, Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3
EE4xx, Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3
EE4xx, Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3
EE4xx, Technical Elective, Credit:3, ECTS:5, Prerequisite: None, Class:3
YIT102, Turkish for Foreign Students II (Foreign Students), Credit:2, ECTS:2, Prerequisite: YIT101, Class:0, LAB:0, Practical:0, PS:0, C:2, R:0, T:1
TUR102, Türk Dili II (Turkish Students), Credit:2, ECTS:2, Prerequisite: TUR101, Class:0, LAB:0, Practical:0, PS:0, C:2, R:0, T:1
AIT102, Atatürk's Principles & Turkish Reform II (Turkish Students), Credit:2, ECTS:2, Prerequisite: AIT101, Class:0, LAB:0, Practical:0, PS:0, C:2, R:0, T:1
AIT104, Principles of Ataturk and the History of Turkish Revolution II (Foreign Students), Credit:2, ECTS:2, Prerequisite: AIT103, Class:0, LAB:0, Practical:0, PS:0, C:2, R:0, T:1

Total Semester: Credit:22, ECTS:28

Program Total: Credit:152, ECTS:253""",

        # Technical Elective Courses - Telecommunications Major
        """Technical Elective Courses - Telecommunications Major:
EE411, Telecommunications, Credit:3, ECTS:5, Prerequisite: EE346, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:0
EE412, Radar Systems, Credit:3, ECTS:5, Prerequisite: ECC008, MTH251, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:2
EE416, Computer Networking, Credit:3, ECTS:5, Prerequisite: ECC008, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:2
EE425, Satellite Communication Systems, Credit:3, ECTS:5, Prerequisite: EE346, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
EE427, Information Theory and Coding, Credit:3, ECTS:5, Prerequisite: ECC008, MTH251, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:2
EE428, Communication Electronics, Credit:3, ECTS:5, Prerequisite: EE346, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:2
EE429, Mobile Communication Systems, Credit:3, ECTS:5, Prerequisite: EE346, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
EE430, Wireless and Personnel Communications Systems, Credit:3, ECTS:5, Prerequisite: EE346, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
EE461, Digital Signal Processing, Credit:3, ECTS:5, Prerequisite: ECC008, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
EE463, Machine Learning in Computer Vision, Credit:3, ECTS:5, Prerequisite: ECC008, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:2
EE469, Electromagnetic Wave Propagation and Antennas, Credit:3, ECTS:5, Prerequisite: EE346, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:2
EE494, Introduction to Computer Vision, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:2""",

        # Technical Elective Courses - Control Major
        """Technical Elective Courses - Control Major:
EE420, Intelligent Control Systems, Credit:3, ECTS:5, Prerequisite: EE210, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:2
EE424, Process Control Instrumentation Technology, Credit:3, ECTS:5, Prerequisite: EE324, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:2
EE435, Mechatronics, Credit:3, ECTS:5, Prerequisite: EE324, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
EE451, Digital Electronics, Credit:3, ECTS:5, Prerequisite: ECC001, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
EE454, Digital Control Systems, Credit:3, ECTS:5, Prerequisite: EE324, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
ECC437, Robotic Systems, Credit:3, ECTS:5, Prerequisite: EE324, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:2
EE470, Programmable Logic Controllers, Credit:3, ECTS:5, Prerequisite: ECC001, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:2
EE495, Optimal and Adaptive Control, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:2""",

        # Technical Elective Courses - Power Major
        """Technical Elective Courses - Power Major:
EE433, Power Electronics, Credit:3, ECTS:5, Prerequisite: EE321, EE331, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:0
EE471, Power System Analysis I, Credit:3, ECTS:5, Prerequisite: EE331, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:2
EE472, Power System Analysis II, Credit:3, ECTS:5, Prerequisite: EE471, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:2
EE473, Power System Protection, Credit:3, ECTS:5, Prerequisite: EE471, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
EE474, Static Power Conversion, Credit:3, ECTS:5, Prerequisite: EE433, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:2
EE475, High Voltage Techniques I, Credit:3, ECTS:5, Prerequisite: EE331, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:2
EE476, High Voltage Techniques II, Credit:3, ECTS:5, Prerequisite: EE475, Class:3, LAB:2, Practical:0, PS:2, C:1, R:1, T:0
EE478, Distribution System Techniques, Credit:3, ECTS:5, Prerequisite: EE471, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0
EE492, Illumination Engineering, Credit:3, ECTS:5, Prerequisite: EE331, Class:3, LAB:0, Practical:0, PS:2, C:1, R:1, T:0""",

        # Restricted Non-Technical Elective Courses
        """Restricted Non-Technical Elective Courses (RNTE):
ECC426, Economics for Engineers, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:2, R:2, T:0
ECC427, Management for Engineers, Credit:3, ECTS:5, Prerequisite: None, Class:3, LAB:0, Practical:0, PS:0, C:2, R:2, T:0""",

        # Program Summary and Career Opportunities
        """Electrical and Electronic Engineering Program Summary:
Degree: Bachelor of Science in Electrical and Electronic Engineering
Duration: 4 years (8 semesters)
Total Credits: 152
Total ECTS: 253

Program Specialization Majors:
1. Telecommunications Major
   - Wireless and mobile communications
   - Signal processing and networking
   - Radar and satellite systems
   - Computer vision and machine learning

2. Control Major
   - Automation and robotics
   - Intelligent control systems
   - Digital control and PLCs
   - Mechatronics and instrumentation

3. Power Major
   - Power systems and protection
   - High voltage engineering
   - Power electronics and conversion
   - Energy systems and distribution

Career Opportunities:
Telecommunications Engineer
Control Systems Engineer
Power Systems Engineer
Electronics Design Engineer
Signal Processing Engineer
Robotics Engineer
Power Electronics Engineer
Communication Systems Engineer
Research and Development Engineer
Project Engineer
Academic and Research Positions

Professional Recognition:
Graduates are qualified to work in telecommunications, power systems, automation, electronics, and various high-tech industries worldwide."""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Engineering",
            "department": "Electrical and Electronic Engineering",
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
            "specialization": "telecommunications",
            "document_type": "course_list",
            "content_type": "technical_electives_telecommunications"
        },
        {
            "course_type": "elective",
            "elective_type": "technical",
            "specialization": "control",
            "document_type": "course_list",
            "content_type": "technical_electives_control"
        },
        {
            "course_type": "elective",
            "elective_type": "technical",
            "specialization": "power",
            "document_type": "course_list",
            "content_type": "technical_electives_power"
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
    ids = [f"electrical_eng_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Electrical and Electronic Engineering curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["electrical engineering power systems telecommunications"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_electrical_electronic_engineering_curriculum_to_chromadb()