from typing import List

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


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Task 1",
                        "status": "Pending"
                    },
                    {
                        "item": "Task 2",
                        "status": "Completed"
                    }
                ]
            }
        }
