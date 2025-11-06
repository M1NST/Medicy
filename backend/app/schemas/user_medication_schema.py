from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserMedicationCreate(BaseModel):
    user_id: int
    med_id: int
    dosage: str
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None


class UserMedicationOut(BaseModel):
    usermed_id: int
    user_id: int
    med_id: int
    dosage: str
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    created_at: datetime

    class Config:
        from_attributes = True
