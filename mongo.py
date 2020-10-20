import os

MONGODB_URI ="mongodb+srv://root:Administrator1@cluster0.expze.mongodb.net/<dbname>?retryWrites=true&w=majority"

DBS_NAME = "myFirstdb"
COLLECTION_NAME  = "myFirstTable"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is conected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
    
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find().limit(5)

for doc in documents:
    print(doc)