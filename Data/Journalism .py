import chromadb
from chromadb.utils import embedding_functions

def add_journalism_curriculum_to_chromadb():
    """Add Journalism curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_journalism",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_journalism",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_journalism")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF COMMUNICATION
DEPARTMENT OF JOURNALISM
Bachelor of Arts in Journalism

Program Duration: 4 years (8 semesters)
Total Credits: Not specified (course-based system)

Main website: https://iletisim.neu.edu.tr/?lang=en
Curriculum link: https://iletisim.neu.edu.tr/academic/academic-programmes/department-of-journalism/courses/?lang=en

Program Focus:
- News Writing and Reporting
- Digital and New Media Journalism
- Multimedia Storytelling
- Data Journalism and Verification
- Media Ethics and Law
- Political Communication
- Investigative Journalism""",

        # 1st Year - Fall Semester
        """First Year - Fall Semester - Compulsory Courses:
CMN101, Introduction to Communication, Credit:3
HIST103, History of Civilization, Credit:3
AIT103, Principles of Ataturk, Credit:2
ENG101, English I, Credit:3
ECON111, Principle of Economy, Credit:3
CMN106, New Media Technologies, Credit:3
YIT101, Turkish for Foreigners, Credit:2

Total Semester Credits: 19""",

        # 1st Year - Spring Semester
        """First Year - Spring Semester - Compulsory Courses:
CMN108, History of Communication, Credit:3
SOC122, Sociology, Credit:3
AIT104, Principles of Atatürk, Credit:2
ENG102, English II, Credit:3
CMN100, New Media Journalism, Credit:3
JRN128, Computer Skills for New Media, Credit:3
YIT102, Turkish for Foreigners, Credit:2

Total Semester Credits: 19""",

        # 2nd Year - Fall Semester
        """Second Year - Fall Semester - Compulsory Courses:
CMN208, Political Science, Credit:3
CMN217, Communication Theories, Credit:3
JRN205, Introduction to News Writing, Credit:3
JRN209, Basic Photography, Credit:3
JRN219, Basic Programming for New Media, Credit:3
Elective, Elective Course, Credit:3

Total Semester Credits: 18""",

        # 2nd Year - Spring Semester
        """Second Year - Spring Semester - Compulsory Courses:
CMN202, Communication Sociology, Credit:3
CMN212, Politics of Mass Media, Credit:3
JRN220, Audio, Image and Video Reporting, Credit:3
JRN309, Press Photography, Credit:3
Elective, Elective Course, Credit:3
Elective, Elective Course, Credit:3

Total Semester Credits: 18""",

        # 3rd Year - Fall Semester
        """Third Year - Fall Semester - Compulsory Courses:
CMN303, Research Methods and Techniques in Social Sciences, Credit:3
CMN310, Law of Communication, Credit:3
JRN301, Techniques of News Writing, Credit:3
JRN306, Techniques of Publishing in Journalism, Credit:3
JRN311, Course Training, Credit:0
Elective, Elective Course, Credit:3
Elective, Elective Course, Credit:3

Total Semester Credits: 18""",

        # 3rd Year - Spring Semester
        """Third Year - Spring Semester - Compulsory Courses:
JRN320, Data Journalism and Verification, Credit:3
CMN341, Research of Mass Media, Credit:3
JRN324, New Media Studies, Credit:3
JRN326, New Media Design, Credit:3
Elective, Elective Course, Credit:3
Elective, Elective Course, Credit:3

Total Semester Credits: 18""",

        # 4th Year - Fall Semester
        """Fourth Year - Fall Semester - Compulsory Courses:
CMN413, Media Ethics, Credit:3
CMN431, Political Communication, Credit:3
JRN433, Rights-Oriented Journalism, Credit:3
JRN435, Editing of Digital News, Credit:3
Elective, Elective Course, Credit:3
Elective, Elective Course, Credit:3

Total Semester Credits: 18""",

        # 4th Year - Spring Semester
        """Fourth Year - Spring Semester - Compulsory Courses:
CMN405, Cultural Studies, Credit:3
CMN444, Communication and Modernity, Credit:3
JRN440, Department Project, Credit:3
CMN446, New Media and Pluralism, Credit:3
Elective, Elective Course, Credit:3
Elective, Elective Course, Credit:3

Total Semester Credits: 18

Total Program Credits: Approximately 146""",

        # Core Journalism Courses Description
        """Core Journalism Courses Description:

JRN205, Introduction to News Writing: Basic principles and practice of journalism, organizing news stories, gathering facts through interviewing and research, developing sources, crafting leads and endings.

JRN209, Basic Photography: History of photography, composition and context, basic principles of capturing quality images for journalism.

JRN219, Basic Programming for New Media: Programming languages, tools and terminology for new media, creating programming projects for digital platforms.

JRN220, Audio, Image and Video Reporting: Digital technology for online news making, video journalism techniques for online media outlets.

JRN301, Techniques of News Writing: Advanced news writing for different story types (hard, soft, features), reporting and editing skills, ethical framework.

JRN306, Techniques of Publishing in Journalism: All stages of newspaper design until publication.

JRN309, Press Photography: Importance of photography in journalism, collecting, editing, and presenting photographic images for news publication.

JRN311, Course Training: Practical application of journalism knowledge in media organizations.

JRN320, Data Journalism and Verification: Data discovery, collection, cleanup, analysis, visualization processes, open data and information rights.

JRN324, New Media Studies: Theories and concepts about new information techniques and technologies.

JRN326, New Media Design: Social, economic and managerial processes related to creativity in new media, social networks in cyberspace.

JRN433, Rights-Oriented Journalism: Human rights law and international frameworks, ethics of human dignity, reporting human rights violations.

JRN435, Editing of Digital News: News broadcasting and editing processes in new media, organizing relationship between writing and visual elements.

JRN440, Departmental Project: Original graduation project based on student's topic of interest.""",

        # Communication and Theory Courses Description
        """Communication and Theory Courses Description:

CMN101, Introduction to Communication: Fundamental concepts in communication, historical development of media sectors.

CMN106, New Media Technologies: Digitalization of media, evolution of communication technologies and their effects on human interactions.

CMN108, History of Communication: Historical development of communication media.

CMN202, Communication Sociology: Fundamental concepts in sociology connected to communication studies.

CMN208, Political Science: Understanding political science concepts and ideologies.

CMN212, Politics of Mass Media: Media influence on politics, agenda setting and public opinion.

CMN217, Communication Theories: Intricacies of the communication field for professional development.

CMN303, Research Methods: Qualitative research methods including interviewing, focus groups, ethnography, and textual analysis.

CMN310, Communication Law: Fundamental concepts in communication law and legal systems.

CMN341, Research of Mass Media: Study of mass communication and its effects on behavior, attitudes, and opinions.

CMN413, Media Ethics: Philosophy of ethics in communication and media studies, ethical frameworks.

CMN431, Political Communication: Theory and practice of political communication, media's role in campaigns and policymaking.

CMN405, Cultural Studies: Interdisciplinary perspectives on culture and society, media texts analysis.

CMN444, Communication and Modernity: Formation of modernity and postmodernity, communication aspects of social processes.

CMN446, New Media and Pluralism: New media effects on democracy and pluralism prospects.""",

        # Elective Courses Description
        """Elective Courses Description:

Journalism Electives:
JRN201, Basic Journalism: Principles and practices of journalism, journalism's role in democratic society.
JRN206, Interviewing Techniques: Preparation, conduct, and writing of interviews for journalism.
JRN212, New Information Techniques: Economic, political, technological changes in journalism since Industrial Revolution.
JRN401, Investigative Journalism: Identifying investigative stories, gathering and reporting investigative news.

Film and Media Electives:
FLM102, History of Cinema: Emergence and evolution of cinema throughout the 20th Century.
FLM231, Basic Concepts in Sound and Image: Basic concepts and techniques for capturing quality sound and image.
FLM310, Introduction to Radio and TV: History, equipment, news production, and broadcasting principles.
FLM315, Semiology: Principles of semiotics, semiotic analysis and representation in cinema.
FLM326, Visual Culture: Social theory of visuality, image production in local and global culture.
FLM328, Introduction to Philosophy: Classic works of Western philosophers, fundamental problems of philosophy.
FLM414, Film Analysis: Critical analysis in cinema, understanding film language.

Public Relations and Advertising:
PRA332, Advertising Applications: Strategic planning for communication campaigns, marketing concepts.
PRA333, New Media and Digital Applications: Information society, new media technologies and digital applications.

Radio and Television:
RTC325, Radio and Television News: Essential skills for radio and television news production.""",

        # Program Summary and Career Opportunities
        """Journalism Program Summary:
Degree: Bachelor of Arts in Journalism
Duration: 4 years (8 semesters)
Faculty: Faculty of Communication

Program Focus Areas:
- Digital and Multimedia Journalism
- News Writing and Reporting
- Data Journalism and Verification
- Media Ethics and Law
- Political Communication
- Investigative Reporting
- New Media Technologies
- Visual Storytelling and Photography

Technical Skills Developed:
- News Writing and Editing
- Digital Storytelling
- Data Analysis and Visualization
- Multimedia Production
- Interviewing Techniques
- Research Methods
- Ethical Decision Making
- Digital Platform Management

Career Opportunities:
News Reporter
Digital Journalist
Investigative Reporter
Data Journalist
Multimedia Producer
News Editor
Photojournalist
Broadcast Journalist
Content Creator
Social Media Manager
Political Correspondent
Academic and Research Positions

Industry Applications:
- Newspaper and Magazine Publishing
- Online News Platforms
- Broadcast Media (TV and Radio)
- Digital Media Companies
- News Agencies
- Corporate Communications
- Non-profit Organizations
- Government and Public Sector
- Media Research and Analysis"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Communication",
            "department": "Journalism",
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
            "course_type": "core",
            "document_type": "course_description",
            "content_type": "journalism_courses"
        },
        {
            "course_type": "theory",
            "document_type": "course_description",
            "content_type": "communication_courses"
        },
        {
            "course_type": "elective",
            "document_type": "course_description",
            "content_type": "elective_courses"
        },
        {
            "document_type": "program_info",
            "content_type": "program_summary_careers"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"journalism_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Journalism curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["news writing digital journalism media ethics"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_journalism_curriculum_to_chromadb()