import chromadb
from chromadb.utils import embedding_functions

def create_civil_engineering_collection():
    """Create a separate collection for Civil Engineering curriculum"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create a NEW collection for civil engineering
    try:
        # First check if it exists and delete it to start fresh
        try:
            chroma_client.delete_collection("neu_civil_engineering")
            print("Removed existing civil engineering collection")
        except:
            print("No existing civil engineering collection found")
        
        # Create new collection
        collection = chroma_client.create_collection(
            name="neu_civil_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_civil_engineering")
        
    except Exception as e:
        print(f"Error creating collection: {e}")
        return
    
    # Prepare civil engineering curriculum documents
    documents = [
        # Faculty Information
        """Faculty: Faculty of Civil and Environmental Engineering
Department: Department of Civil Engineering
Program: Civil Engineering 4-Year Program (English)
Program Type: Annual
Language: English
Total Credits: 158
Total ECTS: 240
Description: Comprehensive civil engineering program covering structural, geotechnical, transportation, and water resources engineering""",

        # Year 1 - Semester 1
        """Year 1 - Semester 1 Courses:
ENG101 Foreign Language I: English I (Compulsory, Theory:2 Practice:0 Credits:3 ECTS:3)
MTH101 Mathematics I: Mathematics I (Compulsory, T:4 P:0 C:4 E:5)
PHY101 General Physics I: General Physics I (Compulsory, T:3 P:2 C:4 E:5)
CHM101 General Chemistry: General Chemistry (Compulsory, T:3 P:2 C:4 E:5)
ECC101 Introduction to Computers and Programming (Compulsory, T:2 P:2 C:3 E:4)
YIT101 Turkish Language for International Students I (Compulsory, T:2 P:0 C:2 E:2)
CAM100 Campus Orientation (Compulsory, T:0 P:0 C:0 E:0)
AIT103 Principles of Ataturk and The History of Turkish Reforms I (Compulsory, T:2 P:0 C:2 E:2)
CHC100 Cyprus History and Culture (Compulsory, T:1 P:0 C:1 E:1)
Semester Total: Theory:19 Practice:4 Credits:23 ECTS:27""",

        # Year 1 - Semester 2
        """Year 1 - Semester 2 Courses:
ENG102 Foreign Language II: English II (Compulsory, T:2 P:0 C:3 E:3)
MTH102 Mathematics II: Mathematics II (Compulsory, T:4 P:0 C:4 E:5)
PHY102 General Physics II: General Physics II (Compulsory, T:2 P:2 C:4 E:5)
GEO102 Geology for Civil Engineers (Compulsory, T:2 P:0 C:2 E:3)
TD102 Technical Drawing (Compulsory, T:2 P:2 C:3 E:4)
YIT102 Turkish Language for International Students II (Compulsory, T:2 P:0 C:2 E:2)
CAR100 Career Planning (Compulsory, T:1 P:0 C:1 E:1)
Semester Total: Theory:15 Practice:4 Credits:19 ECTS:23""",

        # Year 2 - Semester 1
        """Year 2 - Semester 1 Courses:
MTH201 Differential Equations (Compulsory, T:4 P:0 C:4 E:5)
MTH251 Probability and Statistics (Compulsory, T:3 P:0 C:3 E:5)
CIV206 Statics (Compulsory, T:3 P:0 C:3 E:5)
ECC246 Economics for Engineers (Compulsory, T:3 P:0 C:3 E:4)
CIV241 Materials Science (Compulsory, T:3 P:0 C:3 E:5)
AIT104 Principles of Ataturk and The History of Turkish Reforms II (Compulsory, T:2 P:0 C:2 E:2)
Semester Total: Theory:18 Practice:0 Credits:18 ECTS:26""",

        # Year 2 - Semester 2
        """Year 2 - Semester 2 Courses:
MTH232 Advanced Mathematics for Engineering Sciences (Compulsory, T:3 P:0 C:3 E:5)
CIV204 Surveying and Engineering (Compulsory, T:2 P:2 C:4 E:6)
ECC212 Dynamics (Compulsory, T:3 P:0 C:3 E:5)
CIV213 Strength of Materials (Compulsory, T:4 P:0 C:4 E:6)
CIV244 Materials of Construction (Compulsory, T:3 P:0 C:4 E:6)
Non-Technical Elective Course II (Elective, T:2 P:0 C:2 E:2)
Semester Total: Theory:17 Practice:2 Credits:20 ECTS:30""",

        # Year 3 - Semester 1
        """Year 3 - Semester 1 Courses:
MTH323 Numerical Analysis (Compulsory, T:3 P:0 C:3 E:6)
CIV351 Transportation Engineering (Compulsory, T:3 P:0 C:3 E:5)
CIV361 Soil Mechanics I (Compulsory, T:3 P:2 C:4 E:6)
CIV371 Fluid Mechanics (Compulsory, T:3 P:2 C:4 E:6)
CIV381 Structural Analysis I (Compulsory, T:3 P:2 C:4 E:6)
CIV300 Summer Practice I (Compulsory, T:0 P:0 C:0 E:0)
Semester Total: Theory:15 Practice:6 Credits:18 ECTS:29""",

        # Year 3 - Semester 2
        """Year 3 - Semester 2 Courses:
CIV310 Computer Applications in Civil Engineering (Compulsory, T:3 P:0 C:3 E:4)
CIV362 Soil Mechanics II (Compulsory, T:3 P:2 C:4 E:6)
CIV372 Hydromechanics (Compulsory, T:3 P:0 C:3 E:5)
CIV382 Structural Analysis II (Compulsory, T:3 P:2 C:4 E:6)
CIV374 Engineering Hydrology (Compulsory, T:3 P:2 C:4 E:6)
Semester Total: Theory:15 Practice:6 Credits:18 ECTS:27""",

        # Year 4 - Semester 1
        """Year 4 - Semester 1 Courses:
CIV431 Construction Engineering and Management (Compulsory, T:4 P:0 C:4 E:6)
CIV461 Foundation Engineering (Compulsory, T:4 P:0 C:4 E:6)
CIV471 Water Resources Engineering I (Compulsory, T:4 P:0 C:4 E:6)
CIV481 Reinforced Concrete Theory (Compulsory, T:4 P:0 C:4 E:6)
Technical Elective Course I (Elective, T:3 P:0 C:3 E:5)
CIV400 Summer Practice II (Compulsory, T:0 P:0 C:0 E:0)
Semester Total: Theory:19 Practice:0 Credits:19 ECTS:29""",

        # Year 4 - Semester 2
        """Year 4 - Semester 2 Courses:
CIV472 Water Resources Engineering II (Compulsory, T:3 P:0 C:3 E:6)
CIV484 Design of Steel Structures (Compulsory, T:4 P:0 C:4 E:6)
CIV486 Structural Design (Compulsory, T:4 P:0 C:4 E:6)
CIV498 Special Project (Compulsory, T:4 P:0 C:4 E:8)
Technical Elective Course II (Elective, T:3 P:0 C:3 E:5)
Semester Total: Theory:18 Practice:0 Credits:18 ECTS:31""",

        # Program Summary
        """Civil Engineering Program Summary:
Duration: 4 years
Total Credits: 158
Total ECTS: 240
Theory Hours: 136
Practice Hours: 22
Compulsory Courses: 40+
Elective Courses: 3
Specializations: Structural, Geotechnical, Transportation, Water Resources Engineering
Degree: Bachelor of Science in Civil Engineering
Career Paths: Structural Engineer, Geotechnical Engineer, Transportation Engineer, Water Resources Engineer, Construction Manager""",

        # Department Info
        """Department of Civil Engineering Information:
Faculty: Faculty of Civil and Environmental Engineering
Website: https://insaatvecevre.neu.edu.tr/
Program Language: English
Admission: High school diploma, English proficiency, university entrance exam
Facilities: Modern laboratories, computer labs, research centers
Research Areas: Structural engineering, earthquake engineering, transportation systems, water resources, geotechnical engineering"""
    ]
    
    # Metadata for each document
    metadatas = [
        {"document_type": "faculty_info", "year": "all", "semester": "all"},
        {"document_type": "curriculum", "year": "1", "semester": "1"},
        {"document_type": "curriculum", "year": "1", "semester": "2"},
        {"document_type": "curriculum", "year": "2", "semester": "1"},
        {"document_type": "curriculum", "year": "2", "semester": "2"},
        {"document_type": "curriculum", "year": "3", "semester": "1"},
        {"document_type": "curriculum", "year": "3", "semester": "2"},
        {"document_type": "curriculum", "year": "4", "semester": "1"},
        {"document_type": "curriculum", "year": "4", "semester": "2"},
        {"document_type": "program_summary", "year": "all", "semester": "all"},
        {"document_type": "department_info", "year": "all", "semester": "all"}
    ]
    
    # Generate IDs
    ids = [f"civil_eng_{i:03d}" for i in range(len(documents))]
    
    # Add to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} civil engineering documents to new collection!")
        
        # Verify
        count = collection.count()
        print(f"Total documents in neu_civil_engineering: {count}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_civil_engineering_collection()