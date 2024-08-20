import os
from pymongo import MongoClient


# this accepts new or existing collection 
# ayoko kasi mag schema kaya ganto nalang
# hahahahahahaahha
def dynamicCollection(collection_path):
    DB_URL = os.getenv('DATABASE_URL')
    client = MongoClient(DB_URL)
    db = client[collection_path]
    return db[collection_path]
      
 