#Using Python to interact with the mongodb server with pymongo

from pymongo import MongoClient

#pprint module will help to improve readability
from pprint import pprint

DB_connectionString = "mongodb://127.0.0.1:27017"
client = MongoClient(DB_connectionString)
#use userManager
dbase = client.userManager


#creating a collection and creating a document

#userinfo = dbase.createCollection("usersinfo")
info1 = {
      "_id": "59071791b0lkscm2325794",
          "name": "John Doe", 
            "email": "john.doe@gmail.com", 
            "password": "johndoe", 
            "__v": "0"
        }
docInsert = dbase.usersinfo.insert(info1)


#Performing other CRUD operations

#Retrieving a document
docObj = dbase.usersinfo.find({"_id":"59071791b0lkscm2325794"})
print("The data retrieved is: ")
pprint(docObj)


#Update a document with a new field
docUpdate = dbase.usersinfo.update({"website":"https://github.com", "__v":"0"})
#updating a document by replacing an existing field
docReplace = dbase.usersinfo.replace({"password": "johndoe", "password": "doejohn"})

#delete a document
docDelete = dbase.usersinfo.delete({"_id":"59071791b0lkscm2325794"})

