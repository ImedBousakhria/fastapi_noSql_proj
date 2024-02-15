from pydantic import BaseModel

def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "name": todo["_name"],
        "description": todo["_description"],
        "complete": todo["_complete"]
    }
    
def list_serializer(todos) -> list:
    return [individual_serial(todo) for todo in todos]



    