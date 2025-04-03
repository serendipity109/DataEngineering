from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")

db = client["employee"]

collection = db["employees"]

employeeCursor = collection.find({"LastName": "Smith"})

for employee in employeeCursor:
    print(employee)
