

import chromadb
from chromadb.utils import embedding_functions

def add_audiology_curriculum_to_chromadb():
    """Add Audiology curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_audiology",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_audiology",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_audiology")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF HEALTH SCIENCES
DEPARTMENT OF AUDIOLOGY
Bachelor of Science in Audiology
Main website link: https://saglikbilimleri.neu.edu.tr/?lang=en
Curriculum link: https://saglikbilimleri.neu.edu.tr/wp-content/uploads/sites/144/2020/08/25/audiology-courses-25.08.2020.pdf
https://saglikbilimleri.neu.edu.tr/academic/academic-programmes/department-of-physiotherapy-and-rehabilitation/courses/?lang=en


Program Duration: 4 years (8 semesters)
Degree: Bachelor of Science
Total ECTS for Graduation: 240

Legend:
C = Compulsory Course
E = Elective Course
T = Theoretical Hours
P = Practical Hours
C = Credits
ECTS = European Credit Transfer System""",

        # 1st Year - 1st Semester
        """First Year - First Semester (Fall) - Compulsory Courses:
AIT103, Principles of Ataturk and the History of Turkish Revolution 1, C, T:2, P:0, C:2, ECTS:2
ANT103, Anatomy of Hearing and Speech Organs, C, T:3, P:0, C:3, ECTS:3
PHS101, Basic Physiology, C, T:3, P:0, C:3, ECTS:4
AUD103, Introduction to Audiology, C, T:3, P:2, C:4, ECTS:5
AUD101, Sound Physics and Acoustic Principles, C, T:3, P:0, C:3, ECTS:4
ENG101, English I, C, T:3, P:0, C:3, ECTS:3
YIT101, Turkish For Foreign Students I, C, T:3, P:0, C:3, ECTS:3

Total Compulsory: T:19, P:2, C:20, ECTS:24

Elective Courses (Select to reach 30 ECTS):
COM101, Computer, E, T:3, P:2, C:3, ECTS:3
AUD117, Introduction to Speech and Language, E, T:3, P:0, C:3, ECTS:4
AUD109, Music Therapy, E, T:2, P:0, C:2, ECTS:3
BES103, Nutrition Basics I, E, T:1, P:0, C:1, ECTS:3
SBF155, Self Knowledge and Communication Skills, E, T:2, P:0, C:2, ECTS:3
AID103, First Aid, E, T:2, P:0, C:2, ECTS:3

Total Semester ECTS: 30""",

        # 1st Year - 2nd Semester
        """First Year - Second Semester (Spring) - Compulsory Courses:
AIT104, Principles of Ataturk and the History of Turkish Revolution 2, C, T:2, P:0, C:2, ECTS:2
ANT102, Neuroanatomy of Speech and Hearing, C, T:2, P:0, C:2, ECTS:3
PHS102, Neurophysiology, C, T:2, P:0, C:2, ECTS:3
SBF118, Ear Nose and Throat Disorders, C, T:2, P:0, C:2, ECTS:4
AUD106, Interview Techniques in Audiology, C, T:2, P:0, C:2, ECTS:3
ENG102, English II, C, T:3, P:0, C:3, ECTS:3
YIT102, Turkish For Foreign Students II, C, T:3, P:0, C:3, ECTS:3

Total Compulsory: T:16, P:0, C:16, ECTS:21

Elective Courses (Select to reach 30 ECTS):
SBF158, Developmental Psychology, E, T:2, P:0, C:2, ECTS:3
MLB102, Molecular Biology, E, T:3, P:0, C:3, ECTS:3
PSY102, Psychology, E, T:2, P:0, C:2, ECTS:2
BES104, Nutrition Basics II, E, T:1, P:0, C:1, ECTS:3
SBF156, Interpersonal Relationships and Communication, E, T:2, P:0, C:2, ECTS:3
PHS104, Physiology- Hearing/Speech and Vestibular Organs, E, T:3, P:0, C:3, ECTS:3

Total Semester ECTS: 30

Prerequisites: ENG101 is prerequisite for ENG102""",

        # 2nd Year - 3rd Semester
        """Second Year - Third Semester (Fall) - Compulsory Courses:
AUD221, Basic Audiological Tests, C, T:4, P:0, C:4, ECTS:5
AUD223, Laboratory Practises in Audiology, C, T:0, P:4, C:2, ECTS:5
AUD211, Auditory System Disorders, C, T:2, P:0, C:2, ECTS:4
AUD225, Medical Terminology, C, T:2, P:0, C:2, ECTS:2
AUD227, Speech and Language Disorders in Hearing Impaired, C, T:2, P:0, C:2, ECTS:3
BST201, Biostatistics, C, T:3, P:0, C:3, ECTS:5

Total Compulsory: T:13, P:4, C:15, ECTS:24

Elective Courses (Select to reach 30 ECTS):
YIT201, Turkish For Foreign Students III, E, T:3, P:0, C:3, ECTS:3
AUD213, Auditory Perception Processes, E, T:2, P:0, C:2, ECTS:3
AUD209, Psycholinguistics, E, T:2, P:0, C:2, ECTS:3
AUD217, Positive Psychology, E, T:2, P:0, C:2, ECTS:3
AUD219, Geriatric Audiology, E, T:2, P:0, C:2, ECTS:3

Total Semester ECTS: 30""",

        # 2nd Year - 4th Semester
        """Second Year - Fourth Semester (Spring) - Compulsory Courses:
AUD208, Pediatric Audiology, C, T:3, P:2, C:4, ECTS:5
AUD210, Vestibular System Disorders, C, T:2, P:0, C:2, ECTS:3
AUD214, Audiology Practice – I, C, T:0, P:8, C:4, ECTS:5
AUD224, Audiological Diagnosis and Interpretation, C, T:4, P:0, C:4, ECTS:5
AUD226, Hearing Screening Tests, C, T:1, P:2, C:2, ECTS:3
AUD230, Biophysics, C, T:2, P:0, C:2, ECTS:3

Total Compulsory: T:12, P:12, C:18, ECTS:24

Elective Courses (Select to reach 30 ECTS):
YIT202, Turkish For Foreign Students IV, E, T:3, P:0, C:3, ECTS:3
AUD202, Diagnostic Tests in Audiometry, E, T:2, P:2, C:3, ECTS:4
AUD204, Vestibular System Physical Examination Techniques, E, T:2, P:3, C:3, ECTS:4
AUD220, Medical Ethics and Deontology, E, T:2, P:0, C:2, ECTS:2
AUD228, Auditory Processing Disorders, E, T:2, P:0, C:2, ECTS:4

Total Semester ECTS: 30

Prerequisites: 1st and 2nd Year AUD coded compulsory courses are prerequisite for AUD214""",

        # 3rd Year - 5th Semester
        """Third Year - Fifth Semester (Fall) - Compulsory Courses:
AUD301, Electrophysiologic Tests I, C, T:2, P:2, C:3, ECTS:5
AUD303, Hearing Aids I, C, T:3, P:2, C:4, ECTS:5
AUD305, Vestibular System and Evaluation, C, T:3, P:2, C:4, ECTS:5
AUD307, Pediatric Audiology Cases, C, T:3, P:2, C:4, ECTS:5

Total Compulsory: T:11, P:8, C:15, ECTS:20

Elective Courses (Select to reach 30 ECTS):
AUD309, Turkish Sign Language-I, E, T:1, P:2, C:2, ECTS:4
AUD311, Industrial Audiology, E, T:2, P:0, C:2, ECTS:4
AUD313, Hearing and Genetic, E, T:2, P:0, C:2, ECTS:4
FHS335, Research Methods in Health Sciences, E, T:2, P:0, C:2, ECTS:3
FHS355, Time Management, E, T:2, P:0, C:2, ECTS:3

Total Semester ECTS: 30""",

        # 3rd Year - 6th Semester
        """Third Year - Sixth Semester (Spring) - Compulsory Courses:
AUD302, Electrophysiologic Tests II, C, T:2, P:2, C:3, ECTS:5
AUD304, Hearing Aids II, C, T:3, P:2, C:4, ECTS:5
AUD306, Audiology Practice II, C, T:0, P:8, C:4, ECTS:5
AUD308, Vestibular Rehabilitation, C, T:1, P:2, C:2, ECTS:3
HIN302, Health Informatics, C, T:3, P:0, C:3, ECTS:5

Total Compulsory: T:9, P:14, C:16, ECTS:23

Elective Courses (Select to reach 30 ECTS):
AUD310, Turkish Sign Language-II, E, T:1, P:2, C:2, ECTS:4
AUD312, Music Perception in Hearing Impaired, E, T:2, P:0, C:2, ECTS:4
AUD314, Analysis of Voice and Speech, E, T:2, P:0, C:2, ECTS:4
AUD320, Audiology Cases, E, T:2, P:0, C:2, ECTS:4
AUD316, Neurolinguistics, E, T:2, P:0, C:2, ECTS:3
AUD318, Acoustic Features in Educational Settings, E, T:2, P:0, C:2, ECTS:3

Total Semester ECTS: 30

Prerequisites:
- 1st and 2nd Year AUD coded compulsory courses and 3rd Year fall semester compulsory courses are prerequisite for AUD306
- AUD301 is prerequisite for AUD302
- AUD303 is prerequisite for AUD304
- AUD309 is prerequisite for AUD310""",

        # 4th Year - 7th Semester
        """Fourth Year - Seventh Semester (Fall) - Compulsory Courses:
AUD401, Project Work I, C, T:0, P:2, C:1, ECTS:4
AUD403, Seminars in Audiology I, C, T:0, P:2, C:1, ECTS:3
AUD405, Auditory Implants, C, T:3, P:0, C:3, ECTS:4
AUD407, Clinical Audiology: Practice and Observation, C, T:0, P:6, C:3, ECTS:6
AUD409, Pediatric Audiology: Practice and Observation, C, T:0, P:6, C:3, ECTS:6

Total Compulsory: T:3, P:18, C:12, ECTS:23

Elective Courses (Select to reach 30 ECTS):
AUD411, Family Education of Hearing Impaired Children, E, T:2, P:2, C:3, ECTS:5
AUD413, Approach to Multi-Handicapped and Hearing Impaired Patients, E, T:2, P:0, C:2, ECTS:3
FHS403, Branding Strategies and Personal Branding, E, T:2, P:0, C:2, ECTS:3

Total Semester ECTS: 30

Prerequisites: 1st, 2nd and 3rd Year AUD coded compulsory courses are prerequisite for AUD407 and AUD409""",

        # 4th Year - 8th Semester
        """Fourth Year - Eighth Semester (Spring) - Compulsory Courses:
AUD402, Project Work II, C, T:0, P:4, C:2, ECTS:4
AUD404, Seminars in Audiology II, C, T:0, P:2, C:1, ECTS:3
AUD406, Hearing Aids: Practice and Observation, C, T:0, P:6, C:3, ECTS:6
AUD408, Electrophysiological Tests: Practice and Observation, C, T:0, P:6, C:3, ECTS:6
AUD410, Audiological Counselling, C, T:3, P:0, C:3, ECTS:4

Total Compulsory: T:3, P:16, C:11, ECTS:23

Elective Courses (Select to reach 30 ECTS):
AUD412, Rehabilitative Audiology: Practice, E, T:0, P:6, C:3, ECTS:5
AUD416, Pharmacology For Audiology/Speech And Language Therapy, E, T:2, P:0, C:2, ECTS:2
AUD418, Vestibular Laboratory Practice, E, T:0, P:4, C:2, ECTS:3

Total Semester ECTS: 30

Prerequisites:
- AUD303, AUD304, AUD405 coded courses are prerequisite for AUD406 and AUD408
- AUD401 is prerequisite for AUD402
- AUD403 is prerequisite for AUD404""",

        # ECTS Summary and Program Overview
        """Audiology Program ECTS Summary:
Total ECTS for all compulsory courses: 182
Total ECTS for all elective courses: 58
Total ECTS credits for graduation: 240

Program Focus Areas:
- Hearing assessment and diagnosis
- Vestibular system disorders
- Hearing aids and auditory implants
- Pediatric audiology
- Electrophysiological testing
- Auditory rehabilitation
- Speech and language disorders

Career Opportunities:
Clinical Audiologist
Pediatric Audiologist
Educational Audiologist
Industrial Audiologist
Research Audiologist
Hearing Aid Specialist
Vestibular Specialist
Academic and Research Positions

Professional Recognition:
Graduates are qualified to work in hospitals, clinics, rehabilitation centers, schools, hearing aid companies, and research institutions.""",

        # Key Prerequisites Summary
        """Important Prerequisites Summary:
- ENG101 → ENG102
- 1st & 2nd Year AUD courses → AUD214
- 1st, 2nd & 3rd Year AUD courses → AUD306, AUD407, AUD409
- AUD301 → AUD302
- AUD303 → AUD304
- AUD309 → AUD310
- AUD303, AUD304, AUD405 → AUD406, AUD408
- AUD401 → AUD402
- AUD403 → AUD404

Program Requirements:
- All AUD coded courses should be taken before professional practice courses
- Total ECTS for graduation: 240
- Total compulsory ECTS: 182
- Total elective ECTS: 58"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Health Sciences",
            "department": "Audiology",
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
            "document_type": "program_info",
            "content_type": "program_summary_careers"
        },
        {
            "document_type": "program_info",
            "content_type": "prerequisites_summary"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"audiology_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Audiology curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["hearing aids audiology courses"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_audiology_curriculum_to_chromadb()