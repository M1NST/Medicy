from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date  # <-- 1. เพิ่ม Date
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.session import Base

class UserMedication(Base):
    __tablename__ = "user_medications"

    usermed_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.user_id"), nullable=False)
    med_id = Column(Integer, ForeignKey("medicine.med_id"), nullable=False)
    dosage = Column(String(50))
    schedule = Column(String(50))  # <-- 2. เพิ่ม schedule
    start_date = Column(Date)      # <-- 1. เปลี่ยนเป็น Date
    end_date = Column(Date)        # <-- 1. เปลี่ยนเป็น Date
    created_at = Column(DateTime, default=datetime.utcnow) # (ฟิลด์นี้มีในโค้ดแต่ไม่มีใน SQL แต่เก็บไว้ได้ครับ)

    user = relationship("User", back_populates="user_meds")
    medicine = relationship("Medicine", back_populates="user_meds")
    reminders = relationship("Reminder", back_populates="user_medication")
    
    # vvvvv 3. เพิ่ม Relationship นี้ vvvvv
    reminder_logs = relationship("ReminderLog", back_populates="user_medication")