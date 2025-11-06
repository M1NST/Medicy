from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.session import Base

class UserMedication(Base):
    __tablename__ = "user_medications"

    usermed_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.user_id"), nullable=False)
    med_id = Column(Integer, ForeignKey("medicine.med_id"), nullable=False)
    dosage = Column(String(50))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="user_meds")
    medicine = relationship("Medicine", back_populates="user_meds")
    reminders = relationship("Reminder", back_populates="user_medication")
