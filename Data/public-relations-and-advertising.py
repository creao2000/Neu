import chromadb
from chromadb.utils import embedding_functions

def add_public_relations_curriculum_to_chromadb():
    """Add Public Relations and Publicity curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_public_relations",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_public_relations",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_public_relations")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF COMMUNICATION
DEPARTMENT OF PUBLIC RELATIONS AND PUBLICITY
Bachelor of Arts in Public Relations and Publicity

Program Duration: 4 years (8 semesters)
Degree: Bachelor of Arts
Total ECTS for Graduation: 240

Main website: https://iletisim.neu.edu.tr/?lang=en
Curriculum link: https://iletisim.neu.edu.tr/academic/academic-programmes/department-of-public-relations-and-advertising/courses/?lang=en

Legend:
C = Compulsory Course
E = Elective Course
K = Credit (Credits)""",

        # 1st Year - 1st Semester
        """First Year - First Semester (Fall) - Compulsory Courses:
CMN101, Introduction to Communication, C, K:3
YIT101, Turkish for Foreigners I, C, K:2
ENG101, English I, C, K:3
AİT103, Principle of Atatürk I, C, K:2
ECON111, Principle of Economy, C, K:3
CMN111, History of Culture, C, K:3
Elective Course, E, K:3

Total Compulsory: K:16
Total Elective: K:3
Total Semester Credits: 19""",

        # 1st Year - 2nd Semester
        """First Year - Second Semester (Spring) - Compulsory Courses:
CMN108, History of Communication, C, K:3
SOC122, Sociology, C, K:3
YIT102, Turkish for Foreigners II, C, K:2
CMN199, English II, C, K:3
AİT104, Principle of Atatürk II, C, K:2
PRL201, Introduction to Public Relations & Advertising, C, K:3
Elective Course, E, K:3

Total Compulsory: K:16
Total Elective: K:3
Total Semester Credits: 19""",

        # 2nd Year - 3rd Semester
        """Second Year - Third Semester (Fall) - Compulsory Courses:
CMN208, Political Science, C, K:3
CMN217, Communication Theories, C, K:3
CMN201, Social Psychology, C, K:3
CMN203, Communication Workshop, C, K:3
Elective Course, E, K:3
Elective Course, E, K:3

Total Compulsory: K:12
Total Elective: K:6
Total Semester Credits: 18""",

        # 2nd Year - 4th Semester
        """Second Year - Fourth Semester (Spring) - Compulsory Courses:
CMN202, Sociology for Communication, C, K:3
CMN306, Interpersonal Communication, C, K:3
PRL202, Introduction to Business, C, K:3
PRL313, Graphic Design, C, K:3
Elective Course, E, K:3
Elective Course, E, K:3

Total Compulsory: K:12
Total Elective: K:6
Total Semester Credits: 18""",

        # 3rd Year - 5th Semester
        """Third Year - Fifth Semester (Fall) - Compulsory Courses:
CMN303, Research Methods & Techniques in Social Science, C, K:3
CMN310, Law of Communication, C, K:3
PRL309, Design of Advertisement, C, K:3
MARK301, Principles of Marketing, C, K:3
Elective Course, E, K:3
Elective Course, E, K:3

Total Compulsory: K:12
Total Elective: K:6
Total Semester Credits: 18""",

        # 3rd Year - 6th Semester
        """Third Year - Sixth Semester (Spring) - Compulsory Courses:
CMN311, Public Opinion Research, C, K:3
PRL302, Marketing Research, C, K:3
PRL332, Application of Advertising, C, K:3
Elective Course, E, K:3
Elective Course, E, K:3
Elective Course, E, K:3

Total Compulsory: K:9
Total Elective: K:9
Total Semester Credits: 18""",

        # 4th Year - 7th Semester
        """Fourth Year - Seventh Semester (Fall) - Compulsory Courses:
CMN413, Media Ethics, C, K:3
CMN431, Political Communication, C, K:3
PRL403, Advertising & Public Relations Agency Management, C, K:3
PRL433, Planning & Practices in Public Relations, C, K:3
Elective Course, E, K:3
Elective Course, E, K:3

Total Compulsory: K:12
Total Elective: K:6
Total Semester Credits: 18""",

        # 4th Year - 8th Semester
        """Fourth Year - Eighth Semester (Spring) - Compulsory Courses:
CMN444, Communication and Modernity, C, K:3
PRL414, Publicity & Promotion Strategies, C, K:3
PRL440, Department Project, C, K:3
Elective Course, E, K:3
Elective Course, E, K:3
Elective Course, E, K:3

Total Compulsory: K:9
Total Elective: K:9
Total Semester Credits: 18""",

        # Compulsory Course Descriptions
        """Compulsory Course Descriptions:

CMN101 - Introduction to Communication:
The aim of the course is to help students understand fundamental concepts in communication such as the process of signification and representation. Students will acquire knowledge about historical development of different media sectors.

CMN201 - Social Psychology:
Covers introduction to social psychology including social beliefs, judgments, behavior, attitudes, conformity, obedience, persuasion, group influence, prejudice, aggression and helping.

CMN202 - Sociology for Communication:
Presents fundamental concepts and issues in sociology and connects them to communication studies.

CMN203 - Communication Workshop:
Practical course focusing on public relations, preparation of press releases, and creating public opinion through applied studies.

CMN208 - Political Science:
Develops students' understanding of political science and different ideologies through active learning and presentations.

CMN217 - Communication Theories:
Helps students understand the intricacies of the communication field for their professional development.

CMN303 - Research Methods in Social Sciences:
Provides tools for critically engaged, theoretically informed research using interviewing, focus groups, historical research, ethnography, and textual analysis.

CMN306 - Interpersonal Communication:
Teaches students to communicate effectively in conflict situations.

CMN310 - Law of Communication:
Presents fundamental concepts in communication law and how legal systems function.

CMN311 - Public Opinion Research:
Survey research specialization providing public attitude surveys, focus groups, demographic studies and market research.

CMN413 - Media Ethics:
Establishes importance of ethics philosophy in communication and media studies, covering media structures and new technologies.

CMN431 - Political Communication:
Introduction to theory and practice of political communication, media's role in campaigns, and government relations.

CMN444 - Communication and Modernity:
Introduction to formation of modernity and postmodernity, covering Enlightenment, modern state, media, and globalization.

PRL201 - Introduction to Public Relations & Advertising:
Foundation course covering basic principles and practices in public relations and advertising.

PRL202 - Introduction to Business:
Examines origins of business science, basic concepts, management functions and relations with other disciplines.

PRL309 - Design of Advertisement:
Teaches advertising design in visual, auditory and social networks, focusing on linguistics, syntax and slogans.

PRL313 - Graphic Design:
Introduction to graphic design computer programmes including Adobe Photoshop and Adobe Illustrator.

PRL332 - Application of Advertising:
Overview of strategic planning and management process for developing and executing communication campaigns.

PRL403 - Advertising & Public Relations Agency Management:
Examines activities in advertising and PR agencies, organizational relationships and business understanding.

PRL414 - Publicity & Promotion Strategies:
Covers publicity, promotion concepts, marketing communication and integrated marketing communication (IMC) process.

PRL433 - Planning & Practices in Public Relations:
Introduces strategic planning process for organizational public relations efforts.

PRL440 - Department Project:
Students apply a real PR project to prepare for professional life.""",

        # Elective Course Descriptions
        """Elective Course Descriptions:

CMN106 - New Media Technologies:
Introduction to digitalization of media, emergence of new technologies, and their impact on marketing, advertising, and communication professions.

CMN120 - Creative Ideas:
Explores creativity as key tool for successful business and personal life, developing creative thinking skills.

CMN330 - Presentation Techniques:
Practical course developing presentation skills through multiple in-class presentations for clear and confident self-expression.

CMN341 - Research of Mass Media:
Study of how people relay information through mass media to large populations, focusing on newspapers, TV, radio, and internet.

CMN405 - Cultural Studies:
Interdisciplinary field examining theoretical positions on culture and media including mass culture, ideology, popular culture, and social resistance.

CMN455 - Globalisation and International Institutions:
Surveys theoretical, legal and political issues confronting intergovernmental organizations like UN and EU.

FLM110 - Sound Editing I:
Sound recording for film-making including sound effects, dialogue, foley, and location sound.

FLM231 - Basic Concept of Sound and Image:
Introduction to basic concepts and techniques for capturing quality sound and image.

FLM314 - History of Radio and Television:
Historical perspective on radio and television development in American culture and internationally.

FLM315 - Semiotics:
Introduction to principles of semiotics, semiotic analysis and representation in cinema.

FLM318 - Film Genres:
Examination of film genres, their features, similarities, differences, and cultural significance.

JRN201 - Introduction to Journalism:
Study of principles and practices of journalism and its role in democratic society.

JRN206 - Interviewing Techniques:
Teaches preparation, conduct, and writing of interviews for journalism.

JRN212 - New Information Techniques:
Examination of new information technologies and their reflections in journalism worldwide.

JRN401 - Investigative Journalism:
Develops skills in identifying investigative stories and reporting news accurately and professionally.

JRN408 - Current Problems of Local Press:
Investigation of current problems faced by media in daily operations.

PRA200 - Sustainable Development:
Examination of Sustainable Development goals and principles with examples from different countries.

PRA333 - New Media and Digital Applications:
Covers information society concept, new media technologies, and digital communication applications.

PRA422 - Corporate Communication:
Study of corporate communication concepts, features, coverage and related case studies.""",

        # Program Summary and Career Opportunities
        """Public Relations and Publicity Program Summary:
Degree: Bachelor of Arts in Public Relations and Publicity
Duration: 4 years (8 semesters)
Total Credits: Approximately 150
Language of Instruction: English

Program Focus Areas:
- Public Relations Strategy and Planning
- Advertising Design and Application
- Corporate Communication
- Media Relations
- Marketing and Brand Management
- Digital and Social Media
- Crisis Communication
- Public Opinion Research

Core Competencies Developed:
- Strategic communication planning
- Media relations and press management
- Advertising design and campaign development
- Corporate communication strategies
- Public opinion research and analysis
- Digital media applications
- Presentation and interpersonal skills
- Ethical communication practices

Career Opportunities:
Public Relations Specialist
Advertising Account Executive
Corporate Communications Manager
Media Relations Officer
Social Media Manager
Brand Manager
Marketing Communications Specialist
Crisis Communication Manager
Public Affairs Specialist
Event Coordinator
Content Strategist
Digital Marketing Specialist
Public Opinion Researcher
Communication Consultant

Industry Sectors:
Public Relations Agencies
Advertising Firms
Corporate Communications Departments
Government and Public Affairs
Non-Profit Organizations
Media Houses
Digital Marketing Agencies
Event Management Companies
Market Research Firms""",

        # Course Progression and Specializations
        """Course Progression and Specialization Tracks:

Foundation Year (1st Year):
- Basic communication principles and theories
- Cultural and historical context
- Language and general education courses
- Introduction to public relations

Core Development (2nd Year):
- Communication theories and research
- Social psychology and sociology
- Business fundamentals
- Graphic design and workshop skills

Specialization (3rd Year):
- Advanced research methods
- Marketing and advertising principles
- Public opinion research
- Legal and ethical aspects

Professional Preparation (4th Year):
- Agency management
- Strategic planning and practices
- Political communication
- Department project and professional ethics

Specialization Tracks:
1. Corporate Public Relations: Agency management, corporate communication, strategic planning
2. Advertising and Marketing: Advertisement design, marketing research, promotion strategies
3. Media Relations: Political communication, public opinion, media ethics
4. Digital Communication: New media technologies, digital applications, social media"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Communication",
            "department": "Public Relations and Publicity",
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
            "course_type": "compulsory",
            "document_type": "course_description",
            "content_type": "compulsory_courses"
        },
        {
            "course_type": "elective",
            "document_type": "course_description",
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
    ids = [f"pr_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Public Relations and Publicity curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["public relations advertising campaigns"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_public_relations_curriculum_to_chromadb()