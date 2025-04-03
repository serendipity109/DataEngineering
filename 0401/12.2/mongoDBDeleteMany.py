from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["employee"]

collection = db["employees"]

filter = {"LastName": "Smith"}

collection.delete_many(filter)

employeeCursor = collection.find()

for employee in employeeCursor:
    print(employee)
