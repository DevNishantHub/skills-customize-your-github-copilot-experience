# FastAPI Task Management API - Starter Code

from fastapi import FastAPI
from pydantic import BaseModel

# TODO: Create FastAPI instance


# TODO: Define Task model using Pydantic
# Fields: id (int), title (str), description (str), completed (bool)


# TODO: Create in-memory storage for tasks
tasks = []


# TODO: Define root endpoint
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Task Management API"}


# TODO: Define health check endpoint
# @app.get("/health")
# def health_check():
#     return {"status": "healthy"}


# TODO: Create new task endpoint
# @app.post("/tasks", status_code=201)
# def create_task(task: Task):
#     pass


# TODO: Get all tasks endpoint
# @app.get("/tasks")
# def get_tasks():
#     pass


# TODO: Get specific task endpoint
# @app.get("/tasks/{task_id}")
# def get_task(task_id: int):
#     pass


# TODO: Update task endpoint
# @app.put("/tasks/{task_id}")
# def update_task(task_id: int, updated_task: Task):
#     pass


# TODO: Delete task endpoint
# @app.delete("/tasks/{task_id}")
# def delete_task(task_id: int):
#     pass


# Run with: uvicorn starter-code:app --reload
