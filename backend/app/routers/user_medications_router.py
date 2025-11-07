from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user_medications import UserMedication
from app.schemas.user_medication_schema import UserMedicationCreate, UserMedicationOut

router = APIRouter(tags=["User Medications"])

# ✅ ดึงข้อมูลยาของผู้ใช้ตาม user_id
@router.get("/user/{user_id}", response_model=list[UserMedicationOut])
def get_user_medications(user_id: int, db: Session = Depends(get_db)):
    meds = db.query(UserMedication).filter(UserMedication.user_id == user_id).all()
    if not meds:
        raise HTTPException(status_code=404, detail="No medications found for this user")
    return meds

# ✅ ดึงทั้งหมด (สำหรับ debug หรือ admin)
@router.get("/", response_model=list[UserMedicationOut])
def get_all_user_medications(db: Session = Depends(get_db)):
    return db.query(UserMedication).all()

# ✅ เพิ่มข้อมูล user medication
@router.post("/", response_model=UserMedicationOut)
def create_user_medication(payload: UserMedicationCreate, db: Session = Depends(get_db)):
    user_id = payload.user_id if payload.user_id else 4
    new_med = UserMedication(**payload.dict())
    db.add(new_med)
    db.commit()
    db.refresh(new_med)
    return new_med
