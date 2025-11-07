from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.db.session import Base
from datetime import datetime

class UserMedication(Base):
    __tablename__ = "user_medications"

    id = Column(Integer, primary_key=True, index=True)
    med_name = Column(String(100))
    dosage = Column(String(50))
    startDate = Column(Date)
    endDate = Column(Date)
    user_id = Column(Integer, ForeignKey("user.user_id"))

    user = relationship("User", back_populates="user_meds")
    reminders = relationship("Reminder", back_populates="user_med")
    reminder_logs = relationship("ReminderLog", back_populates="user_medication")
