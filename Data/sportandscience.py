import chromadb
from chromadb.utils import embedding_functions

def add_sports_sciences_curriculum_to_chromadb():
    """Add Sports Sciences and Physical Education Teaching curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_sports_sciences",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_sports_sciences",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_sports_sciences")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """Sports Sciences and Physical Education Teaching Curriculum Overview
Degree: Bachelor of Science in Sports Sciences and Physical Education Teaching
Program Duration: 4 years (8 semesters)
Program Type: Teacher Education Program

Legend:
Z/S: Mandatory/Optional (Zorunlu/Seçmeli)
T: Theoretical Hours
P: Practical/Lab Hours
K: Credits
A: ECTS (AKTS)

Program Focus: Preparing physical education teachers with comprehensive sports science knowledge""",

        # 1st Year - 1st Semester
        """First Year - First Semester Courses:
AEF109, Introduction to Education, Type: Z, T: 2, P: 0, K: 2, A: 4
AİT101, Atatürk's Principles and History of Revolution 1, Type: Z, T: 2, P: 0, K: 2, A: 2
İNG101, Foreign Language 1, Type: Z, T: 3, P: 0, K: 3, A: 3
TUR101, Turkish Language 1, Type: Z, T: 2, P: 0, K: 2, A: 2
BİL101, Information Technologies, Type: Z, T: 3, P: 0, K: 3, A: 4
OSB121, Introduction to Sports Sciences, Type: Z, T: 3, P: 0, K: 3, A: 3
OSB123, Human Anatomy and Kinesiology, Type: Z, T: 3, P: 0, K: 3, A: 4
OSB135, Movement Training, Type: Z, T: 2, P: 2, K: 3, A: 3
OSB205, Team Sports 1 (Basketball), Type: Z/S, T: 1, P: 2, K: 2, A: 3
KAM100, Adaptation to Campus, Type: Z, T: 0, P: 0, K: 0, A: 2

Total: Mandatory: 21, Practical: 4, Credits: 23, ECTS: 30""",

        # 1st Year - 2nd Semester
        """First Year - Second Semester Courses:
AEF104, Educational Psychology, Type: Z, T: 2, P: 0, K: 2, A: 4
AEF113, Philosophy & Sociology of Education, Type: Z, T: 2, P: 0, K: 2, A: 4
AİT102, Atatürk's Principles & History of Revolution 2, Type: Z, T: 2, P: 0, K: 2, A: 2
İNG102, Foreign Language 2, Type: Z, T: 3, P: 0, K: 3, A: 3
TUR102, Turkish Language 2, Type: Z, T: 2, P: 0, K: 2, A: 2
OSB122, Health Information & First Aid, Type: Z, T: 2, P: 2, K: 3, A: 3
OSB124, Gymnastics, Type: Z, T: 1, P: 2, K: 2, A: 4
OSB126, Athletics, Type: Z, T: 2, P: 2, K: 3, A: 4
KTK100, Cyprus Culture & History, Type: Z, T: 2, P: 0, K: 2, A: 2
KAR100, Career Planning, Type: Z, T: 0, P: 0, K: 0, A: 2

Total: Mandatory: 18, Practical: 6, Credits: 21, ECTS: 30""",

        # 2nd Year - 1st Semester
        """Second Year - First Semester Courses:
AEF362, Information Media & Technologies Literacy, Type: Z, T: 2, P: 0, K: 2, A: 4
AEF203, Teaching Principles & Methods, Type: Z, T: 2, P: 0, K: 2, A: 4
AEF, Elective 1, Type: S, T: 2, P: 0, K: 2, A: 4
GEN, Elective 1, Type: S, T: 2, P: 0, K: 2, A: 3
BSÖ, Elective 1, Type: S, T: 2, P: 0, K: 2, A: 4
BSÖ213, Physical Education & Sports Learning & Teaching, Type: Z, T: 2, P: 0, K: 2, A: 4
OSB201, Motor Development, Type: Z, T: 3, P: 0, K: 3, A: 4
OSB305, Team Sports 2, Type: Z/S, T: 1, P: 2, K: 2, A: 3

Total: Mandatory: 16, Practical: 2, Credits: 17, ECTS: 30""",

        # 2nd Year - 2nd Semester
        """Second Year - Second Semester Courses:
AEF228, Instructional Technologies, Type: Z, T: 2, P: 0, K: 2, A: 5
AEF206, Research Methods in Education, Type: Z, T: 2, P: 0, K: 2, A: 4
AEF, Elective 2, Type: S, T: 2, P: 0, K: 2, A: 4
GEN, Elective 2, Type: S, T: 2, P: 0, K: 2, A: 3
BSÖ, Elective 2, Type: S, T: 2, P: 0, K: 2, A: 4
BSÖ210, Physical Education & Sports Teaching Programs, Type: Z, T: 2, P: 0, K: 2, A: 2
OSB202, Exercise Physiology, Type: Z, T: 3, P: 0, K: 3, A: 3
OSB206, Team Sports 2 (Football), Type: Z/S, T: 1, P: 2, K: 2, A: 3
OSB106, Rhythm Training & Dance, Type: Z, T: 1, P: 2, K: 2, A: 2

Total: Mandatory: 17, Practical: 4, Credits: 19, ECTS: 30""",

        # 3rd Year - 1st Semester
        """Third Year - First Semester Courses:
AEF312, Classroom Management, Type: Z, T: 2, P: 0, K: 2, A: 3
GEN203, Community Service Practices, Type: Z, T: 1, P: 2, K: 2, A: 3
AEF, Elective 3, Type: S, T: 2, P: 0, K: 2, A: 4
GEN, Elective 3, Type: S, T: 2, P: 0, K: 2, A: 3
BSÖ, Elective 3, Type: S, T: 2, P: 0, K: 2, A: 4
OSB307, Training Theory, Type: Z, T: 3, P: 0, K: 3, A: 3
AEF305, Measurement & Evaluation in Education, Type: Z, T: 2, P: 0, K: 2, A: 4
BSÖ314, Physical Fitness, Type: Z, T: 2, P: 0, K: 2, A: 3
OSB321, Swimming, Type: Z, T: 1, P: 2, K: 2, A: 3

Total: Mandatory: 17, Practical: 4, Credits: 19, ECTS: 30""",

        # 3rd Year - 2nd Semester
        """Third Year - Second Semester Courses:
BSÖ317, Physical Education & Sports Teaching, Type: Z, T: 1, P: 2, K: 2, A: 4
AEF361, Entrepreneurship & Leadership, Type: Z, T: 2, P: 0, K: 2, A: 4
AEF, Elective 4, Type: S, T: 2, P: 0, K: 2, A: 4
GEN, Elective 4, Type: S, T: 2, P: 0, K: 2, A: 3
BSÖ, Elective 4, Type: S, T: 2, P: 0, K: 2, A: 4
OSB302, Skill Learning in Sports, Type: Z, T: 2, P: 0, K: 2, A: 3
OSB304, Team Sports 4 (Handball), Type: Z/S, T: 1, P: 2, K: 2, A: 3
OSB309, Outdoor Sports, Type: Z, T: 1, P: 2, K: 2, A: 3
OSB, Racquet Sports, Type: S, T: 1, P: 2, K: 2, A: 2

Total: Mandatory: 14, Practical: 8, Credits: 18, ECTS: 30""",

        # 4th Year - 1st Semester
        """Fourth Year - First Semester Courses:
AEF405, Teaching Practice 1, Type: Z, T: 2, P: 6, K: 5, A: 10
AEF411, Special Education & Inclusion, Type: Z, T: 2, P: 0, K: 2, A: 4
AEF, Elective 5, Type: S, T: 2, P: 0, K: 2, A: 4
BSÖ, Elective 5, Type: S, T: 2, P: 0, K: 2, A: 4
BSÖ411, Folk Dances, Type: Z, T: 1, P: 2, K: 2, A: 3
OSB401, Sports Nutrition, Type: Z, T: 2, P: 0, K: 2, A: 3
OSB415, Educational Games, Type: Z, T: 1, P: 2, K: 2, A: 2

Total: Mandatory: 12, Practical: 10, Credits: 17, ECTS: 30""",

        # 4th Year - 2nd Semester
        """Fourth Year - Second Semester Courses:
AEF410, Teaching Practice 2, Type: Z, T: 2, P: 6, K: 5, A: 10
AEF412, Guidance in Schools, Type: Z, T: 2, P: 0, K: 2, A: 4
AEF, Elective 6, Type: S, T: 2, P: 0, K: 2, A: 4
BSÖ, Elective 6, Type: S, T: 2, P: 0, K: 2, A: 4
OSB402, Sports Management & Organization, Type: Z, T: 3, P: 0, K: 3, A: 4
OSB404, Physical Activity & Health, Type: Z, T: 2, P: 0, K: 2, A: 2
BSÖ410, Adapted Physical Education & Sports, Type: Z, T: 2, P: 0, K: 2, A: 2

Total: Mandatory: 15, Practical: 6, Credits: 18, ECTS: 30""",

        # Elective Courses
        """Elective Course Pool - Sample Options:
Sports Sciences Electives (BSÖ):
OSB203, Biomechanics, T: 2, P: 0, K: 2, A: 4
BSÖ323, Evaluation of In-Class Learning, T: 2, P: 0, K: 2, A: 4
OSB213, Leisure Education, T: 2, P: 0, K: 2, A: 4
BSÖ445, Physical Education Teaching Models, T: 2, P: 0, K: 2, A: 4
BSÖ216, Sociology of Physical Education, T: 2, P: 0, K: 2, A: 4

Education Electives (AEF):
Various educational theory and methodology courses

General Electives (GEN):
Interdisciplinary courses from other faculties

Additional Sports Electives:
- Advanced Team Sports
- Individual Sports
- Martial Arts
- Adventure Sports
- Sports Psychology
- Sports Marketing""",

        # Program Summary
        """Sports Sciences and Physical Education Teaching Program Summary:
Total Courses: 69
Total Electives: 17 (24.64% of program)
Total Credits: 152
Total ECTS: 240
Degree: Bachelor of Science

Program Structure:
- 8 semesters over 4 years
- Comprehensive teaching practice in final year
- Balanced theoretical and practical training
- Progressive specialization through electives

Key Competencies Developed:
- Physical education teaching methodologies
- Sports science knowledge (anatomy, physiology, biomechanics)
- Classroom management and educational psychology
- Sports coaching and training principles
- Health and fitness assessment
- Adapted physical education

Teaching Practice:
- AEF405: Teaching Practice 1 (5 credits, 10 ECTS)
- AEF410: Teaching Practice 2 (5 credits, 10 ECTS)
- Total teaching practice: 10 credits, 20 ECTS""",

        # Career Opportunities
        """Career Opportunities for Graduates:
Educational Settings:
- Physical Education Teacher (Primary/Secondary Schools)
- Sports Academy Instructor
- School Sports Coordinator
- Adaptive Physical Education Specialist

Sports Industry:
- Sports Coach (Various Disciplines)
- Fitness Trainer and Instructor
- Sports Club Manager
- Recreation Program Coordinator

Health and Wellness:
- Corporate Wellness Coordinator
- Community Health Educator
- Fitness Center Manager
- Personal Trainer

Sports Management:
- Sports Event Organizer
- Sports Facility Manager
- Youth Sports Program Director
- Sports Development Officer

Further Education:
- Master's in Sports Sciences
- Master's in Education
- Sports Psychology
- Sports Management
- PhD in related fields""",

        # Program Features
        """Program Distinctive Features:
Integrated Approach:
- Combines sports sciences with teacher education
- Balance between theoretical knowledge and practical skills
- Progressive teaching experience throughout the program

Practical Training:
- Extensive hands-on sports training
- Teaching practice in real educational settings
- Community service requirements

Specialization Options:
- Wide range of elective courses
- Focus on individual sports interests
- Opportunities for coaching certifications

Professional Development:
- Career planning integrated into curriculum
- Entrepreneurship and leadership training
- Research methods and academic writing skills

International Perspective:
- Foreign language requirement
- Cultural and historical education
- Adaptable to international teaching standards"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Sports Sciences",
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
            "document_type": "course_list",
            "content_type": "elective_courses"
        },
        {
            "document_type": "program_info",
            "content_type": "program_summary"
        },
        {
            "document_type": "program_info",
            "content_type": "career_opportunities"
        },
        {
            "document_type": "program_info",
            "content_type": "program_features"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"sports_sci_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Sports Sciences curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["physical education teaching sports sciences"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_sports_sciences_curriculum_to_chromadb()