from fastapi import APIRouter, Path, Body, HTTPException, status
from model import Todo, TodoItem, TodoItems
from typing import List

# Create a router for todo-related operations
todo_router = APIRouter(prefix="/todo")

# In-memory list to store todos
todo_list = []


@todo_router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def add_todo(todo: Todo) -> dict:
    # Ensure no duplicates by checking the ID
    for existing_todo in todo_list:
        if existing_todo.id == todo.id:
            return {"message": f"Todo with ID {todo.id} already exists"}

    # Append the new todo
    todo_list.append(todo.model_copy())  # Ensure a copy of the todo is added
    return {"message": "Todo added successfully"}


# GET method to retrieve all todos
@todo_router.get("/", response_model=TodoItems)
async def get_all_todos() -> TodoItems:
    return TodoItems(todos=[TodoItem(**todo.item.dict()) for todo in todo_list])


# GET method to retrieve a single todo by ID
@todo_router.get("/{todo_id}", response_model=dict)
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to get")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Todo with ID {todo_id} not found"
    )


# PUT method to update a todo by ID
@todo_router.put("/{todo_id}", response_model=dict)
async def update_todo(
        todo_data: TodoItem = Body(...),  # The body parameter for updating a todo
        todo_id: int = Path(..., title="The ID of the todo to update")  # Path parameter for the ID
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item.item = todo_data.item  # Update the task description
            todo.item.status = todo_data.status  # Update the status
            return {"message": "Todo updated successfully"}
    raise HTTPException (
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Todo with ID {todo_id} not found"
    )


@todo_router.delete("/{todo_id}", response_model=dict)
async def delete_single_todo(todo_id: int = Path(..., title="The ID of the todo to delete")) -> dict:
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list.pop(index)  # Remove the todo by index
            return {"message": "Todo deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Todo with ID {todo_id} not found"
    )
