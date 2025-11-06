from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ReminderCreate(BaseModel):
    reminder_time: datetime
    status_code: Optional[int] = None


class ReminderOut(BaseModel):
    rem_id: int
    reminder_time: datetime
    status_code: Optional[int] = None
    create_time: Optional[datetime]

    class Config:
        from_attributes = True
