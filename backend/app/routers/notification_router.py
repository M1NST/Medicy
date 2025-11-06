from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.notification import Notification
from app.schemas.notification_schema import NotificationCreate, NotificationOut

router = APIRouter()

@router.get("/", response_model=list[NotificationOut])
def get_notifications(db: Session = Depends(get_db)):
    return db.query(Notification).all()

@router.post("/", response_model=NotificationOut)
def create_notification(noti: NotificationCreate, db: Session = Depends(get_db)):
    new_noti = Notification(**noti.dict())
    db.add(new_noti)
    db.commit()
    db.refresh(new_noti)
    return new_noti


__all__ = ['router']