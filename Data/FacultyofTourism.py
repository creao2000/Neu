import chromadb
from chromadb.utils import embedding_functions

def add_tourism_curriculum_to_chromadb():
    """Add Tourism Faculty curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_tourism_faculty",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_tourism_faculty",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_tourism_faculty")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """Faculty of Tourism Bachelor Curriculum Overview
Main website link: https://turizm.neu.edu.tr/?lang=en
Course scheduling link: https://turizm.neu.edu.tr/course-registration/time-table/?lang=en
Curriculum link: https://neu.edu.tr/wp-content/uploads/2020/09/03/tourism-and-hotel-management-03.09.2020.pdf

Degree: Bachelor of Tourism and Hotel Management
Program Duration: 4 years (8 semesters)
Language of Instruction: English""",

        # 1st Semester
        """First Year - First Semester Courses:
THM111, Introduction to Tourism, Credit: 3, ECTS: 6
THM115, Introduction to Business, Credit: 3, ECTS: 6
THM131, Math for Hospitality Industry, Credit: 3, ECTS: 5
THM161, Introduction to Computer, Credit: 3, ECTS: 4
ENG101, English I, Credit: 3, ECTS: 6
LANG101, Elective Language I, Credit: 3, ECTS: 3
AIT101, History of Turkish Reforms, Credit: 0, ECTS: 2

Total: Credits: 18, ECTS: 30""",

        # 2nd Semester
        """First Year - Second Semester Courses:
THM123, Lodging Operations, Credit: 3, ECTS: 6
THM126, Introduction to Economics, Credit: 3, ECTS: 4
THM142, Nutrition & Sanitation, Credit: 3, ECTS: 5
THM146, Front Office Management, Credit: 3, ECTS: 4
ENG102, English II, Credit: 3, ECTS: 6
LANG102, Elective Language II, Credit: 3, ECTS: 3

Total: Credits: 18, ECTS: 30

Summer Training:
THM100, Summer Training I, Credit: 0, ECTS: 12""",

        # 3rd Semester
        """Second Year - First Semester Courses:
THM221, Travel & Tour Operations, Credit: 3, ECTS: 6
THM241, Food Production, Credit: 3, ECTS: 5
THM244, Housekeeping Management, Credit: 3, ECTS: 5
THM261, Fidelio, Credit: 3, ECTS: 5
ENG201, English III, Credit: 3, ECTS: 6
LANG201, Elective Language III, Credit: 3, ECTS: 3

Total: Credits: 18, ECTS: 30""",

        # 4th Semester
        """Second Year - Second Semester Courses:
THM243, Introduction to Marketing, Credit: 3, ECTS: 5
THM246, Amadeus, Credit: 3, ECTS: 6
THM253, Financial Accounting, Credit: 3, ECTS: 4
THM264, Food & Beverage Management, Credit: 3, ECTS: 6
ENG202, English IV, Credit: 3, ECTS: 6
LANG202, Elective Language IV, Credit: 3, ECTS: 3

Total: Credits: 18, ECTS: 30""",

        # 5th Semester
        """Third Year - First Semester Courses:
THM310, Organizational Behavior, Credit: 3, ECTS: 6
THM315, Tourism Economy, Credit: 3, ECTS: 6
THM317, Tourism & Environment, Credit: 3, ECTS: 6
THM318, Cost Control, Credit: 3, ECTS: 6
THM319, Special Interest Tourism, Credit: 3, ECTS: 6

Total: Credits: 15, ECTS: 30""",

        # 6th Semester
        """Third Year - Second Semester Courses:
THM321, Human Resources Management, Credit: 3, ECTS: 6
THM328, Hospitality Marketing, Credit: 3, ECTS: 6
THM340, Event & Conference Management, Credit: 3, ECTS: 6
THM346, Research Methods, Credit: 3, ECTS: 6
THM351, Interbusiness, Credit: 3, ECTS: 6

Total: Credits: 15, ECTS: 30

Summer Training:
THM200, Summer Training II, Credit: 0, ECTS: 12""",

        # 7th Semester
        """Fourth Year - First Semester Courses:
THM411, Tourism Policy & Planning, Credit: 3, ECTS: 6
THM417, Fundamentals of Finance, Credit: 3, ECTS: 6
THM420, Consumer Behavior in Tourism, Credit: 3, ECTS: 6
THM422, Sociology of Tourism, Credit: 3, ECTS: 6
THM426, Strategic Management, Credit: 3, ECTS: 6

Total: Credits: 15, ECTS: 30""",

        # 8th Semester
        """Fourth Year - Second Semester Courses:
Technical Elective I, Credit: 3, ECTS: 6
Technical Elective II, Credit: 3, ECTS: 6
Technical Elective III, Credit: 3, ECTS: 6
Technical Elective IV, Credit: 3, ECTS: 6
Technical Elective V, Credit: 3, ECTS: 6

Total: Credits: 15, ECTS: 30""",

        # Technical Elective Courses
        """Technical Elective Courses (Sample Options):
Tourism Management Electives:
- Hotel Management and Operations
- Resort Management
- Tourism Destination Management
- Sustainable Tourism Development
- Cultural Heritage Tourism
- Tourism Law and Regulations

Hospitality Management Electives:
- Restaurant Management
- Beverage Management
- Convention Management
- Hospitality Information Systems
- Revenue Management
- Quality Management in Hospitality

Tourism Marketing Electives:
- Digital Marketing in Tourism
- Tourism Product Development
- Brand Management in Tourism
- Tourism Sales and Promotion
- Customer Relationship Management

Specialized Tourism Electives:
- Ecotourism and Adventure Tourism
- Medical and Health Tourism
- MICE Tourism (Meetings, Incentives, Conferences, Exhibitions)
- Gastronomy and Culinary Tourism
- Wine Tourism
- Sports Tourism""",

        # Language Electives
        """Language Elective Courses:
LANG101/102/201/202 - Available Language Options:
- German I, II, III, IV
- French I, II, III, IV
- Russian I, II, III, IV
- Spanish I, II, III, IV
- Arabic I, II, III, IV
- Greek I, II, III, IV
- Italian I, II, III, IV
- Chinese I, II, III, IV
- Japanese I, II, III, IV""",

        # Program Summary
        """Tourism and Hotel Management Program Summary:
Total Program Duration: 4 years (8 semesters)
Total Credits: 132
Total ECTS: 264
Degree: Bachelor of Tourism and Hotel Management
Language of Instruction: English

Program Structure:
- 8 academic semesters
- 2 summer training periods (THM100, THM200)
- 4 years of language education (English + elective language)
- 5 technical elective courses in final semester

Key Focus Areas:
- Tourism Management and Operations
- Hospitality and Hotel Management
- Food and Beverage Management
- Tourism Marketing and Economics
- Tourism Planning and Development
- Human Resources and Organizational Behavior
- Financial Management in Tourism

Special Features:
- Practical training with industry software (Fidelio, Amadeus)
- Two mandatory summer training periods
- Continuous language education throughout the program
- Technical specialization in final semester
- Industry-oriented curriculum""",

        # Career Opportunities
        """Career Opportunities for Tourism Graduates:
Hotel and Resort Management:
- Hotel Manager
- Resort Manager
- Front Office Manager
- Housekeeping Manager
- Food and Beverage Manager

Tourism Operations:
- Tour Operator
- Travel Agency Manager
- Destination Manager
- Event and Conference Manager
- MICE Coordinator

Hospitality Services:
- Restaurant Manager
- Catering Manager
- Cruise Ship Hotel Manager
- Airline Cabin Services Manager
- Hospitality Consultant

Tourism Development and Marketing:
- Tourism Marketing Manager
- Tourism Development Officer
- Tourism Policy Planner
- Sustainable Tourism Coordinator
- Cultural Tourism Manager

Other Opportunities:
- Tourism Researcher
- Academic Career
- Tourism Entrepreneur
- Tourism Project Manager
- Customer Experience Manager""",

        # Internship Information
        """Summer Training Program:
THM100 - Summer Training I (After 2nd Semester)
- Duration: Minimum 30 working days
- Credit: 0, ECTS: 12
- Focus: Basic operations in tourism/hospitality establishments

THM200 - Summer Training II (After 6th Semester)
- Duration: Minimum 30 working days
- Credit: 0, ECTS: 12
- Focus: Management-level training in specialized areas

Training Objectives:
- Gain practical industry experience
- Apply theoretical knowledge in real-world settings
- Develop professional skills and competencies
- Build industry connections and networks
- Enhance employability after graduation

Approved Training Venues:
- Hotels and Resorts
- Travel Agencies and Tour Operators
- Restaurants and Catering Services
- Conference and Event Centers
- Tourism Development Organizations
- Airlines and Transportation Services"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Tourism",
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
            "content_type": "technical_electives"
        },
        {
            "course_type": "language",
            "document_type": "course_list",
            "content_type": "language_electives"
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
            "content_type": "internship_info"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"tourism_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Tourism Faculty curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["tourism hotel management courses"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_tourism_curriculum_to_chromadb()