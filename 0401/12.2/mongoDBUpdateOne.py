from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["employee"]

collection = db["employees"]

filter = {"LastName": "Rose"}

newvalues = { "$set": { "Age": 32 } }

collection.update_one(filter, newvalues)

employeeCursor = collection.find()

for employee in employeeCursor:
    print(employee)
