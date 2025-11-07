from pydantic import BaseModel
from datetime import date, time

class UserMedicationBase(BaseModel):
    user_id: int
    med_name: str
    dosage: str
    when_to_take: str
    start_date: date
    end_date: date
    time_of_day: time

class UserMedicationCreate(UserMedicationBase):
    pass

class UserMedicationOut(UserMedicationBase):
    usermed_id: int
    class Config:
        from_attributes = True
