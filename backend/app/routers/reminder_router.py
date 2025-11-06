from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.reminder import Reminder
from app.schemas.reminder_schema import ReminderCreate, ReminderOut

router = APIRouter()

@router.get("/", response_model=list[ReminderOut])
def get_reminders(db: Session = Depends(get_db)):
    return db.query(Reminder).all()


@router.post("/", response_model=ReminderOut)
def create_reminder(rem: ReminderCreate, db: Session = Depends(get_db)):
    new_rem = Reminder(**rem.dict())
    db.add(new_rem)
    db.commit()
    db.refresh(new_rem)
    return new_rem

__all__ = ['router']