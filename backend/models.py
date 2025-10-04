from sqlalchemy import Column, Integer, String, DateTime, Enum, Boolean, ForeignKey, TEXT, DECIMAL, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base
import enum

class UserRole(str, enum.Enum):
    organizer = "organizer"
    vendor = "vendor"
    attendee = "attendee"
    sponsor = "sponsor"

class TaskStatus(str, enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

class EventStatus(str, enum.Enum):
    upcoming = "upcoming"
    active = "active"
    completed = "completed"


class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    location = Column(String(255))
    status = Column(Enum(EventStatus), default=EventStatus.upcoming)
    created_at = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")

    users = relationship("User", back_populates="event")
    tasks = relationship("Task", back_populates="event")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    company_name = Column(String(255))

    event = relationship("Event", back_populates="users")
    tasks = relationship("Task", back_populates="assigned_to")

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    assigned_to_user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(255), nullable=False)
    status = Column(Enum(TaskStatus), default=TaskStatus.pending)
    is_critical = Column(Boolean, default=False)
    due_date = Column(DateTime)

    event = relationship("Event", back_populates="tasks")
    assigned_to = relationship("User", back_populates="tasks")

class EventLog(Base):
    __tablename__ = "event_logs"
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    action = Column(TEXT, nullable=False)
    user_role = Column(String(50))
    timestamp = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")

class LayoutItem(Base):
    __tablename__ = "layout_items"
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    vendor_user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(255), nullable=False)
    type = Column(String(50), nullable=False)
    x_pos = Column(Integer, nullable=False)
    y_pos = Column(Integer, nullable=False)
    width = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    color = Column(String(7))

class Sponsor(Base):
    __tablename__ = "sponsors"
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    tier = Column(String(50), nullable=False)

class Lead(Base):
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True, index=True)
    sponsor_id = Column(Integer, ForeignKey("sponsors.id"), nullable=False)
    attendee_user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    scanned_at = Column(DateTime, nullable=False)
    notes = Column(TEXT)

class Interest(Base):
    __tablename__ = "interests"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)

class UserInterest(Base):
    __tablename__ = "user_interests"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    interest_id = Column(Integer, ForeignKey("interests.id"), primary_key=True)
