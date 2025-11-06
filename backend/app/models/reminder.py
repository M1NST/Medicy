from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.session import Base

class Reminder(Base):
    __tablename__ = "reminder"

    rem_id = Column(Integer, primary_key=True, autoincrement=True)
    # (ถูกต้อง ที่ไม่มี usermed_id ที่นี่)
    reminder_time = Column(DateTime, nullable=False)
    # (ถูกต้อง ที่ไม่มี status ที่เป็น String)
    create_time = Column(DateTime, default=datetime.utcnow)

    logs = relationship("ReminderLog", back_populates="reminder")
    
    status_code = Column(Integer, ForeignKey("status.status_code"))
    status_details = relationship("Status", back_populates="reminders")
    # (ถูกต้อง ที่ไม่มี user_medication relationship ที่นี่)

class ReminderLog(Base):
    __tablename__ = "reminder_logs"

    log_id = Column(Integer, primary_key=True, autoincrement=True)
    rem_id = Column(Integer, ForeignKey("reminder.rem_id"))
    responded_at = Column(DateTime)
    reminder = relationship("Reminder", back_populates="logs")

    # (ถูกต้อง ที่มี usermed_id ที่นี่)
    usermed_id = Column(Integer, ForeignKey("user_medications.usermed_id"), nullable=False)
    user_medication = relationship("UserMedication", back_populates="reminder_logs")