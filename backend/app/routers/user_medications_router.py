from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.models.user_medications import UserMedication
from app.schemas.user_medication_schema import UserMedicationCreate, UserMedicationOut

router = APIRouter()

@router.get("/", response_model=List[UserMedicationOut])
def get_user_meds(user_id: int | None = None, db: Session = Depends(get_db)):
    q = db.query(UserMedication)
    if user_id:
        q = q.filter(UserMedication.user_id == user_id)
    return q.all()

@router.post("/", response_model=UserMedicationOut)
def create_user_med(med: UserMedicationCreate, db: Session = Depends(get_db)):
    new_item = UserMedication(**med.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@router.delete("/{usermed_id}")
def delete_user_med(usermed_id: int, db: Session = Depends(get_db)):
    med = db.query(UserMedication).get(usermed_id)
    if not med:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(med)
    db.commit()
    return {"deleted": True}
