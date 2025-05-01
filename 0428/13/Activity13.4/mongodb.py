import pymongo
from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client.pluto
posts = db.posts

def write(stamps):
    for stamp in stamps:
        item = {'stamp': stamp}
        posts.update_one(item, {'$set': item}, upsert=True)

def read():
    return [p['stamp'] for p in posts.find()
            .sort('stamp', pymongo.DESCENDING)
            .limit(5)]

def delete():
    posts.delete_many({})
