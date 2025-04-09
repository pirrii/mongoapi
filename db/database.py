from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

class Database:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client["pracmongo"]#

    def get_collection(self, collection_name):
        return self.db[collection_name]

# Instancia única de la base de datos
database = Database()