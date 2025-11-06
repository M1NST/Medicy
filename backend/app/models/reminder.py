from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.session import Base

class Reminder(Base):
    __tablename__ = "reminder"

    rem_id = Column(Integer, primary_key=True, autoincrement=True)
    # 1. ลบ usermed_id จากตรงนี้
    reminder_time = Column(DateTime, nullable=False)
    # 2. ลบ status ที่เป็น String ออก
    create_time = Column(DateTime, default=datetime.utcnow)

    logs = relationship("ReminderLog", back_populates="reminder")
    
    # 3. เปลี่ยนชื่อ status_id เป็น status_code
    status_code = Column(Integer, ForeignKey("status.status_code"))
    status_details = relationship("Status", back_populates="reminders")
    # 1. ลบ user_medication relationship จากตรงนี้

class ReminderLog(Base):
    __tablename__ = "reminder_logs"

    log_id = Column(Integer, primary_key=True, autoincrement=True)
    rem_id = Column(Integer, ForeignKey("reminder.rem_id"))
    responded_at = Column(DateTime)
    reminder = relationship("Reminder", back_populates="logs")

    # vvvvv 4. เพิ่มฟิลด์และ Relationship ตาม SQL ใหม่ vvvvv
    usermed_id = Column(Integer, ForeignKey("user_medications.usermed_id"), nullable=False)
    user_medication = relationship("UserMedication", back_populates="reminder_logs")