from typing import Optional
from pydantic import BaseModel

class UserMedicationBase(BaseModel):
    user_id: int
    dosage: Optional[str] = None
    schedule: Optional[str] = None
    start_date: Optional[str] = None  # dd-MM-YYYY or ISO string per your API
    end_date: Optional[str] = None
    med_name: Optional[str] = None    # store plain name instead of FK

class UserMedicationCreate(UserMedicationBase):
    pass

class UserMedicationOut(UserMedicationBase):
    usermed_id: int

    class Config:
        orm_mode = True
