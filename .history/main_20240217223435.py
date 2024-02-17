from fastapi import FastAPI
from schemas import list_serializer, Todo
from database import collection_name

app = FastAPI()

@app.get("/todos", tags=['TODOS'])
async def get_todos():
     todos = list_serializer(collection_name.find())
     return todos


@app.post("/todos/create", tags=['TODOS'])
async def create_todo(todo: Todo):
     collection_name.insert_one(dict(todo))
     
@app.put("/todos/update_todo", tags=['TODOS'])
async def update_todo(todo_id: str, updated_todo: Todo):
     collection_name.find_one_and_update({"_id": i})