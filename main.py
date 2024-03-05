import pymongo
import asyncio

#connect to MongoDB --> prevent username from being uploaded to github

# goal is to export class as a module in other files to connect to database
class DatabaseObject:
    def read_uri_txt(self,file): #self must be the first arg
        reader = open(file, "r")
        return reader.readline()
    def connect_to_mongodb(self, file):
        try:
            uri = self.read_uri_txt(file)
            client = pymongo.MongoClient(uri)
        except pymongo.errors.ServerSelectionTimeoutError:
            print("fail")
        return client
    def connect_to_database(self,client,database_name):
        db = None
        for database in client.list_database_names():
            if database == database_name:
                db = client[database_name]
            else:
                return "Database not found"
        return db






obj = DatabaseObject()
client = obj.connect_to_mongodb("uri.txt")
db = obj.connect_to_database(client, "IOS-Todo-List")
db.create_collection("Test4")







# throw error if connection takes too long
# figure out TDD

# The python code communicates with MongoDB likely via an API that pymongo library communicates with.
#Mongodb exists on a server (the computer that it is stored on)
