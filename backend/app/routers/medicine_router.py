from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List
from app.db.session import get_db
from app.models.medicine import Medicine
from app.schemas.medicine_schema import MedicineCreate, MedicineOut

router = APIRouter()

@router.get("/", response_model=List[MedicineOut])
def get_medicines(db: Session = Depends(get_db)):
    return db.query(Medicine).all()

@router.post("/", response_model=MedicineOut)
def create_medicine(med: MedicineCreate, db: Session = Depends(get_db)):
    new_med = Medicine(**med.dict())
    db.add(new_med)
    try:
        db.commit()
        db.refresh(new_med)
        return new_med
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Medicine already exists")
    except Exception:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error creating medicine")


_all__ = ['router']