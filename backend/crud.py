from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# --- User CRUD ---
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        email=user.email,
        name=user.name,
        role=user.role,
        company_name=user.company_name,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# --- Task CRUD ---
def get_tasks_by_event(db: Session, event_id: int):
    return db.query(models.Task).filter(models.Task.event_id == event_id).all()

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task_status(db: Session, task_id: int, status: schemas.TaskStatus):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task:
        db_task.status = status
        db.commit()
        db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task

# --- Event Log CRUD ---
def create_event_log(db: Session, event_id: int, action: str, user_role: str):
    db_log = models.EventLog(event_id=event_id, action=action, user_role=user_role)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def get_event_logs(db: Session, event_id: int):
    return db.query(models.EventLog).filter(models.EventLog.event_id == event_id).order_by(models.EventLog.timestamp.desc()).all()


# --- Chat Message CRUD ---
def create_chat_message(db: Session, message: schemas.MessageCreate, user_id: int):
    db_message = models.ChatMessage(
        **message.model_dump(),
        user_id=user_id
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_chat_messages(db: Session, event_id: int, channel: str):
    return db.query(models.ChatMessage).filter(
        models.ChatMessage.event_id == event_id,
        models.ChatMessage.channel == channel
    ).order_by(models.ChatMessage.timestamp).all()

# Placeholder CRUD functions for other features.
# You can expand these as you build out the frontend interactions.

def get_expenses_by_event(db: Session, event_id: int):
    return db.query(models.Expense).filter(models.Expense.event_id == event_id).all()

def get_vendors_by_event(db: Session, event_id: int):
    return db.query(models.User).filter(models.User.event_id == event_id, models.User.role == 'vendor').all()
