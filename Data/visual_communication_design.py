import chromadb
from chromadb.utils import embedding_functions

def add_visual_communication_design_curriculum_to_chromadb():
    """Add Visual Communication Design curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_visual_communication_design",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_visual_communication_design",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_visual_communication_design")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF COMMUNICATION
DEPARTMENT OF VISUAL COMMUNICATION DESIGN
Bachelor of Arts in Visual Communication Design

Program Duration: 4 years (8 semesters)
Degree: Bachelor of Arts
Total ECTS for Graduation: 240

Main website: https://iletisim.neu.edu.tr/?lang=en
Curriculum link: https://iletisim.neu.edu.tr/academic/academic-programmes/department-of-visual-communication-design/courses-2/?lang=en

Legend:
K = Credit (Credits)
A = ECTS (European Credit Transfer System)
C = Compulsory Course
E = Elective Course""",

        # 1st Semester
        """First Year - First Semester (Fall) - Compulsory Courses:
ILF101, Introduction to Communication, C, K:3, A:4
TUR101, Turkish Language and Spelling Rules I, C, K:2, A:2
ING101, English I, C, K:3, A:3
AIT101, Atatürk's Principles and Revolutionary History I, C, K:2, A:2
KHM102, Introduction to Law, C, K:3, A:4
ILF123, Basic Art Education, C, K:3, A:4
ILF125, Introduction to Computer Design, C, K:3, A:5
KAM100, Adapting to the Campus, C, K:0, A:2
BIL101, Information Technologies 1, C, K:3, A:4

Total Compulsory: K:22, A:30
Total Semester ECTS: 30""",

        # 2nd Semester
        """First Year - Second Semester (Spring) - Compulsory Courses:
ILF108, Communication History, C, K:3, A:7
ILF122, Sociology, C, K:3, A:7
TUR102, Turkish Language and Spelling Rules II, C, K:2, A:2
ING102, English II, C, K:3, A:3
AIT102, Atatürk's Principles and Revolutionary History II, C, K:2, A:2
ILF124, Basic Design, C, K:3, A:3
ILF234, Art History, C, K:3, A:2
KTK100, Cyprus Culture and History, C, K:2, A:2
KAR100, Career Planning, C, K:0, A:2

Total Compulsory: K:21, A:30
Total Semester ECTS: 30""",

        # 3rd Semester
        """Second Year - Third Semester (Fall) - Compulsory Courses:
ILF208, Political Science, C, K:3, A:5
ILF217, Communication Theories, C, K:3, A:5
ILF209, Basic Photography, C, K:3, A:5
ILF227, Graphic Design I, C, K:3, A:5
ILF215, Illustration, C, K:3, A:5
GIT303, Art Reviews, C, K:3, A:5

Total Compulsory: K:18, A:30
Total Semester ECTS: 30""",

        # 4th Semester
        """Second Year - Fourth Semester (Spring) - Compulsory Courses:
ILF202, Sociology of Communication, C, K:3, A:5
ILF244, Cinematography, C, K:3, A:5
GIT209, Photo-Graphic, C, K:3, A:5
ILF228, Graphic Design II, C, K:3, A:5
GIT207, Brand Design, C, K:3, A:5
GIT208, Media and Advertising Reviews, C, K:3, A:5

Total Compulsory: K:18, A:30
Total Semester ECTS: 30""",

        # 5th Semester
        """Third Year - Fifth Semester (Fall) - Compulsory Courses:
GIT405, Typography, C, K:3, A:5
ILF241, Fiction, C, K:3, A:5
ILF219, Basic Programming for New Media, C, K:3, A:5
GIT301, Graphic Animation I, C, K:3, A:5
GIT311, Publication Design, C, K:3, A:5
Elective Course, E, K:3, A:5

Total Compulsory: K:15, A:25
Total Elective: K:3, A:5
Total Semester ECTS: 30""",

        # 6th Semester
        """Third Year - Sixth Semester (Spring) - Compulsory Courses:
GIT309, Communication and Design, C, K:3, A:5
ILF232, Short Film Production, C, K:3, A:5
ILF428, Creative Writing, C, K:3, A:5
GIT302, Graphic Animation II, C, K:3, A:5
GIT322, Web Design, C, K:3, A:5
Elective Course, E, K:3, A:5

Total Compulsory: K:15, A:25
Total Elective: K:3, A:5
Total Semester ECTS: 30""",

        # 7th Semester
        """Fourth Year - Seventh Semester (Fall) - Compulsory Courses:
ILF413, Communication Ethics, C, K:3, A:5
GIT332, Creative Workshop, C, K:3, A:5
GIT407, Digital Game Design, C, K:3, A:5
Elective Course, E, K:3, A:5
Elective Course, E, K:3, A:5
Elective Course, E, K:3, A:5

Total Compulsory: K:9, A:15
Total Elective: K:9, A:15
Total Semester ECTS: 30""",

        # 8th Semester
        """Fourth Year - Eighth Semester (Spring) - Compulsory Courses:
ILF406, Cultural Studies, C, K:3, A:5
ILF444, Communication and Modernity, C, K:3, A:5
GIT440, Department Project, C, K:3, A:5
Elective Course, E, K:3, A:5
Elective Course, E, K:3, A:5
Elective Course, E, K:3, A:5

Total Compulsory: K:9, A:15
Total Elective: K:9, A:15
Total Semester ECTS: 30""",

        # Elective Courses (Sample)
        """Sample Elective Courses for Visual Communication Design:
GIT304, Advanced Photography, E, K:3, A:5
GIT306, Motion Graphics, E, K:3, A:5
GIT308, Interactive Media Design, E, K:3, A:5
GIT310, Advertising Design, E, K:3, A:5
GIT312, Packaging Design, E, K:3, A:5
GIT314, Corporate Identity Design, E, K:3, A:5
GIT316, Digital Illustration, E, K:3, A:5
GIT318, 3D Modeling and Animation, E, K:3, A:5
GIT320, User Interface Design, E, K:3, A:5
GIT324, Social Media Design, E, K:3, A:5
GIT326, Editorial Design, E, K:3, A:5
GIT328, Environmental Graphic Design, E, K:3, A:5
GIT330, Digital Portfolio Design, E, K:3, A:5""",

        # Program Summary and Career Opportunities
        """Visual Communication Design Program Summary:
Degree: Bachelor of Arts in Visual Communication Design
Duration: 4 years (8 semesters)
Total ECTS: 240
Language of Instruction: English/Turkish

Program Focus Areas:
- Graphic Design and Typography
- Digital Media and Animation
- Photography and Cinematography
- Web and Interactive Design
- Branding and Advertising
- Publication Design
- Digital Game Design
- Creative Writing and Fiction

Core Competencies Developed:
- Visual storytelling and narrative techniques
- Digital design software proficiency
- Creative problem-solving skills
- Communication theory application
- Technical design implementation
- Project management and presentation

Career Opportunities:
Graphic Designer
Art Director
Creative Director
Web Designer
UI/UX Designer
Motion Graphics Designer
Brand Identity Designer
Publication Designer
Advertising Specialist
Digital Media Producer
Game Designer
Photographer
Video Editor
Social Media Designer
Multimedia Artist

Industry Sectors:
Advertising Agencies
Design Studios
Publishing Houses
Media Companies
Game Development Studios
Corporate Communications
Freelance Design
Digital Marketing Agencies
Film and Television Production""",

        # Course Progression and Specializations
        """Course Progression and Specialization Tracks:

Foundation Year (1st Year):
- Basic art, design, and communication principles
- Technical and software fundamentals
- Cultural and historical context

Core Development (2nd Year):
- Advanced design techniques
- Photography and cinematography
- Graphic design principles
- Communication theories

Specialization (3rd Year):
- Typography and publication design
- Web and digital media
- Animation and programming
- Creative writing and fiction

Professional Preparation (4th Year):
- Advanced workshops and projects
- Digital game design
- Professional ethics
- Department project and portfolio development

Specialization Tracks:
1. Digital Media Track: Web design, animation, game design
2. Graphic Design Track: Typography, publication, brand design
3. Visual Storytelling Track: Photography, cinematography, creative writing
4. Advertising Track: Brand design, media reviews, creative workshops"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Communication",
            "department": "Visual Communication Design",
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
            "content_type": "program_summary_careers"
        },
        {
            "document_type": "program_info",
            "content_type": "specialization_tracks"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"vcd_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Visual Communication Design curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["graphic design animation courses"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_visual_communication_design_curriculum_to_chromadb()