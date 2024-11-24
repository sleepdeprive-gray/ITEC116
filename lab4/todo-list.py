from fastapi import FastAPI, APIRouter, HTTPException, status, Depends, Header
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

application = FastAPI()

def api_key_check(authorization: str = Header(None)):
    if authorization is None:      
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API Key."
        )

task_db: List[dict] = [
    {"task_id": 1, "task_title": "Laboratory Activity 1", "task_desc": "Create Lab Act 1", "is_finished": False}
]

class Task(BaseModel):
    task_id: int
    task_title: str
    task_desc: str
    is_finished: bool

apiv1_router = APIRouter()

@apiv1_router.get("/tasks/{task_id}")
def read_task_v1(task_id: float):
    if not task_id.is_integer():
        return {"error": "Whole number only. Task ID must be a whole number."}
    task_id = int(task_id)
    if task_id <= 0:
        return {"error": "Invalid task number input. Counting starts at '1'."}
    for task in task_db:
        if task["task_id"] == task_id:
            return {"status": "ok", "result": task}
    return {"error": f"Task {task_id} not found"}

@apiv1_router.post("/tasks")
def create_task_v1(new_task: Task):
    if any(task['task_id'] == new_task.task_id for task in task_db):
        return {"error": "Task already existing"}
    if new_task.task_id <= 0:
        return {"error": "Invalid task number input. Counting starts at '1'."}
    if not new_task.task_title or not new_task.task_desc:
        return {"error": "Task title and description cannot be empty."}
    task_db.append(new_task.dict())
    return {"status": "ok"}

@apiv1_router.put("/tasks/{task_id}")
def update_task_v1(task_id: float, task: Task):
    if not task_id.is_integer():
        return {"error": "Whole number only. Task ID must be a whole number."}
    task_id = int(task_id)
    if task_id <= 0:
        return {"error": "Invalid task number input. Counting starts at '1'."}
    for index, iteration in enumerate(task_db):
        if iteration["task_id"] == task_id:
            if not task.task_title or not task.task_desc:
                return {"error": "Task title and description cannot be empty."}
            if (task_db[index]['task_title'] == task.task_title and
                task_db[index]['task_desc'] == task.task_desc and
                task_db[index]['is_finished'] == task.is_finished):
                return {"error": "No changes detected. The provided values are the same as the current ones."}
            if task.is_finished not in [True, False]:
                return {"error": "Invalid task status. Only accepts 'true' or 'false'."}
            task_db[index]['task_title'] = task.task_title
            task_db[index]['task_desc'] = task.task_desc
            task_db[index]['is_finished'] = task.is_finished
            return {"status": "ok", "updated_task": task_db[index]}
    return {"error": f"Task {task_id} not found. Cannot update task record"}

@apiv1_router.delete("/tasks/{task_id}")
def delete_task_v1(task_id: float):
    if not task_id.is_integer():
        return {"error": "Whole number only. Task ID must be a whole number."}
    task_id = int(task_id)
    if task_id <= 0:
        return {"error": "Invalid task number input. Counting starts at '1'."}
    for index, task in enumerate(task_db):
        if task["task_id"] == task_id:
            deleted_task = task_db.pop(index)
            return {"status": "ok", "deleted_task": deleted_task}
    return {"error": f"Task {task_id} not found. Cannot delete task record"}

apiv2_router = APIRouter(dependencies=[Depends(api_key_check)])

@apiv2_router.get("/tasks/{task_id}")
def read_task_v2(task_id: float):
    if not task_id.is_integer():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Whole number only. Task ID must be a whole number.")
    task_id = int(task_id)
    if task_id <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid task number input. Counting starts at '1'.")
    for task in task_db:
        if task["task_id"] == task_id:
            return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {task_id} not found.")

@apiv2_router.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task_v2(new_task: Task):
    if any(task['task_id'] == new_task.task_id for task in task_db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Task already existing.")
    if new_task.task_id <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid task number input. Counting starts at '1'.")
    if not new_task.task_title or not new_task.task_desc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Task title and description cannot be empty.")
    task_db.append(new_task.dict())
    return {"status": "Task created successfully."}

@apiv2_router.put("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_task_v2(task_id: float, task: Task):
    if not task_id.is_integer():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Whole number only. Task ID must be a whole number.")
    task_id = int(task_id)
    if task_id <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid task number input. Counting starts at '1'.")
    
    for index, iteration in enumerate(task_db):
        if iteration["task_id"] == task_id:
            # Validate if task title and description are not empty
            if not task.task_title or not task.task_desc:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Task title and description cannot be empty.")
            
            # Check if there are changes; if not, return error
            if (task_db[index]['task_title'] == task.task_title and
                task_db[index]['task_desc'] == task.task_desc and
                task_db[index]['is_finished'] == task.is_finished):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No changes detected.")

            # Validate the status value is either True or False
            if task.is_finished not in [True, False]:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid task status.")

            task_db[index]['task_title'] = task.task_title
            task_db[index]['task_desc'] = task.task_desc
            task_db[index]['is_finished'] = task.is_finished

            return {"status": "ok", "updated_task": task_db[index]}
    
    # If the task with the given task_id does not exist, return a 404
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {task_id} not found.")


@apiv2_router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task_v2(task_id: float):
    if not task_id.is_integer():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Whole number only. Task ID must be a whole number.")
    task_id = int(task_id)
    if task_id <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid task number input. Counting starts at '1'.")
    for index, task in enumerate(task_db):
        if task["task_id"] == task_id:
            deleted_task = task_db.pop(index)
            return {"status": "ok", "deleted_task": deleted_task}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task {task_id} not found.")

application.include_router(apiv1_router, prefix="/apiv1", tags=["apiv1"])
application.include_router(apiv2_router, prefix="/apiv2", tags=["apiv2"])