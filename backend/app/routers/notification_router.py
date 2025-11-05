from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.notification import Notification

router = APIRouter()

@router.get("/")
def get_notifications(db: Session = Depends(get_db)):
    return db.query(Notification).all()

@router.post("/")
def create_notification(noti: dict, db: Session = Depends(get_db)):
    new_noti = Notification(**noti)
    db.add(new_noti)
    db.commit()
    db.refresh(new_noti)
    return new_noti

# Ensure router is exported
__all__ = ['router']
