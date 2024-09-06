from pydantic import BaseModel

# Model for an individual item inside a todo
class Item(BaseModel):
    item: str
    status: str

# Model for the entire Todo, including an ID and the item details
class Todo(BaseModel):
    id: int
    item: Item

# Model for updating a todo (without the ID)
class TodoItem(BaseModel):
    item: str
    status: str

    class Config:
        json_schema_extra = {
            "example": {
                "item": "Updated task",
                "status": "Updated status"
            }
        }
