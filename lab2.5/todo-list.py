# Imports
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

application = FastAPI()

class Task(BaseModel):
    task_id: int
    task_title: str
    task_desc: str
    is_finished: bool

# Task Database / Library
task_db = [
{"task_id": 1, "task_title": "Laboratory Activity 1", "task_desc": "Create Lab Act 1", "is_finished": False}
]

# GET Method
@application.get("/tasks/{task_id}") 
def read_task(task_id: float):                                               # Variable initialization.

    if not task_id.is_integer():                                              # Check if task_id is not a whole number
        return {"error": "Whole number only. Task ID must be a whole number."}

    task_id = int(task_id)  # Convert the valid float to int for further processing
    
    if task_id <= 0:                                                        # Validation for zero and negative number.
        return{"error": "Invalid task number input. Counting starts at '1'."}
    
    if task_id:                                                              # If the input is correct, it will proceed here.

        for i in task_db:

            if i["task_id"] == task_id:                                     # Return the task if there is one.
                return {"status": "ok", "result" : i}                       # Display the result.
        
        return {"error": f"Task {task_id} not found"}                                  # Exception when there's no task found.
    
    return {"status": "ok", "result" : task_db}                             # Displaying success message.

# POST Method
@application.post("/tasks")
def create_task(new_task: Task):                                            # Variable initialization.

    if any(i['task_id'] == new_task.task_id for i in task_db):              # Validation for task if it is existing.
        return {"error": f"Task {new_task} already existing"}                           # Displaying the error statemnent.
    
    if new_task.task_id <= 0:                                                       # Validation of task for zero and negative numbers.
        return{"error": "Invalid task number input. Counting starts at '1'."}       # Displaying the error statemnent.

    if not new_task.task_title or not new_task.task_desc:                   # Verification of task title and description.
        return{"error": "Task title and description cannot be empty."}      # Displaying the error statemnent.
    
    task_db.append(dict(new_task))                                          # Adding new task in the dictionary or database.
    return {"status": "ok"}                                                 # Displaying the success statemnent in adding task.

# PUT Method (Update)
@application.put("/tasks/{task_id}")
def update_task(task_id: float, task: Task):                                  # Variable initialization.

    if not task_id.is_integer():                                              # Check if task_id is not a whole number
        return {"error": "Whole number only. Task ID must be a whole number."}

    task_id = int(task_id)  # Convert the valid float to int for further processing

    if task_id:                                                             # Initialized if task_id is inputted correctly.

        for index, iteration in enumerate(task_db):

            if iteration["task_id"] == task_id:                             # Validation if the task_id inputted is or at the dictionary / database.  

                if not task.task_title or not task.task_desc:               # Check for empty fields
                    return {"error": "Task title and description cannot be empty."}

                if (task_db[index]['task_title'] == task.task_title and
                    task_db[index]['task_desc'] == task.task_desc and
                    task_db[index]['is_finished'] == task.is_finished):     # Check for no changes
                    return {"error": "No changes detected. The provided values are the same as the current ones."}

                if task.is_finished not in [True, False]:                   # Validate status input for updating task.
                    return {"error": "Invalid task status. Only accepts 'true' or 'false'."}

                task_db[index]['task_title'] = task.task_title              # Insertion point for task title.
                task_db[index]['task_desc'] = task.task_desc                # Insertion point for task description.
                task_db[index]['is_finished'] = task.is_finished            # Insertion point for status.
                
                return {"status": "ok", "updated_task": task_db[index]}     # Showing the update on the task.

    return {"error": f"Task {task_id} not found. Cannot update task record"}           # Exception if there's no task found.

# DELETE Method
@application.delete("/tasks/{task_id}")
def delete_task(task_id: float):                                              # Variable initialization.

    if not task_id.is_integer():                                              # Check if task_id is not a whole number
        return {"error": "Whole number only. Task ID must be a whole number."}

    task_id = int(task_id)  # Convert the valid float to int for further processing

    if task_id:

        for index, task in enumerate(task_db):                              # loops in the database / dictionary

            if task["task_id"] == task_id:                                  # Validation if the task is in the database / dictionary.
                deleted_task = task_db.pop(index)                           # Using .pop to delete the task using task_id.
                return {"status": "ok", "deleted_task": deleted_task}       # Showing the deleted task.

    return {"error": f"Task {task_id} not found. Cannot delete task record"}           # Exception if there's no task found.
