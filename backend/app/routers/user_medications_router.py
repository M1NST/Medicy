from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user_medications import UserMedication
from app.schemas.user_medication_schema import UserMedicationCreate, UserMedicationOut
from datetime import datetime # <-- 1. Import datetime

router = APIRouter()

# 🔹 GET ทั้งหมด (โค้ดเดิม)
@router.get("/", response_model=list[UserMedicationOut])
def get_user_medications(db: Session = Depends(get_db)):
    return db.query(UserMedication).all()

# 🔹 GET ตาม user_id (โค้ดเดิม)
@router.get("/user/{user_id}", response_model=list[UserMedicationOut])
def get_medications_by_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(UserMedication).filter(UserMedication.user_id == user_id).all()

# 🔹 POST (เพิ่มยาให้ผู้ใช้)
@router.post("/", response_model=UserMedicationOut)
def create_user_medication(data: UserMedicationCreate, db: Session = Depends(get_db)):
    
    # vvvvv 2. [แก้ไข] เพิ่มตรรกะแปลงวันที่ vvvvv
    # (เราต้องแปลง String 'dd-MM-yyyy' ให้เป็น Date object ก่อนบันทึกลง DB)
    new_record_data = data.dict()
    try:
        if new_record_data.get('start_date'):
            new_record_data['start_date'] = datetime.strptime(data.start_date, '%d-%m-%Y').date()
        if new_record_data.get('end_date'):
            new_record_data['end_date'] = datetime.strptime(data.end_date, '%d-%m-%Y').date()
    except ValueError:
        # (Validator ใน Schema ควรจะดักไว้แล้ว แต่กันเหนียว)
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Invalid date format. Please use dd-MM-yyyy"
        )
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
    new_record = UserMedication(**new_record_data) # <-- 3. ใช้ข้อมูลที่แปลงแล้ว
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

# 🔹 DELETE (โค้ดเดิมที่คุณเพิ่มไว้)
@router.delete("/{usermed_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_medication(usermed_id: int, db: Session = Depends(get_db)):
    med_to_delete = db.query(UserMedication).get(usermed_id)
    
    if not med_to_delete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"UserMedication with id {usermed_id} not found"
        )
        
    try:
        db.delete(med_to_delete)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting medication: {str(e)}"
        )
        
    return None

__all__ = ['router']