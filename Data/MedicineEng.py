import chromadb
from chromadb.utils import embedding_functions

def add_medical_school_curriculum_to_chromadb():
    """Add Medical School curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_medical_school",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_medical_school",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_medical_school")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """Faculty of Medicine English - Medical School Curriculum Overview
Degree: Doctor of Medicine (MD)
Program Duration: 6 years (Phases I-VI)
Program Structure: Integrated medical education with clinical training

Phase Structure:
- Phase I (Year 1): Basic Medical Sciences
- Phase II (Year 2): Systems-Based Medicine
- Phase III (Year 3): Clinical Pathology
- Phase IV (Year 4): Core Clerkships
- Phase V (Year 5): Specialized Clerkships & Electives
- Phase VI (Year 6): Internship Year

Note: Some courses are not compulsory for international students""",

        # PHASE I - Year 1
        """PHASE I - First Year (Basic Medical Sciences):
MED101, Cell Science I, Duration: 7 Weeks
MED102, Cell Science II, Duration: 9 Weeks
MED103, Cell Science III, Duration: 7 Weeks
MED104, Cell Science IV, Duration: 9 Weeks
AIT101, Atatürk & Modern Turkish History 1, Duration: 1 Semester (Not compulsory for international students)
AIT102, Atatürk & Modern Turkish History 2, Duration: 1 Semester (Not compulsory for international students)
ENG101, Written & Oral Communication Skills 1, Duration: 1 Semester
ENG102, Written & Oral Communication Skills 2, Duration: 1 Semester
TURK101, Turkish Language & Literature 1, Duration: 1 Semester (Not compulsory for international students)
TURK102, Turkish Language & Literature 2, Duration: 1 Semester (Not compulsory for international students)

Semester Break: 2 weeks

Focus: Foundation in basic medical sciences, cellular biology, and communication skills""",

        # PHASE II - Year 2
        """PHASE II - Second Year (Systems-Based Medicine):
MED201, Tissue & Skeletal Systems, Duration: 3 Weeks
MED202, Muscle & Peripheral Nervous Systems, Duration: 5 Weeks
MED203, Nervous System, Duration: 6 Weeks
MED204, Cardiovascular, Respiratory & Blood Systems, Duration: 5 Weeks
MED205, Gastrointestinal System, Duration: 4 Weeks
MED206, Endocrine & Urogenital Systems, Duration: 4 Weeks
MED207, Basic Diseases of Fundamentals, Duration: 4 Weeks

Semester Break: 2 weeks

Focus: Systems-based approach to human anatomy, physiology, and basic pathology""",

        # PHASE III - Year 3
        """PHASE III - Third Year (Clinical Pathology):
MED301, Infectious Diseases, Duration: 5 Weeks
MED302, Neoplasia & Hematopoietic Diseases, Duration: 3 Weeks
MED303, Cardiovascular & Respiratory Diseases, Duration: 4 Weeks
MED304, Gastrointestinal Diseases, Duration: 3 Weeks
MED305, Endocrine & Metabolism Diseases, Duration: 3 Weeks
MED306, Neurological & Psychiatric Diseases, Duration: 4 Weeks
MED307, Urogenital Diseases, Duration: 4 Weeks
MED308, Musculo-skeletal Diseases, Duration: 2 Weeks
MED309, Public Health, Forensic Medicine, Biostatistics, Duration: 5 Weeks

Semester Break: 2 weeks

Focus: Disease pathology, clinical medicine foundations, and public health""",

        # PHASE IV - Year 4
        """PHASE IV - Fourth Year (Core Clerkships):
MED401, Internal Medicine, Duration: 9 Weeks
MED402, Pediatrics, Duration: 9 Weeks
MED403, General Surgery, Duration: 9 Weeks
MED404, Obstetrics & Gynecology, Duration: 9 Weeks
MED405, Clinical Pharmacology, Duration: 1 Week

Semester Break: 1-2 weeks

Focus: Core clinical rotations in major medical specialties, hands-on patient care""",

        # PHASE V - Year 5
        """PHASE V - Fifth Year (Specialized Clerkships & Electives):
MED501, Clinical Ethics, Duration: 1 Week (Varies by student group)
MED502, Dermatology, Duration: 3 Weeks (Varies by student group)

Elective Rotations (Duration: 1-3 Weeks each):
- Cardiovascular Surgery
- Plastic & Reconstructive Surgery
- Pediatric Surgery
- Anesthetics
- Neurosurgery
- Emergency Medicine
- Evidence-Based Medicine
- Forensic Medicine
- Infectious Diseases
- Neurology
- Nuclear Medicine
- Ophthalmology
- Orthopedics & Traumatology
- Otorhinolaryngology
- Physical Medicine & Rehabilitation
- Psychiatry + Child & Adolescent Psychiatry
- Radiology
- Radiation Oncology
- Urology

Focus: Specialized clinical exposure and elective rotations for career exploration""",

        # PHASE VI - Year 6
        """PHASE VI - Sixth Year (Internship Year):
Internship Duration: 12 months (July 1 to June 30)

Core Rotations:
- Emergency Medicine, Duration: 1 Month
- Obstetrics & Gynecology, Duration: 2 Months
- Pediatrics, Duration: 2 Months
- Internal Medicine, Duration: 2 Months
- Public Health, Duration: 2 Months
- General Surgery, Duration: 1 Month

Elective Rotations:
- Elective Course I, Duration: 1 Month (Student group dependent)
- Elective Course II, Duration: 1 Month (Student group dependent)

Focus: Comprehensive clinical practice and preparation for medical licensure""",

        # Elective Courses Detailed
        """Elective Courses (1-month each, durations may vary):
Surgical Specialties:
- Cardiovascular Surgery
- Neurosurgery
- Pediatric Surgery
- Plastic & Reconstructive Surgery
- Orthopedics & Traumatology

Medical Specialties:
- Cardiology
- Dermatology
- Endocrinology
- Gastroenterology
- Infectious Diseases
- Neurology
- Nuclear Medicine
- Psychiatry

Diagnostic & Support Services:
- Radiology
- Radiation Oncology
- Anesthesiology & Reanimation
- Emergency Medicine
- Physical Medicine & Rehabilitation

Basic Medical Sciences:
- Anatomy
- Biophysics
- Histology & Embryology
- Physiology
- Medical Biochemistry
- Medical Biology
- Medical Genetics
- Microbiology & Clinical Microbiology
- Pathology

Other Specialties:
- Forensic Medicine
- Ophthalmology
- Otorhinolaryngology
- Urology
- Sports Medicine
- Medical Education & Informatics
- Biostatistics

Note: Elective availability and duration may vary by academic year and student group""",

        # Program Structure Summary
        """Medical Program Structure Summary:
Total Duration: 6 years
Total Phases: 6 (I-VI)
Program Type: Integrated MD Program

Phase Overview:
- Phase I: Basic sciences and foundational knowledge
- Phase II: Systems-based medical education
- Phase III: Clinical pathology and disease mechanisms
- Phase IV: Core clinical clerkships
- Phase V: Specialized clerkships and electives
- Phase VI: Internship and clinical practice

Key Features:
- Progressive integration of basic and clinical sciences
- Early clinical exposure
- Comprehensive elective system for specialization
- 12-month internship for hands-on clinical experience
- International student-friendly curriculum (some courses optional)

Graduation Requirements:
- Successful completion of all phases
- Passing all required examinations
- Completion of internship year
- Meeting clinical competency standards""",

        # Career Pathways
        """Medical Career Pathways after Graduation:
Primary Care Specialties:
- Family Medicine
- Internal Medicine
- Pediatrics
- General Practice

Surgical Specialties:
- General Surgery
- Orthopedic Surgery
- Cardiovascular Surgery
- Neurosurgery
- Plastic Surgery

Medical Specialties:
- Cardiology
- Neurology
- Gastroenterology
- Endocrinology
- Infectious Diseases
- Dermatology

Hospital-based Specialties:
- Anesthesiology
- Radiology
- Pathology
- Emergency Medicine
- Physical Medicine & Rehabilitation

Other Specialties:
- Psychiatry
- Obstetrics & Gynecology
- Ophthalmology
- Otorhinolaryngology
- Urology

Academic and Research Careers:
- Medical Research
- Academic Medicine
- Medical Education
- Public Health
- Medical Administration

Note: Additional residency training required for specialization after MD degree""",

        # International Student Information
        """Information for International Students:
Optional Courses (Not compulsory for international students):
- AIT101, Atatürk & Modern Turkish History 1
- AIT102, Atatürk & Modern Turkish History 2
- TURK101, Turkish Language & Literature 1
- TURK102, Turkish Language & Literature 2

Language of Instruction: English
Clinical Training: Conducted in English and Turkish healthcare settings
Degree Recognition: MD degree recognized internationally
Licensing: Eligibility for various international medical licensing examinations

Support Services:
- International student office
- Language support services
- Clinical placement assistance
- Career counseling for international practice

Note: International students should verify specific licensing requirements in their home countries"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "faculty": "Medical School",
            "degree": "Doctor of Medicine (MD)",
            "document_type": "program_info",
            "content_type": "general_info"
        },
        {
            "phase": "I",
            "year": "1",
            "document_type": "course_list",
            "content_type": "phase_i_basic_sciences"
        },
        {
            "phase": "II",
            "year": "2",
            "document_type": "course_list",
            "content_type": "phase_ii_systems_medicine"
        },
        {
            "phase": "III",
            "year": "3",
            "document_type": "course_list",
            "content_type": "phase_iii_clinical_pathology"
        },
        {
            "phase": "IV",
            "year": "4",
            "document_type": "course_list",
            "content_type": "phase_iv_core_clerkships"
        },
        {
            "phase": "V",
            "year": "5",
            "document_type": "course_list",
            "content_type": "phase_v_specialized_electives"
        },
        {
            "phase": "VI",
            "year": "6",
            "document_type": "course_list",
            "content_type": "phase_vi_internship"
        },
        {
            "course_type": "elective",
            "document_type": "course_list",
            "content_type": "detailed_electives"
        },
        {
            "document_type": "program_info",
            "content_type": "program_structure"
        },
        {
            "document_type": "program_info",
            "content_type": "career_pathways"
        },
        {
            "document_type": "program_info",
            "content_type": "international_students"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"med_school_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Medical School curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["medical school clerkship internship"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_medical_school_curriculum_to_chromadb()