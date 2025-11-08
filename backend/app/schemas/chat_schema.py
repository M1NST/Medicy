from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ChatCreate(BaseModel):
    sender_id: int
    receiver_id: int
    message: str


class ChatOut(BaseModel):
    chat_id: int
    sender_id: int
    receiver_id: int
    message: str
    sent_at: Optional[datetime] = None  # <-- 1. เปลี่ยนชื่อจาก created_at

    class Config:
        from_attributes = True