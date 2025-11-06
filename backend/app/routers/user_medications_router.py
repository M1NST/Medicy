from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user_medication_schema import UserMedicationCreate, UserMedicationOut

router = APIRouter()

# 🔹 GET ทั้งหมด
@router.get("/", response_model=list[UserMedicationOut])
def get_user_medications(db: Session = Depends(get_db)):
    from app.models.user_medications import UserMedication
    return db.query(UserMedication).all()

# 🔹 GET ตาม user_id
@router.get("/user/{user_id}", response_model=list[UserMedicationOut])
def get_medications_by_user(user_id: int, db: Session = Depends(get_db)):
    from app.models.user_medications import UserMedication
    return db.query(UserMedication).filter(UserMedication.user_id == user_id).all()

# 🔹 POST (เพิ่มยาให้ผู้ใช้)
@router.post("/", response_model=UserMedicationOut)
def create_user_medication(data: UserMedicationCreate, db: Session = Depends(get_db)):
    from app.models.user_medications import UserMedication
    new_record = UserMedication(**data.dict())
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

__all__ = ['router']