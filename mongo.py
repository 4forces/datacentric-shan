import pymongo
import os

MONGODB_URI ="mongodb+srv://root:Administrator1@cluster0.expze.mongodb.net/?retryWrites=true&w=majority"

DBS_NAME = "myFirstdb"
COLLECTION_NAME  = "myFirstTable"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is conected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
    
# conn = mongo_connect(MONGODB_URI)

# coll = conn[DBS_NAME][COLLECTION_NAME]

# documents = coll.find().limit(5)

# for doc in documents:
#     print(doc)

def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")
    return option

def add_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter date of birth > ")
    gender = input("Enter gender > ")
    hair_colour = input("Enter hair colour > ")
    occupation = input("Enter occupatoin > ")
    nationality = input("Enter nationality > ")

    new_doc = {'first':first,'last':last,'dob':dob,'gender':gender,'hair_colour':hair_colour,'occupation':occupation,'nationality':nationality}

    try:
        coll.insert(new_doc)
        print("")
        print("Doc inserted")
    except: 
        print("Error connecting to database")


def find_record():
    if doc:
        print("")
        for k,v in doc.items():
            if k != "_id":
                print(k + ": " + v)


def main_loop():
    while True:
        option = show_menu()
        if option == '1':
            add_record()
        elif option == '2':
            find_record()
        elif option == '3':
            print("Edit record")
        elif option == '4':
            print("Delete record")
        elif option == '5':
            conn.close()
            break
        else:
            print("Invalid option")

conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()
        


