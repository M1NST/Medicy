from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user_medications import UserMedications

router = APIRouter()

@router.get("/")
def get_user_meds(db: Session = Depends(get_db)):
    return db.query(UserMedications).all()

@router.post("/")
def create_user_med(user_med: dict, db: Session = Depends(get_db)):
    new_rec = UserMedications(**user_med)
    db.add(new_rec)
    db.commit()
    db.refresh(new_rec)
    return new_rec

# Ensure router is exported
__all__ = ['router']
