from pymongo import MongoClient
import datetime

def write_read():
    client = MongoClient("mongodb://localhost:1800/")
    db = client.demo
    coll = db.logs
    # 寫入
    coll.insert_one({"msg": "Test log", "ts": datetime.datetime.now()})
    # 讀取
    for doc in coll.find():
        print(doc)

if __name__ == "__main__":
    write_read()
