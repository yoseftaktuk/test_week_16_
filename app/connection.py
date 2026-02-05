from pymongo import MongoClient
import os



class Mongo_connection:
    def __init__(self):
        try:
            self.client = MongoClient(
                host=os.getenv('MONGO_HOST'),
                port=os.getenv('MONGO_PORT'),
                username=os.getenv('MONGO_USERNAME'),
                password=os.getenv('MONGO_PASSWORD'),
                authSource=os.getenv('MONGO_AUTH_SOURCE')
            )
        except ConnectionRefusedError as e:
            return str(e)  
        self.db = self.client[os.getenv('MONGO_DB')]
        self.db.create_collection(os.getenv('MONGO_COLLECTION')) 
        self.collection = self.db[os.getenv('MONGO_COLLECTION')]  

