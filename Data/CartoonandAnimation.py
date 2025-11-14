import chromadb
from chromadb.utils import embedding_functions

def add_cartoon_animation_curriculum_to_chromadb():
    """Add Cartoon and Animation curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_cartoon_animation",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_cartoon_animation",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_cartoon_animation")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF COMMUNICATION
DEPARTMENT OF CARTOON AND ANIMATION
Bachelor of Arts in Cartoon and Animation

Program Duration: 4 years (8 semesters)
Total Credits: Not specified (course-based system)

Main website: https://iletisim.neu.edu.tr/?lang=en
Curriculum link: https://iletisim.neu.edu.tr/academic/academic-programmes/department-of-cartoon-and-animation/courses/?lang=en

Program Focus:
- 2D and 3D Animation Techniques
- Cartoon Production and Story Design
- Digital Art and Illustration
- Visual Effects and Sound Design
- Character Design and Pattern Development""",

        # 1st Year - Fall Semester
        """First Year - Fall Semester - Compulsory Courses:
ILF101, Introduction to Communication, Credit:3
KHM102, Introduction to Law, Credit:3
CFA101, Moving Image History, Credit:3
GIT102, Basic Art Education, Credit:3
TUR101, Turkish Language I, Credit:2
ING101, English I, Credit:3
AIT101, Principle of Atatürk I, Credit:2

Total Semester Credits: 19""",

        # 1st Year - Spring Semester
        """First Year - Spring Semester - Compulsory Courses:
ILF108, History of Communication, Credit:3
CFA102, Cartoon and Animation Techniques, Credit:3
GIT101, Basic Design, Credit:3
GIT108, Principle of Art, Credit:3
TUR102, Turkish Language II, Credit:2
ING102, English II, Credit:3
AIT102, Principle of Atatürk II, Credit:2

Total Semester Credits: 19""",

        # 2nd Year - Fall Semester
        """Second Year - Fall Semester - Compulsory Courses:
ILF217, Communication Theories, Credit:3
GIT222, Illustration I, Credit:3
GIT221, Introduction to Art, Credit:3
CFA201, Cartoon Applications, Credit:3
CFA203, Pattern I, Credit:3
CFA205, Story Design, Credit:3

Total Semester Credits: 18""",

        # 2nd Year - Spring Semester
        """Second Year - Spring Semester - Compulsory Courses:
ILF202, Communication Sociology, Credit:3
GIT203, History of Art, Credit:3
CFA202, Computer Based Animation Application, Credit:3
CFA204, Pattern II, Credit:3
CFA206, Illustrated Draft Drawing, Credit:3
RTS341, Screen Writing, Credit:3

Total Semester Credits: 18""",

        # 3rd Year - Fall Semester
        """Third Year - Fall Semester - Compulsory Courses:
CFA301, Stage Design in Cartoons, Credit:3
RTS241, Editing I, Credit:3
CFA303, 2D Animation I, Credit:3
CFA305, 3D Computer Animation I, Credit:3
CFA307, Photography and Single Animation, Credit:3
CFA309, Sound Techniques I, Credit:3

Total Semester Credits: 18""",

        # 3rd Year - Spring Semester
        """Third Year - Spring Semester - Compulsory Courses:
CFA302, Mythology, Credit:3
RTS245, Editing II, Credit:3
CFA304, 2D Animation II, Credit:3
CFA306, 3D Computer Animation II, Credit:3
CFA308, Sound Techniques II, Credit:3
RTS403, Visual Expression, Credit:3

Total Semester Credits: 18""",

        # 4th Year - Fall Semester
        """Fourth Year - Fall Semester - Compulsory Courses:
CFA401, Cartoon Production I, Credit:3
CFA403, Visual Effect, Credit:3
CFA405, 3D Animation Production in Computer I, Credit:3
Elective, Elective Course, Credit:3
Elective, Elective Course, Credit:3
Elective, Elective Course, Credit:3

Total Semester Credits: 18""",

        # 4th Year - Spring Semester
        """Fourth Year - Spring Semester - Compulsory Courses:
CFA402, Cartoon Production II, Credit:3
CFA404, 3D Animation Production in Computer II, Credit:3
CFA406, Departmental Project, Credit:3
Elective, Elective Course, Credit:3
Elective, Elective Course, Credit:3
Elective, Elective Course, Credit:3

Total Semester Credits: 18

Total Program Credits: Approximately 146""",

        # Course Descriptions - Core Animation Courses
        """Core Animation and Cartoon Courses Description:

CFA101, Moving Image History: Historical development of moving images and animation techniques.
CFA102, Cartoon and Animation Techniques: Fundamental techniques in cartoon creation and animation.
CFA201, Cartoon Applications: Practical applications of cartoon creation methods.
CFA203, Pattern I: Character and object pattern design fundamentals.
CFA204, Pattern II: Advanced pattern design and development.
CFA205, Story Design: Narrative structure and storytelling for animation.
CFA202, Computer Based Animation Application: Digital tools for animation creation.
CFA206, Illustrated Draft Drawing: Drawing techniques for animation storyboards.

CFA301, Stage Design in Cartoons: Creating environments and settings for animated works.
CFA303, 2D Animation I: Traditional and digital 2D animation techniques.
CFA304, 2D Animation II: Advanced 2D animation and character movement.
CFA305, 3D Computer Animation I: Introduction to 3D modeling and animation.
CFA306, 3D Computer Animation II: Advanced 3D animation techniques.
CFA307, Photography and Single Animation: Stop-motion and single-frame animation.
CFA309, Sound Techniques I: Audio production for animation.
CFA308, Sound Techniques II: Advanced sound design and mixing.

CFA401, Cartoon Production I: Comprehensive cartoon production project.
CFA402, Cartoon Production II: Advanced production and portfolio development.
CFA403, Visual Effect: Special effects creation for animation.
CFA405, 3D Animation Production in Computer I: 3D animation project development.
CFA404, 3D Animation Production in Computer II: Advanced 3D production techniques.
CFA406, Departmental Project: Final comprehensive animation project.""",

        # Supporting Courses Description
        """Supporting and Foundation Courses:

Communication Courses:
ILF101, Introduction to Communication: Basic communication theories and practices.
ILF108, History of Communication: Historical development of communication media.
ILF217, Communication Theories: Theoretical frameworks in communication studies.
ILF202, Communication Sociology: Sociological aspects of communication.

Art and Design Courses:
GIT102, Basic Art Education: Fundamental art principles and techniques.
GIT101, Basic Design: Design fundamentals and composition.
GIT108, Principle of Art: Artistic principles and aesthetics.
GIT222, Illustration I: Illustration techniques and styles.
GIT221, Introduction to Art: Overview of art history and movements.
GIT203, History of Art: Comprehensive art history survey.

Film and Media Courses:
RTS341, Screen Writing: Scriptwriting for visual media.
RTS241, Editing I: Video and film editing techniques.
RTS245, Editing II: Advanced editing and post-production.
RTS403, Visual Expression: Visual storytelling and expression.

General Education:
KHM102, Introduction to Law: Basic legal concepts and frameworks.
CFA302, Mythology: Mythological stories and their use in animation.""",

        # Program Summary and Career Opportunities
        """Cartoon and Animation Program Summary:
Degree: Bachelor of Arts in Cartoon and Animation
Duration: 4 years (8 semesters)
Faculty: Faculty of Communication

Program Focus Areas:
- 2D Animation Techniques
- 3D Computer Animation
- Character Design and Development
- Storyboarding and Narrative Design
- Digital Illustration and Art
- Visual Effects and Post-Production
- Sound Design for Animation
- Cartoon Production and Direction

Technical Skills Developed:
- Digital Animation Software Proficiency
- Character Design and Pattern Development
- Storyboarding and Visual Storytelling
- 3D Modeling and Animation
- Sound Design and Audio Production
- Visual Effects Creation
- Editing and Post-Production

Career Opportunities:
2D/3D Animator
Character Designer
Storyboard Artist
Animation Director
Visual Effects Artist
Cartoonist
Motion Graphics Designer
Game Animator
Advertising Animator
Film and TV Animation Specialist
Academic and Research Positions

Industry Applications:
- Film and Television Animation
- Video Game Development
- Advertising and Marketing
- Educational Media
- Web and Mobile Applications
- Publishing and Illustration
- Architectural Visualization
- Medical and Scientific Animation"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Communication",
            "department": "Cartoon and Animation",
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
            "content_type": "animation_courses"
        },
        {
            "course_type": "supporting",
            "document_type": "course_description",
            "content_type": "supporting_courses"
        },
        {
            "document_type": "program_info",
            "content_type": "program_summary_careers"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"cartoon_animation_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Cartoon and Animation curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["animation 3D cartoon production"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_cartoon_animation_curriculum_to_chromadb()