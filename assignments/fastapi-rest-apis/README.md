# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI by defining routes, using Pydantic models for request and response data, and handling common API behaviors such as validation, status codes, and not-found errors.

## 📝 Tasks

### 🛠️ Create the API Foundation

#### Description
Set up a FastAPI application with a root endpoint and a simple in-memory data store for a task tracker API.

#### Requirements
Completed program should:

- Create a FastAPI app instance.
- Add a `GET /` endpoint that returns a short welcome message.
- Add a `GET /tasks` endpoint that returns the current list of tasks.
- Keep task data in memory so the API works without a database.

### 🛠️ Implement Task CRUD Operations

#### Description
Create endpoints that let users add, view, update, and delete tasks in the API.

#### Requirements
Completed program should:

- Add a `POST /tasks` endpoint that creates a new task.
- Add a `GET /tasks/{task_id}` endpoint that returns one task by ID.
- Add a `PUT /tasks/{task_id}` endpoint that updates an existing task.
- Add a `DELETE /tasks/{task_id}` endpoint that removes a task.
- Return JSON responses for each endpoint.

### 🛠️ Add Validation and Error Handling

#### Description
Use FastAPI and Pydantic features to make the API safer and easier to use.

#### Requirements
Completed program should:

- Define a Pydantic model for task data.
- Require valid task titles and reject invalid input.
- Return a `404 Not Found` response when a task ID does not exist.
- Use appropriate HTTP status codes for creating, updating, and deleting tasks.
- Include at least one example of filtering tasks with a query parameter, such as showing only completed tasks.
