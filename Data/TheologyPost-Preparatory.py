import chromadb
from chromadb.utils import embedding_functions

def add_theology_curriculum_to_chromadb():
    """Add Theology Faculty Post-Preparatory curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_theology",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_theology",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_theology")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF THEOLOGY
POST-PREPARATORY ACADEMIC CURRICULUM
Bachelor of Theology

Program Duration: 4 years (8 semesters)
Degree: Bachelor of Theology
Total ECTS for Graduation: Approximately 240

Main website: https://ilahiyat.neu.edu.tr/
Curriculum link: https://ilahiyat.neu.edu.tr/akademik/akademik-programlar/hazirlik-sonrasi-akademik-mufredat/dersler/

Legend:
T = Theoretical Hours
U = Practical Hours
C = Credit
ECTS = European Credit Transfer System""",

        # 1st Semester
        """First Year - First Semester - Compulsory Courses:
ADE101, Arabic Language and Literature (Arabic), T:2, U:0, C:2, ECTS:3
YDEN101, Foreign Language I, T:2, U:0, C:2, ECTS:1
ILH101, Reading the Quran and Tajweed I, T:0, U:2, C:2, ECTS:4
ILH112, Sirah (Arabic), T:4, U:0, C:4, ECTS:4
ILH113, History of Hadith (Arabic), T:2, U:0, C:2, ECTS:4
ILH104, Islamic Principles of Faith, T:2, U:0, C:2, ECTS:3
TUR101, Turkish Language I, T:2, U:0, C:2, ECTS:2
AIT101, Atatürk's Principles and Revolutionary History I, T:2, U:0, C:2, ECTS:2
AEF101, Introduction to Educational Sciences, T:3, U:0, C:3, ECTS:4

Total: T:19, U:2, C:21, ECTS:32""",

        # 2nd Semester
        """First Year - Second Semester - Compulsory Courses:
ADE102, Arabic Language and Literature (Arabic), T:2, U:0, C:2, ECTS:3
AEF102, Educational Psychology, T:3, U:0, C:3, ECTS:4
YDEN102, Foreign Language II, T:2, U:0, C:2, ECTS:1
ILH111, Reading the Quran and Tajweed II, T:0, U:2, C:2, ECTS:4
ILH115, Hadith Methodology, T:2, U:0, C:2, ECTS:4
ILH126, History of Tafsir (Arabic), T:2, U:0, C:2, ECTS:3
ILH117, Islamic Principles of Worship, T:2, U:0, C:2, ECTS:3
ILH118, Islamic History I, T:2, U:0, C:2, ECTS:4
TUR102, Turkish Language II, T:2, U:0, C:2, ECTS:2
AIT102, Atatürk's Principles and Revolutionary History II, T:2, U:0, C:2, ECTS:2

Total: T:19, U:2, C:21, ECTS:32""",

        # 3rd Semester
        """Second Year - Third Semester - Compulsory Courses:
ILH444, Developmental Psychology, T:3, U:0, C:3, ECTS:3
ILH201, Reading the Quran and Tajweed III, T:0, U:2, C:2, ECTS:4
ILH202, Method of Tafsir, T:2, U:0, C:2, ECTS:3
ILH203, Turkish Religious Music (Theories), T:2, U:0, C:2, ECTS:3
ILH224, Hadith I (Arabic), T:4, U:0, C:4, ECTS:5
ILH205, Logic, T:2, U:0, C:2, ECTS:3
ILH206, Psychology of Religion, T:2, U:0, C:2, ECTS:3
ILH208, History of Islam II, T:2, U:0, C:2, ECTS:3

Total: T:17, U:2, C:19, ECTS:27""",

        # 4th Semester
        """Second Year - Fourth Semester - Compulsory Courses:
AEF201, Teaching Principles and Methods, T:3, U:0, C:3, ECTS:5
ILH211, Reading the Quran and Tajweed IV, T:0, U:2, C:2, ECTS:4
ILH234, Hadith II (Arabic), T:2, U:0, C:2, ECTS:3
ILH217, Islamic Legal Procedure I, T:2, U:0, C:2, ECTS:3
ILH229, Tafsir I (Arabic), T:4, U:0, C:4, ECTS:6
ILH220, Sociology of Religion, T:2, U:0, C:2, ECTS:3
ILH221, History of Kalam, T:2, U:0, C:2, ECTS:3
ILH222, Turkish Islamic Literature, T:2, U:0, C:2, ECTS:3
ILH223, History of Islamic Arts, T:2, U:0, C:2, ECTS:2

Total: T:19, U:2, C:21, ECTS:32""",

        # 5th Semester - Compulsory
        """Third Year - Fifth Semester - Compulsory Courses:
ILH301, Reading the Quran and Tajweed V, T:0, U:2, C:2, ECTS:4
AEF456, Character and Values Education, T:3, U:0, C:3, ECTS:2
AEF212, Instructional Technologies and Material Design, T:3, U:0, C:3, ECTS:3
ILH302, Systematic Theology I, T:4, U:0, C:4, ECTS:6
ILH305, Sufism I, T:2, U:0, C:2, ECTS:3
ILH306, History of Islamic Civilization, T:2, U:0, C:2, ECTS:3
ILH307, Islamic Legal Procedure II, T:2, U:0, C:2, ECTS:4
ILH308, History of Philosophy, T:2, U:0, C:2, ECTS:3
ILH319, Tafsir II (Arabic), T:2, U:0, C:2, ECTS:3
Elective Course - 1, T:2, U:0, C:2, ECTS:2
Elective Course - 2, T:2, U:0, C:2, ECTS:2

Total: T:23, U:2, C:25, ECTS:35""",

        # 5th Semester - Electives
        """Fifth Semester Elective Courses:
ILH304, Ottoman Turkish, T:2, U:0, C:2, ECTS:2
ILH341, Sufi Music, T:2, U:0, C:2, ECTS:2
ILH342, Arabic Language Rhetoric, T:2, U:0, C:2, ECTS:2
ILH343, Hadith in Popular Education, T:2, U:0, C:2, ECTS:2
ILH344, Contemporary Islamic Countries I, T:2, U:0, C:2, ECTS:2
ILH345, History of Islamic Logic, T:2, U:0, C:2, ECTS:2
ILH346, Classical Fiqh Texts, T:2, U:0, C:2, ECTS:2
ILH347, Mental Health and Religion, T:2, U:0, C:2, ECTS:2""",

        # 6th Semester - Compulsory
        """Third Year - Sixth Semester - Compulsory Courses:
ILH300, Islamic Law I (Arabic), T:4, U:0, C:4, ECTS:6
AEF303, Classroom Management, T:2, U:0, C:2, ECTS:3
AEF314, Measurement and Evaluation in Education, T:3, U:0, C:3, ECTS:5
ILH311, Reading the Quran and Tajweed VI, T:0, U:2, C:2, ECTS:4
ILH312, Systematic Theology II, T:2, U:0, C:2, ECTS:3
ILH315, Sufism II, T:2, U:0, C:2, ECTS:3
ILH320, History of Islamic Philosophy, T:4, U:0, C:4, ECTS:6
ILH321, History of Islamic Sects, T:2, U:0, C:2, ECTS:4
Elective Course-3, T:2, U:0, C:2, ECTS:2
Elective Course-4, T:2, U:0, C:2, ECTS:2

Total: T:23, U:2, C:25, ECTS:38""",

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
ILH331, Contemporary Islamic Countries II, T:2, U:0, C:2, ECTS:2""",

        # 7th Semester - Compulsory
        """Fourth Year - Seventh Semester - Compulsory Courses:
ILH401, Reading the Quran and Tajweed VII, T:0, U:2, C:2, ECTS:6
AEF204, Special Teaching Methods, T:3, U:2, C:3, ECTS:3
ILH402, Religious Education, T:2, U:0, C:2, ECTS:4
ILH403, Public Speaking and Professional Practice, T:2, U:0, C:2, ECTS:6
ILH404, Islamic Moral Principles and Philosophy, T:2, U:0, C:2, ECTS:4
ILH400, Islamic Law II (Arabic), T:4, U:0, C:4, ECTS:6
Elective Course-5, T:2, U:0, C:2, ECTS:2
Elective Course-6, T:2, U:0, C:2, ECTS:2

Total: T:17, U:4, C:19, ECTS:33""",

        # 7th Semester - Electives
        """Seventh Semester Elective Courses:
ILH405, Communication and Guidance in Religious Services, T:2, U:0, C:2, ECTS:2
ILH407, Problems of Religious Psychology, T:2, U:0, C:2, ECTS:2
ILH408, Contemporary Mystical Movements, T:2, U:0, C:2, ECTS:2
ILH409, Hadith Criticism Methods, T:2, U:0, C:2, ECTS:2
ILH425, Contemporary Islamic Thinkers, T:2, U:0, C:2, ECTS:2
ILH426, Rhetoric and Religion, T:2, U:0, C:2, ECTS:2
ILH427, Social Psychology, T:2, U:0, C:2, ECTS:2""",

        # 8th Semester - Compulsory
        """Fourth Year - Eighth Semester - Compulsory Courses:
ILH411, Reading the Quran and Tajweed VIII, T:0, U:2, C:2, ECTS:6
ILH417, History of Religions, T:4, U:0, C:4, ECTS:6
AEF406, Teaching Practice, T:0, U:5, C:5, ECTS:10
ILH418, Philosophy of Religion, T:2, U:0, C:2, ECTS:6
ILH419, Graduation Project, T:2, U:0, C:2, ECTS:8
Elective Course-7, T:2, U:0, C:2, ECTS:2
Elective Course-8, T:2, U:0, C:2, ECTS:2

Total: T:12, U:7, C:19, ECTS:40""",

        # 8th Semester - Electives
        """Eighth Semester Elective Courses:
ILH420, Contemporary Turkish Thought, T:2, U:0, C:2, ECTS:2
ILH421, Current Fiqh Problems, T:2, U:0, C:2, ECTS:2
ILH422, Living World Religions, T:2, U:0, C:2, ECTS:2
ILH423, Today's Hadith Problems, T:2, U:0, C:2, ECTS:2
ILH424, Turkish Theologians, T:2, U:0, C:2, ECTS:2
ILH427, Values Education, T:2, U:0, C:2, ECTS:2
ILH429, Classical Sira Texts, T:2, U:0, C:2, ECTS:2
ILH430, Understanding Global Society, T:2, U:0, C:2, ECTS:2
ILH431, Personal Development and Religion, T:2, U:0, C:2, ECTS:2
ILH432, Comparative Mythology, T:2, U:0, C:2, ECTS:2""",

        # Program Summary and Career Opportunities
        """Theology Program Summary:
Degree: Bachelor of Theology
Duration: 4 years (8 semesters)
Total ECTS: Approximately 240
Language of Instruction: Turkish/Arabic

Program Focus Areas:
- Quranic Studies and Tajweed
- Hadith Sciences
- Islamic Law (Fiqh)
- Islamic Theology (Kalam)
- Islamic History and Civilization
- Comparative Religion
- Religious Education
- Sufism and Islamic Spirituality

Core Competencies Developed:
- Advanced Arabic language skills for Islamic texts
- Quran recitation and interpretation
- Hadith analysis and methodology
- Islamic legal reasoning
- Theological discourse
- Religious counseling and guidance
- Teaching methodologies for religious education

Career Opportunities:
Religious Affairs Officer
Imam and Religious Leader
Quran Teacher
Religious Education Instructor
Islamic Studies Researcher
Religious Counselor
Interfaith Dialogue Specialist
Academic in Islamic Studies
Museum Curator for Islamic Arts
Islamic Content Writer
Community Religious Advisor

Professional Settings:
Ministry of Religious Affairs
Educational Institutions
Research Centers
Islamic Cultural Centers
Interfaith Organizations
Publishing Houses
Media and Broadcasting
Non-Profit Organizations""",

        # Specialization Areas
        """Specialization Areas in Theology:

1. Quranic Sciences and Tafsir:
   - Quran recitation (Tajweed)
   - Tafsir methodology
   - Classical commentary texts
   - Contemporary Quranic studies

2. Hadith Sciences:
   - Hadith methodology
   - Hadith criticism
   - Classical hadith texts
   - Contemporary hadith issues

3. Islamic Law and Jurisprudence:
   - Islamic legal procedure
   - Classical fiqh texts
   - Contemporary legal problems
   - Comparative law

4. Islamic Theology and Philosophy:
   - Systematic theology
   - History of Islamic philosophy
   - Contemporary theological issues
   - Philosophy of religion

5. Islamic History and Civilization:
   - Islamic history
   - History of Islamic sects
   - Contemporary Islamic movements
   - Turkish Islamic thought

6. Religious Education and Counseling:
   - Teaching methods
   - Religious psychology
   - Counseling techniques
   - Values education

Unique Features:
- Strong emphasis on Arabic language for classical texts
- Integration of traditional Islamic sciences with modern approaches
- Teaching practice and professional preparation
- Comprehensive elective system for specialization"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Theology",
            "program_type": "Post-Preparatory",
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
            "content_type": "specialization_areas"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"theology_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Theology curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["Quran tajweed hadith courses"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_theology_curriculum_to_chromadb()