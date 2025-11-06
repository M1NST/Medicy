from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean # <-- 1. เพิ่ม Text, Boolean
from datetime import datetime
from sqlalchemy.orm import relationship
from app.db.session import Base

class Notification(Base):
    __tablename__ = "notification"

    noti_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    title = Column(String(100))
    message = Column(Text) # <-- 1. เปลี่ยนเป็น Text
    created_at = Column(DateTime, default=datetime.utcnow)
    read_status = Column(Boolean, default=False) # <-- 2. เพิ่ม read_status

    user = relationship("User", back_populates="notifications")