from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
from .models import UserRole, TaskStatus, EventStatus

# --- User Schemas ---
class UserBase(BaseModel):
    email: EmailStr
    name: str
    role: UserRole
    company_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        from_attributes = True

# --- Auth Schemas ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# --- Event Schemas ---
class EventBase(BaseModel):
    name: str
    start_date: datetime
    end_date: datetime
    location: Optional[str] = None
    status: Optional[EventStatus] = EventStatus.upcoming

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
    class Config:
        from_attributes = True

# --- Task Schemas ---
class TaskBase(BaseModel):
    name: str
    status: Optional[TaskStatus] = TaskStatus.pending
    due_date: Optional[datetime] = None
    assigned_to_user_id: Optional[int] = None
    is_critical: Optional[bool] = False
    
class TaskCreate(TaskBase):
    event_id: int

class TaskUpdate(BaseModel):
    name: Optional[str] = None
    status: Optional[TaskStatus] = None
    due_date: Optional[datetime] = None
    assigned_to_user_id: Optional[int] = None

class Task(TaskBase):
    id: int
    event_id: int
    class Config:
        from_attributes = True

# --- Chat Schemas ---
class MessageBase(BaseModel):
    message: str

class MessageCreate(MessageBase):
    channel: str
    event_id: int # Assuming one main event for the hackathon

class Message(MessageBase):
    id: int
    user_id: int
    timestamp: datetime
    class Config:
        from_attributes = True

# --- EventLog Schemas ---
class EventLogBase(BaseModel):
    event_id: int
    action: str
    user_role: Optional[str] = None

class EventLogCreate(EventLogBase):
    pass

class EventLog(EventLogBase):
    id: int
    class Config:
        from_attributes = True

# --- AI Builder Schemas ---
class AIEventInput(BaseModel):
    eventType: str
    audienceSize: int
    budget: float
    eventDate: Optional[str] = None
    location: Optional[str] = None
    duration: Optional[int] = None
    specialRequirements: Optional[str] = None
