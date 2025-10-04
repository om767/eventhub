from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, schemas, models
from ..database import get_db

router = APIRouter()

# Assume a single event for the hackathon
HACKATHON_EVENT_ID = 1

@router.get("/chat/{channel}", response_model=List[schemas.Message])
def get_messages(channel: str, db: Session = Depends(get_db)):
    return crud.get_chat_messages(db, event_id=HACKATHON_EVENT_ID, channel=channel)

@router.post("/chat/{channel}", response_model=schemas.Message)
def post_message(channel: str, message: schemas.MessageBase, db: Session = Depends(get_db)):
    # In a real app, user_id would come from the auth token
    MOCK_USER_ID = 1 
    
    message_create = schemas.MessageCreate(
        message=message.message,
        channel=channel,
        event_id=HACKATHON_EVENT_ID
    )
    return crud.create_chat_message(db, message=message_create, user_id=MOCK_USER_ID)
