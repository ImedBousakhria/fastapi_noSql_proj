from pydantic import BaseModel

def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "name": todo['name'],
        "description": todo['description'],
        "complete": todo['complete']
    }
    
def list_serializer(todos) -> list:
    return [individual_serial(todo) for todo in todos]


class Todo(BaseModel):
    name: str
    description: str
    complete: bool
    
    