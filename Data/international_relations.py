import chromadb
from chromadb.utils import embedding_functions

def add_international_relations_curriculum_to_chromadb():
    """Add International Relations curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_international_relations",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_international_relations",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_international_relations")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information - CORRECTED DEGREE
        """FACULTY OF ECONOMICS AND ADMINISTRATIVE SCIENCES
DEPARTMENT OF INTERNATIONAL RELATIONS
Bachelor of Science in International Relations

Program Duration: 4 years (8 semesters)
Degree: Bachelor of Science
Total ECTS for Graduation: 240

Main website: https://iktisat.neu.edu.tr/?lang=en
Curriculum link: https://iktisat.neu.edu.tr/academic/academic-programmes/department-of-international-relations/courses/?lang=en

Legend:
C = Compulsory Course
E = Elective Course
T = Theoretical Hours
ECTS = European Credit Transfer System""",

        # 1st Year - 1st Semester
        """First Year - First Semester - Compulsory Courses:
ENG101, English I, C, Credit:3, ECTS:4, Hours:3
SOC100, Sociology, C, Credit:3, ECTS:6, Hours:3
EAS110, Political Science I, C, Credit:3, ECTS:6, Hours:3
EAS101, Principles of Economics I, C, Credit:3, ECTS:6, Hours:3
EAS105, History of Civilizations, C, Credit:3, ECTS:6, Hours:3
YIT101/TUR101, Turkish for International Students I/Turkish Language I, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:30, Hours:17""",

        # 1st Year - 2nd Semester
        """First Year - Second Semester - Compulsory Courses:
ENG102, English II, C, Credit:3, ECTS:4, Hours:3
EAS112, Political Science II, C, Credit:3, ECTS:6, Hours:3
EAS111, History of Political Thought, C, Credit:3, ECTS:6, Hours:3
EAS102, Principles of Economics II, C, Credit:3, ECTS:6, Hours:3
EAS206, Introduction to Law, C, Credit:3, ECTS:6, Hours:3
YIT102/TUR102, Turkish for International Students II/Turkish Language II, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:30, Hours:17""",

        # 2nd Year - 1st Semester
        """Second Year - First Semester - Compulsory Courses:
EAS215, Academic Communication, C, Credit:3, ECTS:4, Hours:3
IR203, Diplomatic History, C, Credit:3, ECTS:6, Hours:3
IR205, Constitutional Law, C, Credit:3, ECTS:6, Hours:3
IR210, Modern Political Thought, C, Credit:3, ECTS:6, Hours:3
IR207, Introduction to International Relations I, C, Credit:3, ECTS:6, Hours:3
AİT101/103, Atatürk's Principles I/Principles of Atatürk I, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:30, Hours:17""",

        # 2nd Year - 2nd Semester
        """Second Year - Second Semester - Compulsory Courses:
EAS216, Academic Writing, C, Credit:3, ECTS:4, Hours:3
HIST205, World History of the 20th Century, C, Credit:3, ECTS:6, Hours:3
HIST206, Modern Turkish Politics, C, Credit:3, ECTS:6, Hours:3
EAS208, Research Methods, C, Credit:3, ECTS:6, Hours:3
IR208, Introduction to International Relations II, C, Credit:3, ECTS:6, Hours:3
AİT102/104, Atatürk's Principles II/Principles of Atatürk II, C, Credit:2, ECTS:2, Hours:2

Total: Credit:17, ECTS:30, Hours:17""",

        # 3rd Year - 1st Semester
        """Third Year - First Semester - Compulsory Courses:
IR307, Introduction to International Law I, C, Credit:3, ECTS:6, Hours:3
IR311, Turkish Foreign Policy I, C, Credit:3, ECTS:6, Hours:3
IR313, International Politics & Security, C, Credit:3, ECTS:6, Hours:3
IR316, Theories of International Relations, C, Credit:3, ECTS:6, Hours:3
HIST308, Ottoman Economic, Social & Political Structure I, C, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 3rd Year - 2nd Semester
        """Third Year - Second Semester - Compulsory Courses:
IR312, International Institutions & Organization, C, Credit:3, ECTS:6, Hours:3
IR315, Turkish Foreign Policy II, C, Credit:3, ECTS:6, Hours:3
IR314, International Political Economics, C, Credit:3, ECTS:6, Hours:3
POL312, Comparative Political Systems, C, Credit:3, ECTS:6, Hours:3
HIST309, Ottoman Economic, Social & Political Structure II, C, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 4th Year - 1st Semester
        """Fourth Year - First Semester - Compulsory Courses:
IR401, Analysis of International Relations I, C, Credit:3, ECTS:6, Hours:3
IR400, The Cyprus Issue, C, Credit:3, ECTS:6, Hours:3
Elective Course, International Relations Elective, E, Credit:3, ECTS:6, Hours:3
Elective Course, International Relations Elective, E, Credit:3, ECTS:6, Hours:3
Elective Course, International Relations Elective, E, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # 4th Year - 2nd Semester
        """Fourth Year - Second Semester - Compulsory Courses:
IR402, Analysis of International Relations II, C, Credit:3, ECTS:6, Hours:3
Elective Course, International Relations Elective, E, Credit:3, ECTS:6, Hours:3
Elective Course, International Relations Elective, E, Credit:3, ECTS:6, Hours:3
Elective Course, International Relations Elective, E, Credit:3, ECTS:6, Hours:3
Elective Course, International Relations Elective, E, Credit:3, ECTS:6, Hours:3

Total: Credit:15, ECTS:30, Hours:15""",

        # Program Summary - CORRECTED DEGREE
        """International Relations Program Summary:
Degree: Bachelor of Science in International Relations
Duration: 4 years (8 semesters)
Total ECTS: 240
Language of Instruction: English

Program Focus Areas:
- International Relations Theory
- Diplomatic History and Practice
- International Security Studies
- International Political Economy
- Turkish Foreign Policy
- International Law and Organizations
- The Cyprus Issue (Special Focus)

Career Opportunities:
Diplomatic Service Officer
International Organization Staff
Foreign Policy Analyst
Intelligence Analyst
International Business Consultant
Political Risk Analyst
NGO Program Manager""",
    ]
    
    # Corresponding metadata - CORRECTED DEGREE
    metadatas = [
        {
            "faculty": "Economics and Administrative Sciences",
            "department": "International Relations",
            "degree": "Bachelor of Science",  # CORRECTED
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
            "document_type": "program_info",
            "content_type": "program_summary_careers"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"ir_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} International Relations curriculum documents to ChromaDB!")
        print("✅ CORRECTED: Degree is now Bachelor of Science in International Relations")

        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_international_relations_curriculum_to_chromadb()