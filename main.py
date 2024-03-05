from pymongo import MongoClient, errors
import asyncio

#connect to MongoDB --> prevent username from being uploaded to github
class DatabaseObject:
    def __init__(self):
        print("Connecting to MongoDB")
    def read_uri_txt(file):
        reader = open(file, "r")
        return reader.readline()

def connect_to_mongodb(uri):
    try:
        client = MongoClient(DatabaseObject.read_uri_txt("uri.txt"))
    except errors:
       print("Connection failed")

    # db = client["IOS-Todo-List"]
    # db.list_collection_names() #wait for result

uri = DatabaseObject().read_uri_txt()
connect_to_mongodb(uri)
print("hello")

