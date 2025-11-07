from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.session import Base

class Reminder(Base):
    __tablename__ = "reminder"
    rem_id = Column(Integer, primary_key=True, index=True)
    reminder_time = Column(DateTime, nullable=False)
    create_time = Column(DateTime, default=datetime.utcnow)

    status_code = Column(Integer, ForeignKey("status.status_code"))
    status_details = relationship("Status", back_populates="reminders")

    user_med_id = Column(Integer, ForeignKey("user_medications.id"))  # ✅ แก้ไขตรงนี้
    user_med = relationship("UserMedication", back_populates="reminders")

    reminder_logs = relationship("ReminderLog", back_populates="reminder")


class ReminderLog(Base):
    __tablename__ = "reminder_logs"
    log_id = Column(Integer, primary_key=True, index=True)
    rem_id = Column(Integer, ForeignKey("reminder.rem_id"))
    usermed_id = Column(Integer, ForeignKey("user_medications.id"))  # ✅ แก้ไขตรงนี้
    responded_at = Column(DateTime)

    reminder = relationship("Reminder", back_populates="reminder_logs")
    user_medication = relationship("UserMedication", back_populates="reminder_logs")
