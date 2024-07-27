from pymongo import MongoClient
import config

client = MongoClient(config.MONGO_URI)
db = client['create_alert']
