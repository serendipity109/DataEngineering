from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["employee"]

collection = db["employees"]

# 定義要插入的文件資料
employeeCollection = [
    {"FirstName": "John", "LastName": "Smith", "Age": 25},
    {"FirstName": "Peter", "LastName": "Smith", "Age": 26},
    {"FirstName": "Gabriel", "LastName": "Smith", "Age": 28},
    {"FirstName": "Penny", "LastName": "Lane", "Age": 22},
    {"FirstName": "Eleanor", "LastName": "Rigby", "Age": 23},
    {"FirstName": "Helen", "LastName": "Rose", "Age": 23}
]

# 插入資料到 Collection 中
result = collection.insert_many(employeeCollection)

if "employee" in client.list_database_names():
	print("Employee database created!")
print(result.inserted_ids)
