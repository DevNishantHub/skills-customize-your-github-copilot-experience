# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, fast REST APIs using the FastAPI framework. You'll create a simple API with multiple endpoints, handle data validation, and understand HTTP methods and status codes.

## 📝 Tasks

### 🛠️	Create a Basic FastAPI Application

#### Description
Set up a FastAPI application with a basic structure including a root endpoint and a health check endpoint.

#### Requirements
Completed program should:

- Install and import FastAPI and Uvicorn
- Create a FastAPI instance
- Define a root endpoint (/) that returns a welcome message
- Define a health check endpoint (/health) that returns the API status
- Run the server using Uvicorn


### 🛠️	Build a Task Management API

#### Description
Create a simple task management API with CRUD (Create, Read, Update, Delete) operations for managing tasks.

#### Requirements
Completed program should:

- Define a Task model using Pydantic with fields: id, title, description, and completed status
- Implement POST /tasks endpoint to create new tasks
- Implement GET /tasks endpoint to retrieve all tasks
- Implement GET /tasks/{task_id} endpoint to retrieve a specific task
- Implement PUT /tasks/{task_id} endpoint to update a task
- Implement DELETE /tasks/{task_id} endpoint to delete a task
- Use proper HTTP status codes (200, 201, 404, etc.)
- Include data validation using Pydantic models
- Store tasks in memory (a list or dictionary)
