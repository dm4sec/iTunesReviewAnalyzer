from config import *
from pymongo import MongoClient


client = MongoClient(MONGO_IP, MONGO_PORT)
db = client.get_database("iTunes")
db.get_collection("app").create_index("trackId")
db.get_collection("comment").create_index("userReviewId", unique=True)
