from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["employee"]

collection = db["employees"]

filter = {"LastName": "Smith"}

newvalues = { "$set": { "Department": "Computer Science" } }

collection.update_many(filter, newvalues)

employeeCursor = collection.find()

for employee in employeeCursor:
    print(employee)
