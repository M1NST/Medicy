from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.session import Base

class Reminder(Base):
    __tablename__ = "reminder"

    rem_id = Column(Integer, primary_key=True, autoincrement=True)
    usermed_id = Column(Integer, ForeignKey("user_medications.usermed_id"))
    reminder_time = Column(DateTime, nullable=False)
    status = Column(String(50), default="Pending")
    create_time = Column(DateTime, default=datetime.utcnow)

    logs = relationship("ReminderLog", back_populates="reminder")
    status_id = Column(Integer, ForeignKey("status.status_code"))
    status_details = relationship("Status", back_populates="reminders_from_reminder")
    user_medication = relationship("UserMedication", back_populates="reminders")

class ReminderLog(Base):
    __tablename__ = "reminder_logs"

    log_id = Column(Integer, primary_key=True, autoincrement=True)
    rem_id = Column(Integer, ForeignKey("reminder.rem_id"))
    responded_at = Column(DateTime)
    reminder = relationship("Reminder", back_populates="logs")
    
