import chromadb
from chromadb.utils import embedding_functions

def add_filmmaking_broadcasting_curriculum_to_chromadb():
    """Add Filmmaking and Broadcasting curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_filmmaking_broadcasting",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_filmmaking_broadcasting",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_filmmaking_broadcasting")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF COMMUNICATION
DEPARTMENT OF FILMMAKING AND BROADCASTING
Bachelor of Arts in Filmmaking and Broadcasting

Program Duration: 4 years (8 semesters)
Total Credits: 240 (30 per semester)

Main website: https://iletisim.neu.edu.tr/?lang=en
Curriculum link: https://iletisim.neu.edu.tr/academic/academic-programmes/department-of-filmmaking-and-broadcasting/courses/?lang=en

Legend:
T = Theoretical Hours
P = Practical Hours
C = Credits""",

        # 1st Year - Fall Semester
        """First Year - Fall Semester - Compulsory Courses:
FLM100, Project Proposal I, T:3, P:3, C:6
FLM102, Cinema History, T:4, P:0, C:4
FLM104, Screen Writing I, T:3, P:3, C:6
FLM106, New Media Technologies, T:2, P:2, C:4
FLM108, Cinematography I, T:3, P:2, C:6
FLM110, Sound Recording I, T:1, P:3, C:4

Total Semester Credits: 30""",

        # 1st Year - Spring Semester
        """First Year - Spring Semester - Compulsory Courses:
FLM101, Directing I, T:3, P:3, C:6
FLM103, Edit Theory (The Art of Editing), T:2, P:2, C:4
FLM105, Script Supervising, T:3, P:3, C:6
FLM107, Editing I, T:2, P:2, C:4
FLM109, Cinematography II, T:3, P:2, C:6
FLM111, Sound Editing & Design I, T:1, P:3, C:4

Total Semester Credits: 30""",

        # 2nd Year - Fall Semester
        """Second Year - Fall Semester - Compulsory Courses:
FLM200, Project Proposal II, T:3, P:3, C:6
FLM202, Producing, T:2, P:2, C:4
FLM204, Screenwriting II, T:3, P:3, C:6
FLM206, Directing II, T:2, P:2, C:4
FLM208, Cinematography III, T:3, P:3, C:6
FLM Elective, Elective Course, T:2, P:2, C:4

Total Semester Credits: 30""",

        # 2nd Year - Spring Semester
        """Second Year - Spring Semester - Compulsory Courses:
FLM201, Project, T:3, P:3, C:6
FLM203, Production Management, T:3, P:3, C:6
FLM205, Sound Editing & Design II, T:1, P:3, C:4
FLM207, Editing II, T:2, P:2, C:4
FLM209, Career & Portfolio Development, T:3, P:3, C:6
FLM Elective, Elective Course, T:2, P:2, C:4

Total Semester Credits: 30""",

        # 3rd Year - Fall Semester
        """Third Year - Fall Semester - Compulsory Courses:
FLM310, Introduction to Radio & TV, T:3, P:3, C:6
FLM312, Studio News, T:4, P:0, C:4
FLM314, History of Radio & TV, T:3, P:3, C:6
FLM316, Advanced Scenario and Casting, T:3, P:3, C:6
FLM318, Film Genres, T:2, P:2, C:4
FLM Elective, Elective Course, T:1, P:3, C:4

Total Semester Credits: 30""",

        # 3rd Year - Spring Semester
        """Third Year - Spring Semester - Compulsory Courses:
FLM311, Storyboard, T:2, P:2, C:4
FLM313, Radio Programme Making, T:3, P:3, C:6
FLM315, Semiotics, T:2, P:2, C:4
FLM317, Art Direction, T:3, P:3, C:6
FLM319, Writing for TV, T:3, P:3, C:6
FLM Elective, Elective Course, T:1, P:3, C:4

Total Semester Credits: 30""",

        # 4th Year - Fall Semester
        """Fourth Year - Fall Semester - Compulsory Courses:
FLM410, TV Programme Making, T:4, P:4, C:8
FLM412, Documentary Making, T:3, P:3, C:6
FLM414, Film Criticism, T:2, P:2, C:4
FLM Elective, Elective Course, T:2, P:2, C:4
FLM Elective, Elective Course, T:2, P:2, C:4

Total Semester Credits: 30""",

        # 4th Year - Spring Semester
        """Fourth Year - Spring Semester - Compulsory Courses:
FLM411, Portfolio Presentation, T:3, P:3, C:6
FLM413, Final Projects, T:4, P:6, C:10
FLM Elective, Elective Course, T:2, P:2, C:4
FLM Elective, Elective Course, T:2, P:2, C:4

Total Semester Credits: 30

Program Total Credits: 240""",

        # Elective Courses
        """Elective Courses - Filmmaking and Broadcasting:

Second Year Electives:
FLM210, Documentary Theory & Practice, T:2, P:2, C:4
FLM211, TV Advertising, T:2, P:2, C:4
FLM212, Visual Effects, T:2, P:2, C:4
FLM213, Advance Sound Recording II, T:2, P:2, C:4
FLM214, Sound Recording II, T:2, P:2, C:4
FLM216, Introduction to Communication, T:2, P:2, C:4

Third Year Electives:
FLM320, Art History, T:2, P:2, C:4
FLM321, Photography, T:2, P:2, C:4
FLM322, World Literature, T:2, P:2, C:4
FLM323, Storyboard Drawing, T:2, P:2, C:4
FLM325, Studio Photography, T:2, P:2, C:4
FLM326, Introduction to Philosophy, T:2, P:2, C:4
FLM326, Visual Culture, T:2, P:2, C:4

Fourth Year Electives:
FLM416, Animation, T:2, P:2, C:4
FLM418, Music in Film, T:2, P:2, C:4
FLM420, Computer Aided Design, T:2, P:2, C:4""",

        # Course Descriptions - Core Production Courses
        """Core Production and Technical Courses Description:

Production and Directing:
FLM100/200, Project Proposal I/II: Development of film project concepts and proposals
FLM101/206, Directing I/II: Fundamentals and advanced techniques of film direction
FLM201, Project: Comprehensive film production project
FLM413, Final Projects: Capstone film production project

Screenwriting and Story Development:
FLM104/204, Screen Writing I/II: Scriptwriting fundamentals and advanced techniques
FLM105, Script Supervising: Continuity and script management during production
FLM316, Advanced Scenario and Casting: Advanced script development and actor selection
FLM319, Writing for TV: Television scriptwriting and format development

Cinematography and Visual Techniques:
FLM108/109/208, Cinematography I/II/III: Camera operation, lighting, and visual storytelling
FLM311, Storyboard: Visual planning and shot composition
FLM317, Art Direction: Production design and visual aesthetics

Editing and Post-Production:
FLM103, Edit Theory: Theoretical foundations of film editing
FLM107/207, Editing I/II: Practical editing techniques and software
FLM205, Sound Editing & Design II: Advanced audio post-production

Sound Production:
FLM110, Sound Recording I: Location sound recording techniques
FLM111, Sound Editing & Design I: Basic audio editing and design""",

        # Broadcasting and Media Courses Description
        """Broadcasting and Media Studies Courses:

Radio and Television Production:
FLM310, Introduction to Radio & TV: Fundamentals of broadcast media
FLM312, Studio News: Television news production and presentation
FLM313, Radio Programme Making: Radio production and programming
FLM410, TV Programme Making: Television program production

Media Theory and Studies:
FLM102, Cinema History: Historical development of cinema
FLM314, History of Radio & TV: Evolution of broadcast media
FLM315, Semiotics: Study of signs and symbols in media
FLM318, Film Genres: Analysis of different film genres
FLM414, Film Criticism: Critical analysis and evaluation of films

Production Management:
FLM202, Producing: Film production management and financing
FLM203, Production Management: Organizational aspects of film production
FLM209, Career & Portfolio Development: Professional preparation and portfolio creation
FLM411, Portfolio Presentation: Final portfolio presentation and career preparation""",

        # Program Summary and Career Opportunities
        """Filmmaking and Broadcasting Program Summary:
Degree: Bachelor of Arts in Filmmaking and Broadcasting
Duration: 4 years (8 semesters)
Total Credits: 240
Faculty: Faculty of Communication

Program Focus Areas:
- Film Production and Direction
- Screenwriting and Story Development
- Cinematography and Visual Arts
- Editing and Post-Production
- Sound Design and Recording
- Television and Radio Production
- Documentary Filmmaking
- Media Theory and Criticism

Technical Skills Developed:
- Camera Operation and Lighting
- Digital Editing Software
- Sound Recording and Design
- Scriptwriting and Storyboarding
- Production Management
- Broadcast Studio Operations
- Visual Effects and Animation
- Portfolio Development

Career Opportunities:
Film Director
Cinematographer
Screenwriter
Film Editor
Sound Designer
Producer
TV Program Director
Radio Producer
Documentary Filmmaker
Film Critic
Production Manager
Broadcast Technician
Content Creator
Media Consultant

Industry Applications:
- Film and Television Production
- Advertising and Commercial Production
- Documentary Filmmaking
- Radio Broadcasting
- Digital Media Content Creation
- Corporate Video Production
- Event Coverage and Live Broadcasting
- Educational Media Production
- Entertainment Industry"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Communication",
            "department": "Filmmaking and Broadcasting",
            "degree": "Bachelor",
            "document_type": "program_info",
            "content_type": "general_info"
        },
        {
            "year": "1",
            "semester": "1",
            "document_type": "course_list",
            "content_type": "first_year_fall_semester"
        },
        {
            "year": "1",
            "semester": "2",
            "document_type": "course_list",
            "content_type": "first_year_spring_semester"
        },
        {
            "year": "2",
            "semester": "1",
            "document_type": "course_list",
            "content_type": "second_year_fall_semester"
        },
        {
            "year": "2",
            "semester": "2",
            "document_type": "course_list",
            "content_type": "second_year_spring_semester"
        },
        {
            "year": "3",
            "semester": "1",
            "document_type": "course_list",
            "content_type": "third_year_fall_semester"
        },
        {
            "year": "3",
            "semester": "2",
            "document_type": "course_list",
            "content_type": "third_year_spring_semester"
        },
        {
            "year": "4",
            "semester": "1",
            "document_type": "course_list",
            "content_type": "fourth_year_fall_semester"
        },
        {
            "year": "4",
            "semester": "2",
            "document_type": "course_list",
            "content_type": "fourth_year_spring_semester"
        },
        {
            "course_type": "elective",
            "document_type": "course_list",
            "content_type": "elective_courses"
        },
        {
            "course_type": "core",
            "document_type": "course_description",
            "content_type": "production_courses"
        },
        {
            "course_type": "core",
            "document_type": "course_description",
            "content_type": "broadcasting_courses"
        },
        {
            "document_type": "program_info",
            "content_type": "program_summary_careers"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"filmmaking_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Filmmaking and Broadcasting curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["filmmaking cinematography directing screenwriting"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_filmmaking_broadcasting_curriculum_to_chromadb()