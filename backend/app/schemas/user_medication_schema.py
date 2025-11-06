from pydantic import BaseModel
from datetime import datetime, date  # <-- 1. เพิ่ม date
from typing import Optional


class UserMedicationCreate(BaseModel):
    user_id: int
    med_id: int
    dosage: str
    schedule: Optional[str] = None      # <-- 3. เพิ่ม schedule
    start_date: Optional[date] = None   # <-- 2. เปลี่ยนเป็น date
    end_date: Optional[date] = None     # <-- 2. เปลี่ยนเป็น date


class UserMedicationOut(BaseModel):
    usermed_id: int
    user_id: int
    med_id: int
    dosage: str
    schedule: Optional[str]               # <-- 3. เพิ่ม schedule
    start_date: Optional[date]            # <-- 2. เปลี่ยนเป็น date
    end_date: Optional[date]              # <-- 2. เปลี่ยนเป็น date
    created_at: datetime

    class Config:
        from_attributes = True