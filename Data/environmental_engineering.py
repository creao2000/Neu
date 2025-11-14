import chromadb
from chromadb.utils import embedding_functions

def create_environmental_engineering_collection():
    """Create a separate collection for Environmental Engineering curriculum"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create a NEW collection for environmental engineering
    try:
        # First check if it exists and delete it to start fresh
        try:
            chroma_client.delete_collection("neu_environmental_engineering")
            print("Removed existing environmental engineering collection")
        except:
            print("No existing environmental engineering collection found")
        
        # Create new collection
        collection = chroma_client.create_collection(
            name="neu_environmental_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_environmental_engineering")
        
    except Exception as e:
        print(f"Error creating collection: {e}")
        return
    
    # Prepare environmental engineering curriculum documents
    documents = [
        # Faculty Information
        """Faculty: Faculty of Civil and Environmental Engineering
Department: Department of Environmental Engineering
Program: Environmental Engineering 4-Year Program (English)
Program Type: Annual
Language: English
Total Credits: 158
Total ECTS: 240
Description: Comprehensive environmental engineering program covering water treatment, air pollution control, waste management, and environmental modeling""",

        # Year 1 - Semester 1
        """Year 1 - Semester 1 Courses:
ENG101 English I (Compulsory, Theory:2 Practice:0 Credits:3 ECTS:3)
MTH101 Calculus I (Compulsory, T:3 P:2 C:4 E:5)
PHY101 General Physics I (Compulsory, T:3 P:2 C:4 E:5)
CHM101 General Chemistry I (Compulsory, T:3 P:2 C:4 E:5)
ECC101 Computer Programming (Compulsory, T:2 P:2 C:3 E:4)
CAM101 Campus Orientation (Compulsory, T:0 P:0 C:0 E:0)
YIT101 Turkish Language for International Students I (Compulsory, T:2 P:0 C:2 E:2)
AIT103 Ataturk's Principles and the History of Turkish Revolution I (Compulsory, T:2 P:0 C:2 E:2)
CHC100 Cyprus History and Culture (Compulsory, T:1 P:0 C:1 E:1)
Semester Total: Theory:18 Practice:8 Credits:23 ECTS:27""",

        # Year 1 - Semester 2
        """Year 1 - Semester 2 Courses:
ENG102 English II (Compulsory, T:2 P:0 C:3 E:3)
MTH102 Calculus II (Compulsory, T:3 P:2 C:4 E:5)
PHY102 General Physics II (Compulsory, T:3 P:2 C:4 E:5)
ENV102 Introduction to Environmental Engineering (Compulsory, T:2 P:0 C:2 E:2)
TD102 Technical Drawing (Compulsory, T:2 P:2 C:3 E:4)
CAR101 Career Planning (Compulsory, T:1 P:0 C:1 E:1)
YIT102 Turkish Language for International Students II (Compulsory, T:2 P:0 C:2 E:2)
AIT104 Ataturk's Principles and the History of Turkish Revolution II (Compulsory, T:2 P:0 C:2 E:2)
Semester Total: Theory:17 Practice:6 Credits:21 ECTS:24""",

        # Year 2 - Semester 1
        """Year 2 - Semester 1 Courses:
MTH201 Differential Equations and Linear Algebra (Compulsory, T:4 P:0 C:4 E:6)
MTH251 Statistics and Probability (Compulsory, T:3 P:0 C:3 E:6)
ENV201 Environmental Microbiology (Compulsory, T:3 P:2 C:4 E:6)
ENV202 Environmental Chemistry I (Compulsory, T:3 P:0 C:3 E:6)
ENV241 Materials Science (Compulsory, T:4 P:0 C:4 E:6)
ECC246 Engineering Economy (Compulsory, T:3 P:0 C:3 E:5)
Semester Total: Theory:20 Practice:2 Credits:21 ECTS:35""",

        # Year 2 - Semester 2
        """Year 2 - Semester 2 Courses:
ENV203 Thermodynamics (Compulsory, T:3 P:2 C:4 E:6)
ENV204 Environmental Chemistry II (Compulsory, T:3 P:2 C:4 E:6)
ENV371 Fluid Mechanics (Compulsory, T:3 P:2 C:4 E:6)
ENV206 Urban Hydrology (Compulsory, T:4 P:0 C:4 E:5)
Non-Technical Elective Course I (Elective, T:2 P:0 C:2 E:2)
Semester Total: Theory:15 Practice:6 Credits:18 ECTS:25""",

        # Year 3 - Semester 1
        """Year 3 - Semester 1 Courses:
ENV305 Chemical Processes (Compulsory, T:3 P:2 C:4 E:6)
ENV351 Unit Operations in Environmental Engineering (Compulsory, T:3 P:2 C:4 E:6)
ENV361 Water Quality Management (Compulsory, T:3 P:0 C:3 E:5)
ENV373 Engineering Ethics (Compulsory, T:2 P:0 C:2 E:3)
ENV381 Solid Waste Management (Compulsory, T:3 P:0 C:3 E:5)
ENV300 Summer Practice I - 30 days (Compulsory, T:0 P:0 C:0 E:0)
Semester Total: Theory:14 Practice:4 Credits:16 ECTS:25""",

        # Year 3 - Semester 2
        """Year 3 - Semester 2 Courses:
ECC206 Statics (Compulsory, T:3 P:0 C:3 E:4)
ENV326 Biological Processes (Compulsory, T:3 P:2 C:4 E:6)
ENV372 Hydromechanics (Compulsory, T:3 P:2 C:4 E:6)
ENV382 Water Treatment Plant Design (Compulsory, T:3 P:2 C:4 E:6)
ENV374 Air Pollution Control (Compulsory, T:3 P:2 C:4 E:6)
Semester Total: Theory:15 Practice:8 Credits:19 ECTS:28""",

        # Year 4 - Semester 1
        """Year 4 - Semester 1 Courses:
ENV431 Waste Water Treatment Plant Design (Compulsory, T:3 P:2 C:4 E:6)
ENV461 Earth Science (Compulsory, T:3 P:2 C:4 E:6)
ENV471 Water Resources Engineering (Compulsory, T:4 P:0 C:4 E:6)
ENV481 Environmental Modelling (Compulsory, T:4 P:0 C:4 E:6)
ENV400 Summer Practice II - 30 days (Compulsory, T:0 P:0 C:0 E:0)
Technical Elective I (Elective, T:3 P:0 C:3 E:5)
Semester Total: Theory:17 Practice:4 Credits:19 ECTS:29""",

        # Year 4 - Semester 2
        """Year 4 - Semester 2 Courses:
ENV472 Industrial Pollution Control (Compulsory, T:3 P:0 C:3 E:5)
ENV484 Hazardous Waste Control (Compulsory, T:3 P:0 C:3 E:5)
ENV486 Environmental Law (Compulsory, T:4 P:0 C:4 E:6)
ENV498 Special Project (Compulsory, T:4 P:0 C:4 E:6)
Technical Elective II (Elective, T:3 P:0 C:3 E:5)
Semester Total: Theory:17 Practice:0 Credits:17 ECTS:27""",

        # Program Summary
        """Environmental Engineering Program Summary:
Duration: 4 years
Total Courses: 48
Total Electives: 4
Total Credits: 158
Total ECTS: 240
Theory Hours: 139
Practice Hours: 38
Elective Percentage: 8%
Specializations: Water Treatment, Air Pollution Control, Waste Management, Environmental Modeling
Degree: Bachelor of Science in Environmental Engineering
Career Paths: Environmental Engineer, Water Treatment Specialist, Air Quality Engineer, Waste Management Engineer, Environmental Consultant""",

        # Core Specializations
        """Environmental Engineering Core Specializations:
1. Water and Wastewater Treatment:
   - Water Treatment Plant Design
   - Waste Water Treatment Plant Design
   - Water Quality Management
   
2. Air Pollution Control:
   - Air Pollution Control Technologies
   - Industrial Pollution Control
   
3. Solid Waste Management:
   - Solid Waste Management
   - Hazardous Waste Control
   
4. Environmental Systems:
   - Environmental Modeling
   - Water Resources Engineering
   - Urban Hydrology""",

        # Department Information
        """Department of Environmental Engineering Information:
Faculty: Faculty of Civil and Environmental Engineering
Website: https://insaatvecevre.neu.edu.tr/
Program Language: English
Curriculum PDF: https://insaatvecevre.neu.edu.tr/wp-content/uploads/sites/136/2023/11/23/Faculty-of-Civil-and-Environmental-Engineering-Department-of-Environmental-Engineering-4-ENG-ANNUAL.pdf
Admission Requirements: High school diploma, English proficiency, university entrance exam
Research Areas: Water treatment technologies, air pollution control, waste management, environmental modeling, sustainable engineering"""
    ]
    
    # Metadata for each document
    metadatas = [
        {"document_type": "faculty_info", "year": "all", "semester": "all", "department": "Environmental Engineering"},
        {"document_type": "curriculum", "year": "1", "semester": "1", "courses_count": "9"},
        {"document_type": "curriculum", "year": "1", "semester": "2", "courses_count": "8"},
        {"document_type": "curriculum", "year": "2", "semester": "1", "courses_count": "6"},
        {"document_type": "curriculum", "year": "2", "semester": "2", "courses_count": "5"},
        {"document_type": "curriculum", "year": "3", "semester": "1", "courses_count": "6"},
        {"document_type": "curriculum", "year": "3", "semester": "2", "courses_count": "5"},
        {"document_type": "curriculum", "year": "4", "semester": "1", "courses_count": "6"},
        {"document_type": "curriculum", "year": "4", "semester": "2", "courses_count": "5"},
        {"document_type": "program_summary", "year": "all", "semester": "all", "total_credits": "158", "total_ects": "240"},
        {"document_type": "specializations", "year": "all", "semester": "all", "specialization_areas": "4"},
        {"document_type": "department_info", "year": "all", "semester": "all", "website": "https://insaatvecevre.neu.edu.tr/"}
    ]
    
    # Generate IDs
    ids = [f"env_eng_{i:03d}" for i in range(len(documents))]
    
    # Add to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} environmental engineering documents to new collection!")
        
        # Verify
        count = collection.count()
        print(f"Total documents in neu_environmental_engineering: {count}")
        
        # Test query
        test_results = collection.query(
            query_texts=["environmental engineering water treatment"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_environmental_engineering_collection()