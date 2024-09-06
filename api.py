from fastapi import FastAPI
from todo_routes import todo_router  # Import the router from todo_routes.py

# Create the FastAPI app
app = FastAPI()

# Root endpoint
@app.get("/")
async def welcome() -> dict:
    return {"message": "Welcome to the Todos API"}

# Include the router for the todo endpoints
app.include_router(todo_router)

if __name__ == "__main__":
    import uvicorn
    # Run the app with uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080, reload=True)
