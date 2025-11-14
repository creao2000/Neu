import chromadb
from chromadb.utils import embedding_functions

def add_food_engineering_turkish_to_chromadb():
    """Add Food Engineering Turkish Program curriculum data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_food_engineering_turkish",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_food_engineering_turkish",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_food_engineering_turkish")
    
    # Prepare curriculum documents based on the provided data
    documents = [
        # Program Information
        """Near East University Faculty of Agriculture
Department of Food Engineering (Turkish Program)
Main website link: https://neu.edu.tr/academic/faculties/
Academic Program link: https://ziraat.neu.edu.tr/academic/academic-programmes/food-engineering-turkish-program/courses/""",

        # First Year First Semester
        """First Year - First Semester Courses (Year One or 1 First Semester):
CHM104, Chemistry For Biological Sciences, credit 4
ECC107, Biology, credit 2
ING101, English I, credit 3
MTH101, Mathematics I, credit 4
PHY101, Physics I, credit 4
FDE101, Introduction to Food Engineering, credit 1""",

        # First Year Second Semester
        """First Year - Second Semester Courses (Year One or 1 Second Semester):
CHM122, Organic Chemistry, credit 3
ENG102, English II, credit 3
MTH102, Mathematics II, credit 4
ECC016, Introduction to Computer & Programming, credit 3
PHY102, Physics II, credit 4
TD102, Technical Drawing, credit 3
YIT102, Turkish for Foreign Students, credit 2
AIT104, Atatürk Revolutions, credit 2""",

        # Second Year First Semester
        """Second Year - First Semester Courses (Year Two or 2 First Semester):
FDE201, Mass & Energy Balances, credit 3
ECC217, Microbiology, credit 3
FDE205, Biochemistry, credit 3
ENG201, Writing Techniques in Academic English, credit 3
MTH201, Differential Equations, credit 4
RNTE, Restricted Non-Technical Elective, credit 3""",

        # Second Year Second Semester
        """Second Year - Second Semester Courses (Year Two or 2 Second Semester):
FDE202, Thermodynamics, credit 4
FDE206, Food Microbiology, credit 4
FDE212, Food Engineering Unit Operations I, credit 4
CHM212, Analytical Chemistry, credit 3
FDE214, Engineering Materials, credit 3
RNTE, Restricted Non-Technical Elective, credit 3""",

        # Third Year First Semester
        """Third Year - First Semester Courses (Year Three or 3 First Semester):
FDE300, Summer Practice I, credit 0
FDE301, Instrumental Analysis, credit 3
FDE303, Food Chemistry I, credit 3
FDE311, Food Engineering Unit Operations II, credit 4
MTH251, Probability and Statistics, credit 3
TE, Technical Elective, credit 2""",

        # Third Year Second Semester
        """Third Year - Second Semester Courses (Year Three or 3 Second Semester):
FDE302, Food Analysis, credit 3
FDE304, Food Chemistry II, credit 3
FDE306, Food Engineering Applied Kinetics, credit 3
FDE312, Food Engineering Unit Operations III, credit 4
RNTE, Restricted Non-Technical Elective, credit 3
TE, Technical Elective, credit 2""",

        # Fourth Year First Semester
        """Fourth Year - First Semester Courses (Year Four or 4 First Semester - Final Year First Semester):
FDE400, Summer Practice II, credit 0
FDE401, Food Engineering Design I, credit 3
FDE403, Process Control, credit 3
FDE407, Food Packaging, credit 2
FDE411, Food Technology, credit 3
TE, Technical Elective, credit 3
TE, Technical Elective, credit 3""",

        # Fourth Year Second Semester
        """Fourth Year - Second Semester Courses (Year Four or 4 Second Semester - Final Year Second Semester):
FDE402, Food Engineering Design II, credit 3
FDE404, Quality Control in Food Engineering, credit 3
FDE412, Food Engineering Unit Operation Laboratory, credit 3
TE, Technical Elective, credit 3
TE, Technical Elective, credit 3""",

        # Technical Elective Courses
        """Technical Elective Courses:
FDE320, Industrial Microbiology, credit 2
FDE321, Food Biotechnology, credit 2
FDE322, Principles of Nutrition, credit 2
FDE323, Physical Properties of Food, credit 2
FDE421, Cereal Technology, credit 3
FDE422, Fermentation Technology, credit 3
FDE423, Fruit & Vegetable Technology, credit 3
FDE424, Sea Food Products Technology, credit 3
FDE425, Fats & Oil Technology, credit 3
FDE426, Dairy Technology, credit 3
FDE427, Meat Technology, credit 3
FDE430, Plant Sanitation, credit 3
FDE431, Food Economy & Management, credit 3
FDE432, Food Legislation, credit 3""",

        # Restricted Non-Technical Elective Courses
        """Restricted Non-Technical Elective Courses:
ECC426, Economics for Engineers, credit 3
ECC427, Management for Engineers, credit 3""",

        # Course Descriptions - Year 1
        """Course Descriptions - First Year Courses:

ECC107, Biology (2-0)2
An introduction to living earth, characteristics of living things, importance of water in life, inorganic materials, biological molecules, hormones, vitamins, enzymes, features of prokaryotic and eukaryotic cells, physical and chemical properties of cell, cell membrane structure and function, transports across cell membranes, organelles, aerobic, anaerobic respiration and fermentation, photosynthesis and chemosynthesis, ribosomes and protein synthesis, centrioles, DNA replication and repair, cellular reproduction.

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

ECC016, Introduction to Computer & Programming (3-0)3
Construction and abstraction of computer program. Structure of a Pascal program, data types, constants, input and output of integer numbers, real numbers. Arithmetic expressions. Control structures, Procedures. Enumerated types, array records and subscripted variables. Arrays. Files, pointers, linked-lists, queues.

ENG102, English II (3-0)3
This course will be a continuation of ENG 101, with greater emphasis on student autonomy, research skills and synthesizing ability. Documentation in writing will be introduced at the beginning of the course.
Prerequisite: ENG101

MTH102, Calculus II (4-0)4
Plane and polar co-ordinates, area in polar co-ordinates, arc length of curves. Limit continuity and differentiability of function of several variables, extreme values, and method of Lagrange multipliers. Double integral, triple integral with applications. Line integrals, Green's theorem. Sequences, infinite series, power series, Taylor's series. Complex numbers.
Prerequisite: MTH101

TD102, Technical Drawing (3-0)3
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
Basic principles in thermodynamics, chemical equilibrium concept, temperature and irreversibility, the first law, work and heat concepts, the second law and entropy, state equations and thermodynamic properties of pure substances, design and analysis of open and closed systems.
Prerequisite: FDE201

FDE212, Food Engineering Unit Operations I (4-2)4
Dimensional analysis, transport phenomena and fluid mechanics, properties of fluids, viscosity, density, surface tension, Newton's law, fluid statics, static balance, manometers, flow of fluids, mass balances, characteristics of flow, laminar flow boundary layer theory.
Prerequisite: MTH201

FDE301, Instrumental Analysis (3-2)3
Basic principles of spectroscopy, ultra violet and visible region spectroscopy, UV-VIS spectrophotometers, analytical applications, fluorescence and phosphorescence spectroscopy, refractometric and polarimetric methods and measurements, atomic absorption and flame emission spectroscopy.
Prerequisite: CHM212

FDE401, Food Engineering Design I (3-0)3
During one semester, students choose a design based topic in Food Engineering and conduct research about this topic using sources such as libraries, computer and laboratory facilities and prepare a trial plan. A final report in a scientific manuscript format and an oral presentation is prepared.
Prerequisite: FDE312""",

        # Program Overview and Career Opportunities
        """Food Engineering Turkish Program Overview:
Bachelor's Degree program in Turkish focusing on food processing, preservation, quality control, and food technology.
Combines engineering principles with food science and technology.
Includes practical training and summer practices in food plants.
Prepares students for careers in food industry, quality control, research and development in Turkish-speaking regions.

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
            "language": "Turkish Program",
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
            "course_type": "elective",
            "document_type": "course_list",
            "content_type": "restricted_non_technical_electives"
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
    ids = [f"food_engineering_turkish_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} Food Engineering Turkish Program curriculum documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["food engineering Turkish program"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_food_engineering_turkish_to_chromadb()