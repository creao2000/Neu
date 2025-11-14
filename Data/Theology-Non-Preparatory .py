import chromadb
from chromadb.utils import embedding_functions

def add_theology_non_preparatory_curriculum_to_chromadb():
    """Add Theology Faculty Non-Preparatory curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_theology_non_preparatory",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_theology_non_preparatory",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_theology_non_preparatory")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF THEOLOGY
NON-POST-PREPARATORY ACADEMIC CURRICULUM (Formasyonlu)
Bachelor of Theology

Program Duration: 4 years (8 semesters)
Degree: Bachelor of Theology
Total ECTS for Graduation: Approximately 240

Main website: https://ilahiyat.neu.edu.tr/
Curriculum link: https://ilahiyat.neu.edu.tr/akademik/akademik-programlar/ilahiyat-formasyonlu/dersler/

Legend:
T = Theoretical Hours
U = Practical Hours
C = Credit
ECTS = European Credit Transfer System

Note: This program includes integrated pedagogical formation courses""",

        # 1st Semester
        """First Year - First Semester - Compulsory Courses:
YDAR101, Arabic I, T:8, U:0, C:8, ECTS:12
YDEN101, Foreign Language I, T:2, U:0, C:2, ECTS:1
ILH101, Reading the Quran and Tajweed I, T:2, U:0, C:2, ECTS:4
ILH102, Sira, T:2, U:0, C:2, ECTS:4
ILH103, History of Hadith, T:2, U:0, C:2, ECTS:4
ILH104, Islamic Principles of Faith, T:2, U:0, C:2, ECTS:3
TRD121, Turkish Language I, T:2, U:0, C:2, ECTS:1
ATA121, Atatürk's Principles and Revolutionary History I, T:2, U:0, C:2, ECTS:1

Total: T:22, U:0, C:22, ECTS:30""",

        # 2nd Semester
        """First Year - Second Semester - Compulsory Courses:
YDAR102, Arabic II, T:6, U:0, C:6, ECTS:9
YDEN102, Foreign Language II, T:2, U:0, C:2, ECTS:1
ILH111, Reading the Quran and Tajweed II, T:2, U:0, C:2, ECTS:4
ILH115, Hadith Methodology, T:2, U:0, C:2, ECTS:4
ILH116, History of Tafsir, T:2, U:0, C:2, ECTS:3
ILH117, Islamic Principles of Worship, T:2, U:0, C:2, ECTS:3
ILH118, Islamic History I, T:2, U:0, C:2, ECTS:4
TRD122, Turkish Language II, T:2, U:0, C:2, ECTS:1
ATA122, Atatürk's Principles and Revolutionary History II, T:2, U:0, C:2, ECTS:1

Total: T:22, U:0, C:22, ECTS:30""",

        # 3rd Semester
        """Second Year - Third Semester - Compulsory Courses:
YDAR201, Arabic III, T:4, U:0, C:4, ECTS:6
ILH201, Reading the Quran and Tajweed III, T:2, U:0, C:2, ECTS:4
ILH202, Method of Tafsir, T:2, U:0, C:2, ECTS:3
ILH203, Turkish Religious Music (Theories), T:2, U:0, C:2, ECTS:3
ILH204, Hadith I, T:4, U:0, C:4, ECTS:5
ILH205, Logic, T:2, U:0, C:2, ECTS:3
ILH206, Psychology of Religion, T:2, U:0, C:2, ECTS:3
ILH208, Islamic History II, T:2, U:0, C:2, ECTS:3

Total: T:20, U:0, C:20, ECTS:30""",

        # 4th Semester
        """Second Year - Fourth Semester - Compulsory Courses:
YDAR202, Arabic IV, T:2, U:0, C:2, ECTS:3
ILH211, Reading the Quran and Tajweed IV, T:2, U:0, C:2, ECTS:4
ILH214, Hadith II, T:2, U:0, C:2, ECTS:3
ILH217, Islamic Legal Procedure I, T:2, U:0, C:2, ECTS:3
ILH219, Tafsir I, T:4, U:0, C:4, ECTS:6
ILH220, Sociology of Religion, T:2, U:0, C:2, ECTS:3
ILH221, History of Kalam, T:2, U:0, C:2, ECTS:3
ILH222, Turkish Islamic Literature, T:2, U:0, C:2, ECTS:3
ILH223, History of Islamic Arts, T:2, U:0, C:2, ECTS:2

Total: T:20, U:0, C:20, ECTS:30""",

        # 5th Semester - Compulsory
        """Third Year - Fifth Semester - Compulsory Courses:
ILH301, Reading the Quran and Tajweed V, T:2, U:0, C:2, ECTS:4
ILH302, Systematic Theology I, T:4, U:0, C:4, ECTS:6
ILH305, Sufism I, T:2, U:0, C:2, ECTS:3
ILH306, History of Islamic Civilization, T:2, U:0, C:2, ECTS:3
ILH307, Islamic Legal Procedure II, T:2, U:0, C:2, ECTS:4
ILH308, History of Philosophy, T:2, U:0, C:2, ECTS:3
ILH309, Tafsir II, T:2, U:0, C:2, ECTS:3
ILH Elective Course - 1, T:2, U:0, C:2, ECTS:2
ILH Elective Course - 2, T:2, U:0, C:2, ECTS:2
AEF Elective Course - 3, Variable
AEF Elective Course - 4, Variable
AEF Elective Course - 5, Variable

Total: T:20, U:0, C:20, ECTS:30""",

        # 5th Semester - Electives
        """Fifth Semester Elective Courses:
ILH304, Ottoman Turkish, T:2, U:0, C:2, ECTS:2
ILH341, Sufi Music, T:2, U:0, C:2, ECTS:2
ILH342, Arabic Language Rhetoric, T:2, U:0, C:2, ECTS:2
ILH343, Hadith in Popular Education, T:2, U:0, C:2, ECTS:2
ILH344, Contemporary Islamic Countries I, T:2, U:0, C:2, ECTS:2
ILH345, History of Islamic Logic, T:2, U:0, C:2, ECTS:2
ILH346, Classical Fiqh Texts, T:2, U:0, C:2, ECTS:2
ILH347, Mental Health and Religion, Variable
AEF101, Introduction to Educational Sciences, T:3, U:0, C:3, ECTS:4
AEF102, Educational Psychology, T:3, U:0, C:3, ECTS:4
AEF213, Guidance, T:3, U:0, C:2, ECTS:5""",

        # 6th Semester - Compulsory
        """Third Year - Sixth Semester - Compulsory Courses:
ILH310, Islamic Law I, T:4, U:0, C:4, ECTS:6
ILH311, Reading the Quran and Tajweed VI, T:2, U:0, C:2, ECTS:4
ILH312, Systematic Theology II, T:2, U:0, C:2, ECTS:3
ILH315, Sufism II, T:2, U:0, C:2, ECTS:3
ILH320, History of Islamic Philosophy, T:4, U:0, C:4, ECTS:6
ILH321, History of Islamic Sects, T:2, U:0, C:2, ECTS:4
ILH Elective Course-1, T:2, U:0, C:2, ECTS:2
ILH Elective Course-2, T:2, U:0, C:2, ECTS:2
ILH444, Elective Course-3, Variable
AEF Elective Course-4, Variable

Total: T:20, U:0, C:20, ECTS:30""",

        # 6th Semester - Electives
        """Sixth Semester Elective Courses:
ILH322, Commentary Texts, T:2, U:0, C:2, ECTS:2
ILH323, Islamic Studies in the West, T:2, U:0, C:2, ECTS:2
ILH324, Current Philosophical Movements, T:2, U:0, C:2, ECTS:2
ILH326, Contemporary Islamic Movements, T:2, U:0, C:2, ECTS:2
ILH327, Logic and Islamic Sciences, T:2, U:0, C:2, ECTS:2
ILH328, Classical Sufi Texts, T:2, U:0, C:2, ECTS:2
ILH329, Scientific Writing and Research Techniques, T:2, U:0, C:2, ECTS:2
ILH330, Public Speaking and Communication, T:2, U:0, C:2, ECTS:2
ILH331, Contemporary Islamic Countries II, T:2, U:0, C:2, ECTS:2
ILH444, Developmental Psychology, T:3, U:0, C:3, ECTS:3
AEF201, Teaching Principles and Methods, T:3, U:0, C:3, ECTS:5""",

        # 7th Semester - Compulsory
        """Fourth Year - Seventh Semester - Compulsory Courses:
ILH401, Reading the Quran and Tajweed VII, T:2, U:0, C:2, ECTS:6
ILH402, Religious Education, T:2, U:0, C:2, ECTS:4
ILH403, Public Speaking and Professional Practice, T:2, U:0, C:2, ECTS:6
ILH404, Islamic Moral Principles and Philosophy, T:2, U:0, C:2, ECTS:4
ILH410, Islamic Law II, T:4, U:0, C:4, ECTS:6
ILH Elective Course-1, T:2, U:0, C:2, ECTS:2
AEF Elective Course-2, Variable
AEF Elective Course-3, Variable

Total: T:14, U:0, C:14, ECTS:28""",

        # 7th Semester - Electives
        """Seventh Semester Elective Courses:
ILH405, Communication and Guidance in Religious Services, T:2, U:0, C:2, ECTS:2
ILH407, Problems in the Psychology of Religion, T:2, U:0, C:2, ECTS:2
ILH408, Contemporary Mystical Movements, T:2, U:0, C:2, ECTS:2
ILH409, Hadith Criticism Methods, T:2, U:0, C:2, ECTS:2
ILH425, Contemporary Islamic Thinkers, T:2, U:0, C:2, ECTS:2
ILH426, Rhetoric and Religion, T:2, U:0, C:2, ECTS:2
ILH427, Social Psychology, Variable
AEF212, Instructional Technologies and Material Design, T:3, U:0, C:3, ECTS:3
AEF204, Special Teaching Methods, T:3, U:0, C:3, ECTS:3""",

        # 8th Semester - Compulsory
        """Fourth Year - Eighth Semester - Compulsory Courses:
ILH411, Reading the Quran and Tajweed VIII, T:2, U:0, C:2, ECTS:6
ILH417, History of Religions, T:4, U:0, C:4, ECTS:6
ILH418, Philosophy of Religion, T:2, U:0, C:2, ECTS:6
ILH419, Graduation Project, T:2, U:0, C:2, ECTS:8
AEF Elective Course-1, Variable
AEF Elective Course-2, Variable
AEF Elective Course-3, Variable
ILH Elective Course-4, T:2, U:0, C:2, ECTS:2

Total: T:12, U:0, C:12, ECTS:28""",

        # 8th Semester - Electives
        """Eighth Semester Elective Courses:
ILH420, Contemporary Turkish Thought, T:2, U:0, C:2, ECTS:2
ILH421, Current Fiqh Problems, T:2, U:0, C:2, ECTS:2
ILH422, Living World Religions, T:2, U:0, C:2, ECTS:2
ILH423, Today's Hadith Problems, T:2, U:0, C:2, ECTS:2
ILH424, Turkish Theologians, T:2, U:0, C:2, ECTS:2
ILH427, Values Education, T:2, U:0, C:2, ECTS:2
ILH429, Classical Sira Texts, T:2, U:0, C:2, ECTS:2
ILH430, Understanding Global Society, Variable
AEF303, Classroom Management, T:2, U:0, C:2, ECTS:3
AEF314, Measurement and Evaluation in Education, T:3, U:0, C:3, ECTS:4
AEF406, Teaching Practice, T:5, U:2, C:3, ECTS:10
ILH431, Personal Development and Religion, T:2, U:0, C:2, ECTS:2
ILH432, Comparative Mythology, T:2, U:0, C:2, ECTS:2""",

        # Program Summary and Career Opportunities
        """Theology (Non-Preparatory) Program Summary:
Degree: Bachelor of Theology (with Pedagogical Formation)
Duration: 4 years (8 semesters)
Total ECTS: Approximately 240
Language of Instruction: Turkish/Arabic
Program Type: Integrated Pedagogical Formation

Key Features:
- Includes Arabic language courses throughout the curriculum
- Integrated pedagogical formation courses (AEF coded)
- Graduation project requirement
- Teaching practice opportunities

Program Focus Areas:
- Arabic Language and Literature
- Quranic Studies and Tajweed
- Hadith Sciences
- Islamic Law and Jurisprudence
- Islamic Theology and Philosophy
- Religious Education
- Islamic History and Civilization

Career Opportunities:
Religious Education Teacher
Imam and Religious Leader
Quran Course Instructor
Religious Affairs Specialist
Religious Counselor
Academic Researcher
Interfaith Dialogue Coordinator
Islamic Content Developer
Community Religious Advisor
Museum Educator for Islamic Arts

Professional Settings:
Ministry of National Education
Ministry of Religious Affairs
Public and Private Schools
Quran Courses and Religious Education Centers
Research Institutions
Islamic Cultural Centers
Media and Publishing
Non-Governmental Organizations""",

        # Key Differences from Post-Preparatory Program
        """Key Differences from Post-Preparatory Program:

1. Arabic Language Integration:
   - Intensive Arabic courses throughout first two years
   - No separate preparatory year required
   - Gradual Arabic language development

2. Pedagogical Formation:
   - Integrated education courses (AEF coded)
   - Teaching methodology and practice
   - Classroom management skills
   - Educational psychology

3. Course Structure:
   - More credits in early semesters (22 vs 21)
   - Different course codes and sequencing
   - Integrated approach to language and content

4. Teaching Qualification:
   - Direct pathway to teaching certification
   - Teaching practice included
   - Special teaching methods for religious education

Specialization Areas:
1. Religious Education and Pedagogy
2. Islamic Sciences and Arabic Literature
3. Religious Counseling and Guidance
4. Islamic History and Civilization
5. Contemporary Islamic Studies"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Theology",
            "program_type": "Non-Preparatory",
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
            "content_type": "third_year_first_semester_compulsory"
        },
        {
            "year": "3",
            "semester": "1",
            "course_type": "elective",
            "document_type": "course_list",
            "content_type": "fifth_semester_electives"
        },
        {
            "year": "3",
            "semester": "2",
            "document_type": "course_list",
            "content_type": "third_year_second_semester_compulsory"
        },
        {
            "year": "3",
            "semester": "2",
            "course_type": "elective",
            "document_type": "course_list",
            "content_type": "sixth_semester_electives"
        },
        {
            "year": "4",
            "semester": "1",
            "document_type": "course_list",
            "content_type": "fourth_year_first_semester_compulsory"
        },
        {
            "year": "4",
            "semester": "1",
            "course_type": "elective",
            "document_type": "course_list",
            "content_type": "seventh_semester_electives"
        },
        {
            "year": "4",
            "semester": "2",
            "document_type": "course_list",
            "content_type": "fourth_year_second_semester_compulsory"
        },
        {
            "year": "4",
            "semester": "2",
            "course_type": "elective",
            "document_type": "course_list",
            "content_type": "eighth_semester_electives"
        },
        {
            "document_type": "program_info",
            "content_type": "program_summary_careers"
        },
        {
            "document_type": "program_info",
            "content_type": "program_comparison"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"theology_np_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Theology Non-Preparatory curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["Arabic language pedagogical formation"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_theology_non_preparatory_curriculum_to_chromadb()