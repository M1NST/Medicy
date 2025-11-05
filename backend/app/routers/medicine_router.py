from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.models.medicine import Medicine

router = APIRouter()

@router.get("/", response_model=List[dict])
def get_medicines(db: Session = Depends(get_db)):
    meds = db.query(Medicine).all()
    return [{"med_id": m.med_id, "med_name": m.med_name, "description": m.description} for m in meds]

@router.post("/")
def create_medicine(med: dict, db: Session = Depends(get_db)):
    new_med = Medicine(med_name=med["med_name"], description=med.get("description"))
    db.add(new_med)
    db.commit()
    db.refresh(new_med)
    return new_med

# Ensure router is exported
__all__ = ['router']
