from pydantic import BaseModel, validator
from datetime import datetime, date
from typing import Optional
from .medicine_schema import MedicineOut

class UserMedicationCreate(BaseModel):
    user_id: int
    med_id: int
    dosage: str
    schedule: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None

    # vvvvv 1. ลบ allow_reuse=True ออก vvvvv
    @validator('start_date', 'end_date', pre=True)
    def check_date_format(cls, v):
        if v is None:
            return None
        try:
            # แค่ลองแปลงดู ถ้าผ่านแสดงว่า format ถูก
            datetime.strptime(v, '%d-%m-%Y') 
            return v
        except ValueError:
            raise ValueError(f"Date format for {v} must be dd-MM-yyyy")

class UserMedicationOut(BaseModel):
    usermed_id: int
    user_id: int
    med_id: int
    dosage: str
    schedule: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    created_at: datetime
    medicine: MedicineOut

    # vvvvv 2. ลบ allow_reuse=True ออก vvvvv
    @validator('start_date', 'end_date', pre=True)
    def format_date_output(cls, v):
        # (ตัวนี้จะทำงานเมื่ออ่านจาก DB)
        if isinstance(v, date):
            return v.strftime('%d-%m-%Y')
        # ถ้าค่าเป็น None หรือเป็น String อยู่แล้ว ก็ให้ผ่านไป
        return v 

    class Config:
        from_attributes = True
        json_encoders = {
            date: lambda v: v.strftime("%d-%m-%Y")
        }