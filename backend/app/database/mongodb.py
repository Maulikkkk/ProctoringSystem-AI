from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "ai_proctoring"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Example placeholder collections
events_collection = db["events"]
