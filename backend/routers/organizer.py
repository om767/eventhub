from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, schemas, models
from ..database import get_db

router = APIRouter()

# For simplicity, we'll assume a single event (event_id=1) for this hackathon.
# In a real app, you'd get this from the logged-in user's context.
HACKATHON_EVENT_ID = 1

@router.get("/tasks/", response_model=List[schemas.Task])
def read_tasks(db: Session = Depends(get_db)):
    tasks = crud.get_tasks_by_event(db, event_id=HACKATHON_EVENT_ID)
    return tasks

@router.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    # Force the event_id for this hackathon
    task.event_id = HACKATHON_EVENT_ID
    return crud.create_task(db=db, task=task)
    
@router.put("/tasks/{task_id}/status", response_model=schemas.Task)
def update_task_status(task_id: int, status_update: schemas.TaskUpdate, db: Session = Depends(get_db)):
    updated_task = crud.update_task_status(db=db, task_id=task_id, status=status_update.status)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    # Log this action
    crud.create_event_log(db, event_id=HACKATHON_EVENT_ID, action=f"Task '{updated_task.name}' status changed to {status_update.status.value}", user_role="organizer")
    return updated_task

@router.delete("/tasks/{task_id}", response_model=schemas.Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted_task = crud.delete_task(db=db, task_id=task_id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted_task

@router.get("/logs/", response_model=List[schemas.EventLog])
def read_event_logs(db: Session = Depends(get_db)):
    return crud.get_event_logs(db, event_id=HACKATHON_EVENT_ID)
