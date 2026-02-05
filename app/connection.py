from pymongo import MongoClient
import os



class Mongo_connection:
    def __init__(self):
        try:
            self.client = MongoClient('mongodb://mongo-0.mongo:27017/')
            self.client['my_db']
            
          
        except ConnectionRefusedError as e:
            return str(e)  
        self.db = self.client['my_db']
        self.db.create_collection(os.getenv('MONGO_COLLECTION')) 
        self.collection = self.db[os.getenv('MONGO_COLLECTION')]  

