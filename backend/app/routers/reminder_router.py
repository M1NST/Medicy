from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.models.reminder import Reminder

router = APIRouter()

@router.get("/", response_model=List[dict])
def get_reminders(db: Session = Depends(get_db)):
    data = db.query(Reminder).all()
    return [{"rem_id": r.rem_id, "reminder_time": r.reminder_time, "status_code": r.status_code} for r in data]

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.models.reminder import Reminder

router = APIRouter()

@router.get("/", response_model=List[dict])
def get_reminders(db: Session = Depends(get_db)):
    data = db.query(Reminder).all()
    return [{"rem_id": r.rem_id, "reminder_time": r.reminder_time, "status_code": r.status_code} for r in data]

@router.post("/")
def create_reminder(rem: dict, db: Session = Depends(get_db)):
    new_rem = Reminder(reminder_time=rem["reminder_time"], status_code=rem.get("status_code"))
    db.add(new_rem)
    db.commit()
    db.refresh(new_rem)
    return new_rem