from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class NotificationCreate(BaseModel):
    user_id: int
    title: str
    message: str


class NotificationOut(BaseModel):
    noti_id: int
    user_id: int
    title: str
    message: str
    created_at: Optional[datetime] = None
    read_status: bool = False  # <-- 1. เพิ่ม read_status

    class Config:
        from_attributes = True