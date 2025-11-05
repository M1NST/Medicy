from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Reminder(Base):
    __tablename__ = "reminder"

    rem_id = Column(Integer, primary_key=True, autoincrement=True)
    reminder_time = Column(DateTime, nullable=False)
    create_time = Column(DateTime)
    status_code = Column(Integer, ForeignKey("status.status_code"))

    # ใช้ชื่อ class แบบ string เพื่อหลีกเลี่ยง circular import
    status = relationship("Status", back_populates="reminders")
    logs = relationship("ReminderLog", back_populates="reminder")


class ReminderLog(Base):
    __tablename__ = "reminder_logs"

    log_id = Column(Integer, primary_key=True, autoincrement=True)
    rem_id = Column(Integer, ForeignKey("reminder.rem_id"))
    usermed_id = Column(Integer, ForeignKey("user_medications.usermed_id"))
    responded_at = Column(DateTime)

    reminder = relationship("Reminder", back_populates="logs")
    user_medication = relationship("UserMedications", back_populates="reminder_logs")
