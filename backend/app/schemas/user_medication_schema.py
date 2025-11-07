from pydantic import BaseModel, field_validator
from datetime import date, datetime
from typing import Optional

class UserMedicationBase(BaseModel):
    med_name: str
    dosage: str
    startDate: date
    endDate: date
    user_id: Optional[int] = 4
    when: Optional[str] = None
    details: Optional[str] = None

    @field_validator("startDate", "endDate", mode='before')
    def parse_date(cls, value):
        if isinstance(value, str):
            try:
                return datetime.strptime(value, "%d/%m/%Y").date()
            except ValueError:
                raise ValueError("Date must be in format DD/MM/YYYY")
        return value

# ✅ สำหรับการสร้างข้อมูลใหม่ (POST)
class UserMedicationCreate(UserMedicationBase):
    pass


# ✅ สำหรับการแสดงผล (response)
class UserMedicationOut(UserMedicationBase):
    usermed_id: int

    class Config:
        orm_mode = True
