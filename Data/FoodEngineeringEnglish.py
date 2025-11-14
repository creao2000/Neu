import chromadb
from chromadb.utils import embedding_functions

def add_food_engineering_curriculum_to_chromadb():
    """Add Food Engineering curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_food_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_food_engineering",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_food_engineering")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """Near East University Faculty of Agriculture
Department of Food Engineering (English Program)
Main website link: https://neu.edu.tr/academic/faculties/
Academic Program link: https://ziraat.neu.edu.tr/academic/academic-programmes/food-engineering-english-program/courses/""",

        # 1st Semester
        """First Year - First Semester Courses (Year One or 1 First Semester):
CAM100, Campus Orientation
MTH101, Calculus I
PHY101, General Physics I
CHM104, General Chemistry for Biological Sciences and Engineering
ECC107, Biology
FDE101, Introduction to Food Engineering
ENG101, English I
TUR101/YİT101, Turkish I/Turkish for International Students I
AİT101/AİT103, Atatürk's Principles and History of Turkish Revolutions I""",

        # 2nd Semester
        """First Year - Second Semester Courses (Year One or 1 Second Semester):
CHC100, Cyprus History and Culture
MTH102, Calculus II
PHY102, General Physics II
CHM122, Organic Chemistry
ECC103, Technical Drawing
ENG102, English II
TUR102/YİT102, Turkish II/Turkish for International Students II
AİT102/AİT104, Atatürk's Principles and History of Turkish Revolutions II""",

        # 3rd Semester
        """Second Year - First Semester Courses (Year Two or 2 First Semester):
FDE201, Mass and Energy Balances
ECC217, Microbiology
FDE205, Biochemistry
FDE214 (ECC211), Engineering Materials
MTH201, Differential Equations
FDE202 (ECC207), Thermodynamics
CAR100, Carrier Planning""",

        # 4th Semester
        """Second Year - Second Semester Courses (Year Two or 2 Second Semester):
ENG201, Oral Communication Skills
FDE206, Food Microbiology
ECC101, Introduction to Computer and Programming
CHM212, Analytical Chemistry
AGR426, Agricultural Economics
AGR427, Agricultural Business and Management
NTE, Non-technical Elective""",

        # 5th Semester
        """Third Year - First Semester Courses (Year Three or 3 First Semester):
FDE300, Summer Practice I
FDE301, Instrumental Analysis
FDE303, Food Chemistry I
FDE212 (ECC304), Food Engineering Unit Operation I
MTH251, Probability and Statistics
TE, Technical Elective Course""",

        # 6th Semester
        """Third Year - Second Semester Courses (Year Three or 3 Second Semester):
FDE302, Food Analysis
FDE304, Food Chemistry II
FDE306, Food Engineering Applied Kinetics
FDE311 (ECC316), Food Engineering Unit Operations II
FDE312 (ECC334), Food Engineering Unit Operations III
TE, Technical Elective Course""",

        # 7th Semester
        """Fourth Year - First Semester Courses (Year Four or 4 First Semester - Final Year First Semester):
FDE400, Summer Practice II
FDE401, Food Engineering Design I
FDE403, Process Control
FDE407, Food Packaging Technology
FDE411, Food Technology
TE, Technical Elective Course""",

        # 8th Semester
        """Fourth Year - Second Semester Courses (Year Four or 4 Second Semester - Final Year Second Semester):
FDE402, Food Engineering Design II
FDE404, Quality Control in Food Engineering
FDE412, Food Engineering Unit Operation Laboratory
TE, Technical Elective Course
TE, Technical Elective Course
TE, Technical Elective Course""",

        # Elective Courses
        """Technical Elective Courses:
FDE320, Industrial Microbiology
FDE321, Food Biotechnology
FDE322, Principles of Nutrition
FDE323, Physical Properties of Food
FDE421, Cereal Technology
FDE422, Fermentation Technology
FDE423, Fruit and Vegetable Technology
FDE424, Sea Food Products Technology
FDE425, Fats and Oils Technology
FDE426, Dairy Technology
FDE427, Meat Technology
FDE430, Plant Sanitation
FDE431, Food Economy and Management
FDE432, Food Legislation
AGR402, Organic Farming
AGR426, Agricultural Economics
AGR427, Agricultural Business and Management""",

        # Course Descriptions - Year 1
        """Course Descriptions - First Year Courses:

ECC107, Biology (2-0)2
An introduction to life earth, characteristics of living things, importance of water in life, inorganic materials, biological molecules, hormones, vitamins, enzymes, features of prokaryotic and eukaryotic cells, physical and chemical properties of cell, cell membrane structure and function, transports across cell membranes, organelles, aerobic, anaerobic respiration and fermentation, photosynthesis and kemosynthesis, ribosomes and protein synthesis, centrioles, DNA replication and repair, cellular reproduction.

CHM104, General Chemistry for Biological Sciences & Engineering (3-2)4
A basic course with emphasizing the metric system. Introduction to atomic theory, stoichiometry. The structural and physical properties of matter. Periodic relationship among elements and periodic table. Gaseous state. Thermo-chemistry. Energy and enthalpy. Electronic structure of atoms. Chemical bonding.

ENG101, English I (3-0)3
Within a thematic approach, reading, writing, speaking, and listening skills will be developed. In speaking and writing, students will be encouraged to use language forms that they learn through reading and listening. Under broad themes, the students will be exposed to extensive reading both in and outside the classroom.

FDE101, Introduction to Food Engineering (1-0)1
Definition and importance of food engineering, relationship of food engineering with other disciplines, main characteristics and functions of foods, food processing methods, food preservation techniques.

MTH101, Calculus I (4-0)4
Functions, limits and continuity. Derivatives. Average value theorem. Graph plotting. Integrals. Logarithmic, trigonometric and reverse trigonometric functions and their derivatives. L'hospital's rules. Integral methods, applications of integrals and irregular integrals.

PHY101, General Physics I (3-2)4
Measurement, vectors, kinematics, force, mass. Newton's laws, applications of Newton's laws. Work and kinetic energy. Conservation of linear momentum. Impulse, collisions, rotation, moments of inertia. Torque, angular momentum, conservation of angular momentum, static equilibrium.""",

        # Course Descriptions - Year 2
        """Course Descriptions - Second Year Courses:

FDE205, Biochemistry (3-2)3
Cell structure and material transport from cell membrane, introduction to metabolism, carbohydrate metabolism, biological oxidation, photosynthesis, lipid metabolism, aminoacid metabolism, definition and biosynthesis of nucleic acid, biosynthesis of nucleotides, biosynthesis of proteins, enzymes, co-enzymes.
Prerequisite: CHM104

ECC101, Introduction to Computer & Programming (3-0)3
Construction and abstraction of computer program. Structure of a Pascal program, data types, constants, input and output of integer numbers, real numbers. Arithmetic expressions. Control structures, Procedures. Enumerated types, array records and subscripted variables. Arrays. Files, pointers, linked-lists, queues.

ENG102, English II (3-0)3
This course will be a continuation of ENG 101, with greater emphasis on student autonomy, research skills and synthesizing ability. Documentation in writing will be introduced at the beginning of the course.
Prerequisite: ENG101

MTH102, Calculus II (4-0)4
Plane and polar co-ordinates, area in polar co-ordinates, arc length of curves. Limit continuity and differentiability of function of several variables, extreme values, and method of Lagrange multipliers. Double integral, triple integral with applications. Line integrals, Green's theorem. Sequences, infinite series, power series, Taylor's series. Complex numbers.
Prerequisite: MTH101

ECC103, Technical Drawing (3-0)3
Fundamentals of engineering drawing, introductory materials, use of instruments, lettering, constructional geometry, orthographic drawing, sectioning, dimensioning, pictorial drawing and sketching, isometric projection, assembly drawing, assembly elements.

PHY102, General Physics II (3-2)4
Electrical charges. Coulomb's law. Electrical fields. Gauss's law. Electrical potential. Capacitance and dielectrics. Current and resistance. Direct current circuits. Magnetic fields. Sources of the magnetic field. Faraday's law of induction. Inductance and inductors.
Prerequisite: PHY101""",

        # Course Descriptions - Core Food Engineering Courses
        """Course Descriptions - Core Food Engineering Courses:

FDE201, Mass and Energy Balances (3-0)3
Systems of units and dimensions. Dimensional equations and consistency. Concentration, force, weight, pressure and temperature. Definition of types of process, operation and system. Block diagram representation of a process. Material balances for steady-state open systems and for steady-state open systems with recycle, by-pass and purge.
Prerequisite: CHM104

FDE202, Thermodynamics (4-0)4
Basic principles in thermodynamic, chemical equilibrium concept, temperature and irreversibility, the first law, work and heat concepts, the second law and entropy, state equations and thermodynamic properties of pure substances, design and analysis of open and closed systems.
Prerequisite: FDE201

FDE212, Food Engineering Unit Operations I (4-2)4
Dimensional analysis, transport phenomena and fluid mechanics, properties of fluids, viscosity, density, surface tension, Newton's law, fluid statics, static balance, manometers, flow of fluids, mass balances, characteristics of flow, laminar flow boundary layer theory.
Prerequisite: MTH201

FDE301, Instrumental Analysis (3-2)3
Basic principles of spectroscopy, ultra violet and visible region spectroscopy, UV-VIS spectrophotometers, analytical applications, fluorescence and phosphorescence spectroscopy, refractometric and polarimetric methods and measurements, atomic absorption and flame emmission spectroscopy.
Prerequisite: CHM212

FDE401, Food Engineering Design I (3-0)3
During one semester, students choose a design based topic in Food Engineering and conduct research about this topic using sources such as libraries, computer and laboratory facilities and prepare a trial plan. A final report in a scientific manuscript format and an oral presentation is prepared.
Prerequisite: FDE312""",

        # Program Overview and Career Opportunities
        """Food Engineering Program Overview:
Bachelor's Degree program focusing on food processing, preservation, quality control, and food technology.
Combines engineering principles with food science and technology.
Includes practical training and summer practices in food plants.
Prepares students for careers in food industry, quality control, research and development.

Career Opportunities for Food Engineering Graduates:
Food Engineer
Quality Control Manager
Food Technologist
Production Manager
Research and Development Specialist
Food Safety Auditor
Process Engineer
Product Development Specialist"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "department": "Food Engineering",
            "faculty": "Agriculture",
            "language": "English Program",
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
            "year": "1",
            "document_type": "course_description",
            "content_type": "first_year_courses"
        },
        {
            "year": "2",
            "document_type": "course_description",
            "content_type": "second_year_courses"
        },
        {
            "course_type": "core",
            "document_type": "course_description",
            "content_type": "food_engineering_core_courses"
        },
        {
            "document_type": "program_info",
            "content_type": "program_overview_careers"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"food_engineering_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Food Engineering curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["food engineering courses"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_food_engineering_curriculum_to_chromadb()