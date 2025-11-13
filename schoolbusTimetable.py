
# import chromadb

# # Initialize ChromaDB client
# chroma_client = chromadb.PersistentClient(path="./chroma_db")

# # List all collections first to confirm
# collections = chroma_client.list_collections()
# print("Current collections:", [col.name for col in collections])

# # Delete the specific collection
# try:
#     chroma_client.delete_collection(name="neu_bus_timetable")
#     print("✅ Collection 'neu_bus_timetable' deleted successfully!")
# except Exception as e:
#     print(f"❌ Error deleting collection: {e}")

# # Verify it's gone
# collections = chroma_client.list_collections()
# print("Remaining collections:", [col.name for col in collections])



import chromadb
from chromadb.utils import embedding_functions

def add_bus_timetable_to_chromadb():
    """Add comprehensive bus timetable data to ChromaDB"""
    
    # Initialize ChromaDB
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get collection
    try:
        collection = chroma_client.get_collection(
            name="neu_bus_timetable",
            embedding_function=sentence_transformer_ef
        )
        print("Collection exists, adding new data...")
    except:
        collection = chroma_client.create_collection(
            name="neu_bus_timetable",
            embedding_function=sentence_transformer_ef
        )
        print("Created new collection: neu_bus_timetable")
    
    # Prepare bus timetable documents based on the provided data
    documents = [
        # Main Timetable
        """Bus Timetable Main Routes:
Lefkoşa and Gönyeli Direct Route:
06:45

Lefkoşa, Gönyeli-Yenikent, Kızılbaş, Yeniken, Gönyeli Route:
07:15, 08:15, 09:15, 10:15, 11:15, 12:15, 13:15, 14:15, 15:15, 16:15, 17:15, 18:15, 19:15

Lefkoşa, Yenikent and Gönyeli  Route:
20:15, 22:15""",

        # Lefkoşa Route
        """Route: Lefkoşa Route
Days: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
Departure Place: Main bus stop facing the 8. Dorm building
Stops:
- YDÜ Kampüs Ana Durakları
- Kampüs YDÜ Bank Durakları
- Sanayi Durakları
- Tofaş Durakları
- Çangar Durakları
- Mezarlık Durakları
- Terminal Durakları
- Girne Kapısı Durakları
- Kumsal Park Durakları
- Sağlık Bakanlığı Durakları
- Tepe Home Durakları
- Lefkoşa Hastane Durakları
- Fuar Durakları
- Kampüs Hukuk Fak. Durakları
- Kampüs Ana Duraklar""",

        # Gönyeli Route
        """Route: Gönyeli Route
Days: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
Stops:
- YDÜ Kampüs Ana Duraklar
- Kampüs YDÜ Bank Durakları
- Gönyeli Stadı Önü Durakları
- Livera Durakları
- Yalçın Park Durakları
- Asker Durakları
- Büyük Kiler Durakları
- Deniz Plaza Durakları
- Küçük Kiler Durakları
- Kampüs Hukuk Fak. Durakları
- Kampüs Ana Duraklar""",

        # Yenikent Route
        """Route: Yenikent Route
Days: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
Stops:
- YDÜ Kampüs Ana Duraklar
- Kampüs YDÜ Bank Durakları
- Demir Market Durakları
- Yeni Yüzüyıl Arkası Durakları
- Mr. Pound Durakları
- Metehan Çemberi Durakları
- Belça Durakları
- Küçük Kiler Durakları
- Arçelik Durakları
- Gönyeli Belediyesi Durakları
- Kampüs Hukuk Fak. Durakları
- Kampüs Ana Duraklar""",

        # Yenikent - Gönyeli Route
        """Route: Yenikent - Gönyeli Route
Days: Monday, Tuesday, Wednesday, Thursday, Friday
Stops:
- YDÜ Kampüs Ana Duraklar
- Kampüs YDÜ Bank Durakları
- Üst Geçit Durakları
- Arda Market Durakları
- San Taşlar Durakları
- İmra Market Durakları
- Talihsiz Mobilya Durakları
- Ersoy Apt. Durakları
- Kampüs Hukuk Fak. Durakları
- Kampüs Ana Duraklar""",

        # Girne University Routes
        """Route: Near East University to Girne (Kyrenia University)
Days: Monday to Friday
Departure Place: Main bus stop facing the 8. Dorm building
Stops:
- Near East University
- Boğaz
- Barış Park
- Kar Market
- Grand Pasha
- Kyrenia University

Route: Girne (Kyrenia University) to Near East University
Days: Monday to Friday
Departure Place: Kyrenia University
Stops:
- Kyrenia University
- Grand Pasha
- Kar Market
- Barış Park
- Boğaz
- Near East University""",

        # Weekend Service
        """Weekend Service (Lefkoşa - Gönyeli - Yenikent)
Saturday Schedule:
06:45 → 07:15
08:15 → 10:15
12:15 → 14:15
17:15 → 18:15

Sunday Schedule:
10:00 → 12:00
14:00 → 16:00
18:00""",

        # University Shuttles
        """University Shuttle Services:

Girne University Shuttle
Days: Monday to Friday
From Near East University: 07:00, 11:00, 15:30
From Girne University: 08:00, 12:00, 17:00
Detailed Timings:
07:00 → 07:30
08:30 →
10:000 → 11:00
        → 13:30
13:30 → 14:30
15:30 → 17:00
18:00 → 19:00

Mağusa University Shuttle
07:30 or 17:15 → 11:00
2:30 → 04:00 → 18:30

Güzel Yurt Shuttle
Days: Monday to Friday
From Güzel Yurt: 07:00
From Near East University: 18:00""",

        # Important Notes
        """Important Notes and Service Information:
- Girne bus operates Monday to Friday only (no weekend service)
- Güzel Yurt shuttle operates Monday to Friday only (no weekend service)
- Girne and Mağusa bus timetable is arranged: left hours in Departure from University, right hours in Departure from Girne University
- All routes operate every day of the week unless specified otherwise
- Timings are in 24-hour format
- Buses depart from the main bus stop facing the 8th Dorm building at Near East University campus and front of Eğitim Sarayı
- Lefkoşa, Gönyeli-Yenikent, Kızılbaş, Yeniken, Gönyeli routes return to the main bus stop facing the 8th Dorm building at Near East University campus most of the time from 25 minutes to 55 minutes after departure time (may be affected by traffic conditions)
- School holidays and public holidays may affect the bus schedule
- Güzel Yurt shuttle: bus departs from Güzel Yurt at 07:00 and from Near East University at 18:00""",

        # Contact Information
        """Contact Information:
Website: https://bus.neu.edu.tr/
Phone Numbers:
+90 (392) 223 64 64
+90 (392) 680 20 00
Email: ulasim.mudurlugu@neu.edu.tr

Transportation Office:
Near East University Transportation Department
Available for bus schedules, route information, student transportation cards, complaints and suggestions"""
    ]
    
    # Corresponding metadata for each document
    metadatas = [
        {
            "document_type": "timetable",
            "content_type": "main_schedule",
            "routes": "Lefkoşa, Gönyeli, Yenikent"
        },
        {
            "route_name": "Lefkoşa Route",
            "operating_days": "Monday to Sunday",
            "stops_count": "15",
            "document_type": "route_info",
            "content_type": "lefkosa_route"
        },
        {
            "route_name": "Gönyeli Route",
            "operating_days": "Monday to Sunday",
            "stops_count": "11",
            "document_type": "route_info",
            "content_type": "gonyeli_route"
        },
        {
            "route_name": "Yenikent Route",
            "operating_days": "Monday to Sunday",
            "stops_count": "12",
            "document_type": "route_info",
            "content_type": "yenikent_route"
        },
        {
            "route_name": "Yenikent-Gönyeli Route",
            "operating_days": "Monday to Friday",
            "stops_count": "10",
            "document_type": "route_info",
            "content_type": "yenikent_gonyeli_route"
        },
        {
            "route_name": "Girne University Route",
            "operating_days": "Monday to Friday",
            "document_type": "route_info",
            "content_type": "girne_university_route"
        },
        {
            "service_name": "Weekend Service",
            "operating_days": "Saturday & Sunday",
            "document_type": "weekend_service",
            "content_type": "weekend_schedule"
        },
        {
            "service_name": "University Shuttles",
            "operating_days": "Monday to Friday",
            "document_type": "shuttle_service",
            "content_type": "university_shuttles"
        },
        {
            "title": "Service Notes",
            "document_type": "service_notes",
            "content_type": "important_information"
        },
        {
            "title": "Contact Information",
            "document_type": "contact_info",
            "content_type": "transportation_office"
        }
    ]
    
    # Generate unique IDs for each document
    ids = [f"bus_timetable_{i:03d}" for i in range(len(documents))]
    
    # Add documents to collection
    try:
        collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully added {len(documents)} bus timetable documents to ChromaDB!")
        
        # Verify the addition
        count = collection.count()
        print(f"Total documents in collection: {count}")
        
        # Test a sample query
        test_results = collection.query(
            query_texts=["bus schedule Girne university"],
            n_results=3
        )
        print(f"Test query returned {len(test_results['documents'][0])} results")
        
    except Exception as e:
        print(f"Error adding documents to ChromaDB: {e}")

# Function to run the data addition
if __name__ == "__main__":
    add_bus_timetable_to_chromadb()
