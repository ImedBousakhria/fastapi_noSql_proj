from pymongo import MongoClient

client = MongoClient("mongodb+srv://ibousakhria:imed123!@cluster0.jpliqa5.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_db
collection_name = db["todo_collection"]
