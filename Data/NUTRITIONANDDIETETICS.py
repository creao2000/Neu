
import chromadb
from chromadb.utils import embedding_functions

def add_nutrition_dietetics_curriculum_to_chromadb():
    """Add Nutrition and Dietetics curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_nutrition_dietetics",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_nutrition_dietetics",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_nutrition_dietetics")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """FACULTY OF HEALTH SCIENCES
DEPARTMENT OF NUTRITION AND DIETETICS
Bachelor of Science in Nutrition and Dietetics
Main website link: https://saglikbilimleri.neu.edu.tr/?lang=en
Curriculum link: https://saglikbilimleri.neu.edu.tr/wp-content/uploads/sites/144/2020/10/13/nutrition-and-dietetics-13.10.2020.pdf


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
AİT101, Atatürk's Principles and the History of the Turkish Revolution, C, T:2, P:0, C:2, ECTS:2
NAD105, Professional Orientation I, C, T:1, P:0, C:1, ECTS:1
NAD113, Principles of Nutrition I, C, T:2, P:3, C:3, ECTS:6
CHM101, Chemistry I, C, T:3, P:2, C:4, ECTS:5
MTH117, Basic Mathematics, C, T:3, P:0, C:3, ECTS:3
ECO115, General Economics, C, T:3, P:0, C:3, ECTS:3
ENG101, English I, C, T:3, P:0, C:3, ECTS:3
YİT101, Turkish for Foreign Students I, C, T:2, P:0, C:2, ECTS:2

Total Compulsory: T:19, P:5, C:21, ECTS:25

Elective Courses (Select to reach 30 ECTS):
NAD103, Nutrition Basics I, E, T:1, P:0, C:1, ECTS:3
NAD107, Nutritional Anthropology, E, T:1, P:0, C:1, ECTS:3
AID103, First Aid, E, T:2, P:0, C:2, ECTS:3
NAD115, Food Diversity, E, T:2, P:0, C:2, ECTS:2
FHS155, Self Knowledge and Communication Skills, E, T:2, P:0, C:2, ECTS:3

Total Semester ECTS: 30""",

        # 1st Year - 2nd Semester
        """First Year - Second Semester (Spring) - Compulsory Courses:
AİT102, Atatürk's Principles and the History of the Turkish Revolution, C, T:2, P:0, C:2, ECTS:2
NAD106, Professional Orientation II, C, T:1, P:0, C:1, ECTS:1
NAD114, Principles of Nutrition II, C, T:2, P:3, C:3, ECTS:6
CHM102, Chemistry II, C, T:3, P:2, C:4, ECTS:5
MLB102, Medical Biology and Genetics, C, T:3, P:0, C:3, ECTS:3
PSY102, Psychology, C, T:2, P:0, C:2, ECTS:2
NAD108, Demographical Structure and Health, C, T:2, P:0, C:2, ECTS:2
ENG102, English II, C, T:3, P:0, C:3, ECTS:3
YİT102, Turkish for Foreign Students II, C, T:2, P:0, C:2, ECTS:2

Total Compulsory: T:20, P:5, C:22, ECTS:26

Elective Courses (Select to reach 30 ECTS):
COM102, Computer, E, T:3, P:0, C:3, ECTS:4
NAD104, Nutrition Basics II, E, T:1, P:0, C:1, ECTS:3
NAD118, Cypriot Cuisine, E, T:1, P:0, C:1, ECTS:3
NAD120, Food Choice in Optimal Nutrition, E, T:2, P:0, C:2, ECTS:2
FHS156, Interpersonal Relationships and Communication, E, T:2, P:0, C:2, ECTS:3
FHS158, Developmental Psychology, E, T:2, P:0, C:2, ECTS:3
NAD122, Nutrients and Health, E, T:2, P:0, C:2, ECTS:4
NAD124, Aging and Nutrition, E, T:2, P:0, C:2, ECTS:4
FHS104, Occupational Health and Safety, E, T:2, P:0, C:2, ECTS:4

Total Semester ECTS: 30""",

        # 2nd Year - 3rd Semester
        """Second Year - Third Semester (Fall) - Compulsory Courses:
NAD221, Nutritional Biochemistry I, C, T:3, P:0, C:3, ECTS:4
NAD231, Food Chemistry and Analyses I, C, T:2, P:3, C:3, ECTS:5
ANT201, Anatomy I, C, T:2, P:0, C:2, ECTS:2
PHS203, Physiology I, C, T:2, P:0, C:2, ECTS:2
MIC203, Basic Microbiology, C, T:2, P:2, C:3, ECTS:5
ENG201, English III, C, T:3, P:0, C:3, ECTS:3

Total Compulsory: T:14, P:5, C:16, ECTS:21

Elective Courses (Select to reach 30 ECTS):
YİT201, Turkish for Foreign Students III, E, T:3, P:0, C:3, ECTS:3
BES241, Occupational English I, E, T:2, P:0, C:2, ECTS:2
NAD201, Healthy Food Choices I, E, T:2, P:0, C:2, ECTS:3
NAD203, Development of Health, E, T:2, P:0, C:2, ECTS:4
NAD207, Nutrition and Healthy Life, E, T:2, P:0, C:2, ECTS:3
NAD211, Food Industry, E, T:2, P:0, C:2, ECTS:3

Total Semester ECTS: 30""",

        # 2nd Year - 4th Semester
        """Second Year - Fourth Semester (Spring) - Compulsory Courses:
NAD222, Nutritional Biochemistry II, C, T:3, P:0, C:3, ECTS:4
NAD232, Food Chemistry and Analyses II, C, T:2, P:3, C:3, ECTS:5
ANT202, Anatomy II, C, T:2, P:0, C:2, ECTS:2
PHS204, Physiology II, C, T:2, P:0, C:2, ECTS:2
MIC222, Food Microbiology, C, T:2, P:2, C:3, ECTS:5
IMN202, Information Management in Nutrition Science, C, T:2, P:0, C:2, ECTS:2
ENG202, English IV, C, T:3, P:0, C:3, ECTS:3

Total Compulsory: T:16, P:5, C:18, ECTS:23

Elective Courses (Select to reach 30 ECTS):
YİT202, Turkish for Foreign Students IV, E, T:3, P:0, C:3, ECTS:3
BES242, Occupational English II, E, T:2, P:0, C:2, ECTS:2
NAD202, Healthy Food Choices II, E, T:2, P:0, C:2, ECTS:3
NAD216, Exercise and Nutrition, E, T:2, P:0, C:2, ECTS:3
NAD224, Methods of Food Control, E, T:1, P:2, C:2, ECTS:3
NAD228, Basic Approaches in Evaluation of Dietary Assessment, E, T:2, P:0, C:2, ECTS:4
NAD230, Current Scientific Topics in Nutritional Sciences, E, T:1, P:0, C:1, ECTS:2

Total Semester ECTS: 30""",

        # 3rd Year - 5th Semester
        """Third Year - Fifth Semester (Fall) - Compulsory Courses:
NAD315, Mother and Child Nutrition, C, T:2, P:3, C:3, ECTS:5
NAD321, Nutritional Assessment of Community, C, T:3, P:0, C:3, ECTS:3
NAD343, Food Service Systems I, C, T:3, P:0, C:3, ECTS:3
NAD351, Medical Nutrition Therapy in Diseases I, C, T:2, P:3, C:3, ECTS:5
PTH311, Physiopathology of Chronic Diseases I, C, T:2, P:0, C:2, ECTS:2
NAD349, Nutrition Education, C, T:2, P:0, C:2, ECTS:2
BST301, Biostatistics, C, T:3, P:0, C:3, ECTS:5

Total Compulsory: T:17, P:6, C:19, ECTS:25

Elective Courses (Select to reach 30 ECTS):
NAD301, Functional Foods and Health, E, T:1, P:0, C:1, ECTS:3
NAD305, Cancer and Nutrition, E, T:1, P:0, C:1, ECTS:3
NAD307, Food Technology, E, T:3, P:0, C:3, ECTS:3
NAD317, Sports Nutrition and Health, E, T:2, P:0, C:2, ECTS:2
NAD371, General Management, E, T:3, P:0, C:3, ECTS:5
FHS335, Research Methods in Health Sciences, E, T:2, P:0, C:2, ECTS:3

Total Semester ECTS: 30""",

        # 3rd Year - 6th Semester
        """Third Year - Sixth Semester (Spring) - Compulsory Courses:
NAD316, Pediatric Nutrition in Acute and Chronic Diseases, C, T:2, P:3, C:3, ECTS:5
NAD322, Community Nutrition and Epidemiology, C, T:3, P:0, C:3, ECTS:3
NAD334, Food Control and Legislation, C, T:2, P:0, C:2, ECTS:2
NAD344, Food Service Systems II, C, T:3, P:0, C:3, ECTS:3
NAD352, Medical Nutrition Therapy in Diseases II, C, T:2, P:3, C:3, ECTS:5
PTH312, Physiopathology of Chronic Diseases II, C, T:2, P:0, C:2, ECTS:2
HIN302, Health Informatics, C, T:3, P:0, C:3, ECTS:5

Total Compulsory: T:17, P:6, C:19, ECTS:25

Elective Courses (Select to reach 30 ECTS):
NAD318, Nutrigenetics, Nutrigenomics and Personalized Nutrition, E, T:3, P:0, C:3, ECTS:5
NAD320, Physical Activity and Health, E, T:2, P:0, C:2, ECTS:3
NAD350, Nutritional Screening Tools, E, T:1, P:0, C:1, ECTS:2
PUH320, Community Health, E, T:2, P:0, C:2, ECTS:2
FHS356, Time Management, E, T:2, P:0, C:2, ECTS:3
NAD356, Scientific Publication Analysis, E, T:2, P:0, C:2, ECTS:3

Total Semester ECTS: 30""",

        # 4th Year - 7th Semester
        """Fourth Year - Seventh Semester (Fall) - Compulsory Courses:
NAD431, Graduate Thesis, C, T:0, P:3, C:2, ECTS:5
NAD448, Professional Practice in Children's Hospital, C, T:0, P:14, C:6, ECTS:7
NAD449, Professional Practice in Adult's Hospital, C, T:0, P:14, C:6, ECTS:7
NAD441, Professional Practice in Nutrition and Dietetics Field, C, T:0, P:35, C:9, ECTS:6
NAD445, Seminar, C, T:0, P:2, C:1, ECTS:3

Total Compulsory: T:0, P:68, C:24, ECTS:28

Elective Courses (Select to reach 30 ECTS):
FHS403, Branding Strategies and Personal Branding, E, T:2, P:0, C:2, ECTS:3
NAD405, Counselling in Nutrition and Dietetics, E, T:1, P:0, C:1, ECTS:2
NAD407, Eating Disorders, E, T:1, P:0, C:1, ECTS:2
NAD411, Current Applications in Pediatrics I, E, T:3, P:0, C:3, ECTS:5
NAD419, Enteral and Parenteral Nutrition I, E, T:3, P:0, C:3, ECTS:4
NAD413, Current Applications in Medical Nutrition Therapy I, E, T:3, P:0, C:3, ECTS:5
NAD415, Menu Planning in Diseases I, E, T:3, P:0, C:3, ECTS:5
NAD417, Mediterranean Diet and Health I, E, T:2, P:2, C:3, ECTS:5
NAD421, Nutrient-Drug Interaction, E, T:2, P:0, C:2, ECTS:4

Total Semester ECTS: 30""",

        # 4th Year - 8th Semester
        """Fourth Year - Eighth Semester (Spring) - Compulsory Courses:
NAD431, Graduate Thesis, C, T:0, P:3, C:2, ECTS:5
NAD450, Professional Practice in Institutional Food Services, C, T:0, P:14, C:6, ECTS:7
NAD451, Professional Practice in Hospital and Institutions, C, T:0, P:14, C:6, ECTS:7
NAD445, Seminar, C, T:0, P:2, C:1, ECTS:3

Total Compulsory: T:0, P:33, C:15, ECTS:22

Elective Courses (Select to reach 30 ECTS):
FHS403, Branding Strategies and Personal Branding, E, T:2, P:0, C:2, ECTS:3
NAD406, Ethics in Health Sciences, E, T:2, P:0, C:2, ECTS:4
NAD408, Enteral and Parenteral Nutrition II, E, T:2, P:2, C:3, ECTS:4
NAD412, Current Applications in Pediatrics II, E, T:3, P:0, C:3, ECTS:5
NAD414, Current Applications in Medical Nutrition Therapy I, E, T:3, P:0, C:3, ECTS:5
NAD416, Menu Planning in Diseases I, E, T:3, P:0, C:3, ECTS:5
NAD418, Mediterranean Diet and Health I, E, T:2, P:2, C:3, ECTS:4
NAD422, Eating Behaviour Disorders, E, T:1, P:0, C:1, ECTS:2
NAD424, Nutrient-Drug Interaction, E, T:2, P:0, C:2, ECTS:4

Total Semester ECTS: 30""",

        # Prerequisites and Important Notes
        """Important Prerequisites and Program Notes:

Course Prerequisites:
- NAD105 is prerequisite for NAD106
- NAD221 is prerequisite for NAD222
- NAD231 is prerequisite for NAD232
- ANT201 is prerequisite for ANT202
- PHS203 is prerequisite for PHS204
- ENG101 is prerequisite for ENG102
- ENG201 is prerequisite for ENG202
- NAD321 is prerequisite for NAD322
- NAD343 is prerequisite for NAD344
- PTH311 is prerequisite for PTH312

Program Requirements:
- All NAD coded courses should be taken before Professional Practice courses
- NAD431 and NAD445 courses can only be registered for one semester
- Total ECTS for graduation: 240
- Total compulsory ECTS: 187
- Total elective ECTS: 53

Professional Practice:
- Extensive practical training in final year
- Hospital placements (children's and adult's hospitals)
- Institutional food service placements
- Field practice in nutrition and dietetics""",

        # Program Summary and Career Opportunities
        """Nutrition and Dietetics Program Summary:
Degree: Bachelor of Science in Nutrition and Dietetics
Duration: 4 years (8 semesters)
Total ECTS: 240
Language of Instruction: English

Program Focus Areas:
- Clinical Nutrition and Dietetics
- Community Nutrition
- Food Science and Technology
- Medical Nutrition Therapy
- Food Service Management
- Public Health Nutrition
- Sports Nutrition
- Pediatric Nutrition

Career Opportunities:
Clinical Dietitian
Community Nutritionist
Food Service Manager
Sports Nutritionist
Pediatric Dietitian
Research Dietitian
Public Health Nutritionist
Nutrition Educator
Food Industry Specialist
Wellness Consultant
Academic and Research Positions

Professional Recognition:
Graduates are eligible to become registered dietitians and work in various healthcare settings, community programs, food industry, and research institutions."""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Health Sciences",
            "department": "Nutrition and Dietetics",
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
            "content_type": "prerequisites_notes"
        },
        {
            "document_type": "program_info",
            "content_type": "program_summary_careers"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"nutrition_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Nutrition and Dietetics curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["nutrition dietetics clinical courses"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_nutrition_dietetics_curriculum_to_chromadb()