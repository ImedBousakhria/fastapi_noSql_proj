from fastapi import FastAPI
app = FastAPI()


from schemas import list_serializer
from database import db, collection_name
@app.get("/todos", tags=['TODOS'])
def get_todos():
     todos = list_serializer(collection_name.find())
     return todos
