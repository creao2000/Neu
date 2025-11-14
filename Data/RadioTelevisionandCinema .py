import chromadb
from chromadb.utils import embedding_functions

def add_radio_tv_cinema_curriculum_to_chromadb():
    """Add Radio, Television and Cinema curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_radio_tv_cinema",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_radio_tv_cinema",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_radio_tv_cinema")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF COMMUNICATION
DEPARTMENT OF RADIO, TELEVISION AND CINEMA
Bachelor of Arts in Radio, Television and Cinema

Program Duration: 4 years (8 semesters)
Degree: Bachelor of Arts
Total Credits for Graduation: Approximately 150

Legend:
C = Compulsory Course
E = Elective Course
K = Credit (Credits)""",

        # 1st Year - 1st Semester
        """First Year - First Semester (Fall) - Compulsory Courses:
İLF101, Introduction to Communication, C, K:3
İLF111, History of Culture, C, K:3
İLF171, Turkish I, C, K:2
İNG101, English I, C, K:2
AİT101, Principle of Atatürk I, C, K:2
KHM102, Introduction to Law, C, K:3
EKON111, Principle of Economy, C, K:3
İLF133, Life in University I, C, K:0

Total Compulsory: K:18
Total Semester Credits: 18""",

        # 1st Year - 2nd Semester
        """First Year - Second Semester (Spring) - Compulsory Courses:
İLF108, History of Communication, C, K:3
SOC122, Sociology, C, K:3
İLF172, Turkish II, C, K:2
İNG102, English II, C, K:2
AİT102, Principle of Atatürk II, C, K:2
RTS101, Introduction to Radio and Television, C, K:3
RTS331, History of Cinema, C, K:3
İLF134, Life in University II, C, K:0

Total Compulsory: K:18
Total Semester Credits: 18""",

        # 2nd Year - 3rd Semester
        """Second Year - Third Semester (Fall) - Compulsory Courses:
İLF208, Political Science, C, K:3
İLF217, Communication Theories, C, K:3
RTS203, Radio Programme Making, C, K:3
RTS422, Lighting and Camera, C, K:3
GZT209, Basic Photography, C, K:3
RTS329, Turkish Cinema, C, K:3

Total Compulsory: K:18
Total Semester Credits: 18""",

        # 2nd Year - 4th Semester
        """Second Year - Fourth Semester (Spring) - Compulsory Courses:
İLF202, Sociology for Communication, C, K:3
RTS330, Contemporary Turkish Cinema, C, K:3
RTS241, Editing I, C, K:3
RTS244, Cinematography, C, K:3
GİT203, History of Art, C, K:3
Elective Course, E, K:3

Total Compulsory: K:15
Total Elective: K:3
Total Semester Credits: 18""",

        # 3rd Year - 5th Semester
        """Third Year - Fifth Semester (Fall) - Compulsory Courses:
İLF303, Research Methods and Techniques in Social Sciences, C, K:3
İLF310, Communication Law, C, K:3
RTS301, Internal Internship I, C, K:3
RTS325, Reporting for Radio and Television, C, K:3
RTS432, Short Film Making, C, K:3
Elective Course, E, K:3

Total Compulsory: K:15
Total Elective: K:3
Total Semester Credits: 18""",

        # 3rd Year - 6th Semester
        """Third Year - Sixth Semester (Spring) - Compulsory Courses:
İLF311, Public Opinion Research, C, K:3
İLF341, Research of Mass Media, C, K:3
RTS205, TV Programme Making, C, K:3
RTS302, Internal Internship II, C, K:3
Elective Course, E, K:3
Elective Course, E, K:3

Total Compulsory: K:12
Total Elective: K:6
Total Semester Credits: 18""",

        # 4th Year - 7th Semester
        """Fourth Year - Seventh Semester (Fall) - Compulsory Courses:
İLF413, Media Ethics, C, K:3
İLF431, Political Communication, C, K:3
RTS321, Applied TV Studies, C, K:3
RTS407, Film Genres, C, K:3
Elective Course, E, K:3
Elective Course, E, K:3

Total Compulsory: K:12
Total Elective: K:6
Total Semester Credits: 18""",

        # 4th Year - 8th Semester
        """Fourth Year - Eighth Semester (Spring) - Compulsory Courses:
İLF405, Cultural Studies, C, K:3
İLF444, Communication and Modernity, C, K:3
RTS406, Film Criticism Analysis, C, K:3
RTS440, Department Project, C, K:3
Elective Course, E, K:3
Elective Course, E, K:3

Total Compulsory: K:12
Total Elective: K:6
Total Semester Credits: 18""",

        # Core Course Descriptions
        """Core Course Descriptions - Communication Foundation:

İLF101 - Introduction to Communication:
The main aim is to define what communication is and let students evaluate the concept of communication with a historical perspective.

İLF111 - History of Culture:
Introduces the conception of culture, explains civilizations' roles, and shows how cultural past is essential for new advancements. Compares technologies, trades, science, faith and art activities across civilizations.

İLF108 - History of Communication:
Gives a general outline of Turkish and European journalism as well as social, economic, political and cultural roots of the printing press.

SOC122 - Sociology:
Study of society and human interaction, focusing on why and how people live regularly in society. Examines relationships between individuals and global social processes.

İLF208 - Political Science:
Develops students' understanding of political science through active learning and presentations about different ideologies.

İLF217 - Communication Theories:
Helps students understand the intricacies of the communication field for professional development.

İLF303 - Research Methods in Social Sciences:
Provides tools for critically engaged research using interviewing, focus groups, historical research, ethnography, and textual analysis.

İLF310 - Law of Communication:
Presents fundamental concepts in communication law and understanding of legal systems.

İLF413 - Media Ethics:
Establishes importance of ethics philosophy in communication and media studies, covering media structures and new technologies.

İLF431 - Political Communication:
Introduction to theory and practice of political communication; role of media in campaigns and policymaking.

İLF405 - Cultural Studies:
Interdisciplinary field examining theoretical positions on culture and media including mass culture, ideology, and social resistance.

İLF444 - Communication and Modernity:
Introduction to formation of modernity and postmodernity, covering Enlightenment, modern state, media, and globalization.""",

        # Radio, TV and Cinema Course Descriptions
        """Radio, Television and Cinema Course Descriptions:

RTS101 - Introduction to Radio and Television:
Defines and explains historical evolution of radio and TV.

RTS331 - History of Cinema:
Understanding origins and history of film from narrative, social and aesthetic perspectives. Covers technological advances and global cinema.

RTS203 - Radio Programme Making:
Radio program production techniques, production stages, program types and broadcasting principles.

RTS422 - Lighting and Camera:
Practical training in lighting methods and camera techniques. Covers psychological atmosphere creation, lighting for character psychology, and scene emphasis.

GZT209 - Basic Photography:
Basic steps of photography, camera introduction, shooting techniques, chemical bathing and printing process.

RTS329 - Turkish Cinema:
Study of Yeşilçam cinema - capital structure, script, actors, audience, and cinema sociology. Different trends and generations in Turkish cinema.

RTS330 - Contemporary Turkish Cinema:
Focus on transition between Post-Yeşilçam and New Film Makers, especially post-1980's era.

RTS241 - Editing I:
Education on visual aesthetic within editing process, teaching functions and goals of editing with practical experiences.

RTS244 - Cinematography:
Explains elements that create a movie and relationships between them. Introduces cinematography terminology and basic concepts.

RTS301 - Internal Internship I:
Practical experience at NEU FM, NEU TV, NEU News Centre, graphic lab and photoshop labs. Following all phases of radio and TV program making.

RTS325 - Reporting for Radio and Television:
Radio and TV news report writing different from print media, with practical exercises.

RTS432 - Short Film Making:
Education on making short films from production process to screening process.

RTS205 - TV Programme Making:
Covers TV program types, production process, budget, research, synopsis writing, shooting, editing and all program phases.

RTS302 - Internal Internship II:
Continuation of RTS301, using faculty facilities to improve skills.

RTS321 - Applied TV Studies:
Information on lighting, sound, decoration, camera use, editing, interviewing, makeup, and anchoring.

RTS407 - Film Genres:
Introduction to film genres, their origins, and development in relation to genre theory.

RTS406 - Film Criticism and Analysis:
Critical analysis of visual materials, sound, colors, camera angles, and cultural context through examples.

RTS440 - Department Project:
Final graduation project where students demonstrate/screen their own project and defend it before faculty jury.

RTS341 - Script Writing:
First part focuses on script elements, story and character creation. Second part develops story, character development and script writing.""",

        # Program Summary and Career Opportunities
        """Radio, Television and Cinema Program Summary:
Degree: Bachelor of Arts in Radio, Television and Cinema
Duration: 4 years (8 semesters)
Total Credits: Approximately 150
Language of Instruction: English/Turkish

Program Focus Areas:
- Film Production and Direction
- Television Program Production
- Radio Broadcasting
- Cinematography and Lighting
- Film Editing and Post-Production
- Screenwriting and Story Development
- Film Criticism and Analysis
- Media Research and Theory

Core Competencies Developed:
- Film and television production techniques
- Camera operation and lighting
- Audio-visual editing
- Script writing and story development
- Media research and analysis
- Program planning and management
- Critical film analysis
- Ethical media practices

Career Opportunities:
Film Director
Television Producer
Radio Program Producer
Cinematographer
Film Editor
Screenwriter
TV Program Director
Film Critic
Media Researcher
Content Producer
Broadcast Journalist
Video Editor
Production Manager
Film Festival Organizer

Industry Sectors:
Television Stations
Radio Stations
Film Production Companies
Advertising Agencies
Media Houses
Streaming Platforms
Film Festivals
Post-Production Studios
Content Creation Companies
Educational Media""",

        # Course Progression and Specializations
        """Course Progression and Specialization Tracks:

Foundation Year (1st Year):
- Basic communication principles and theories
- Cultural and historical context
- Language and general education
- Introduction to radio, TV and cinema

Technical Development (2nd Year):
- Radio and TV program production
- Cinematography and lighting
- Photography and editing
- Turkish cinema history

Professional Application (3rd Year):
- Advanced research methods
- Internship and practical experience
- Short film making
- TV and radio reporting

Specialization and Portfolio (4th Year):
- Advanced TV studies and film genres
- Political communication and ethics
- Film criticism and analysis
- Department project and portfolio development

Specialization Tracks:
1. Film Production: Cinematography, editing, short film making, script writing
2. Television Production: TV program making, applied TV studies, lighting and camera
3. Radio Broadcasting: Radio program making, reporting, audio production
4. Film Studies: Film criticism, genre studies, Turkish cinema, cultural studies"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Communication",
            "department": "Radio, Television and Cinema",
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
            "course_type": "core",
            "document_type": "course_description",
            "content_type": "communication_courses"
        },
        {
            "course_type": "core",
            "document_type": "course_description",
            "content_type": "rtc_courses"
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
    ids = [f"rtc_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Radio, Television and Cinema curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["film production cinematography courses"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_radio_tv_cinema_curriculum_to_chromadb()