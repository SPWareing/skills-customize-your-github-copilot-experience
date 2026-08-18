from typing import Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


app = FastAPI(title="Task Tracker API")


class Task(BaseModel):
    id: int
    title: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=300)
    completed: bool = False


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=300)


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=300)
    completed: Optional[bool] = None


tasks = [
    Task(id=1, title="Review FastAPI basics", description="Read the lesson notes", completed=False),
    Task(id=2, title="Build a sample endpoint", description="Try creating a GET route", completed=True),
]


def find_task_index(task_id: int) -> int:
    for index, task in enumerate(tasks):
        if task.id == task_id:
            return index
    return -1


@app.get("/")
def root():
    return {"message": "Task Tracker API is running"}


@app.get("/tasks")
def list_tasks(completed: Optional[bool] = None):
    if completed is None:
        return tasks
    return [task for task in tasks if task.completed == completed]


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: Look up the task by ID and return it.
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    # TODO: Create a new task with the next available ID and append it to tasks.
    return task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    # TODO: Update the matching task and return the updated task.
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    # TODO: Remove the matching task from the list.
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")