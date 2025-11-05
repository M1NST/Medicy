from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class UserMedications(Base):
    __tablename__ = "user_medications"

    usermed_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    med_id = Column(Integer, ForeignKey("medicine.med_id"))
    dosage = Column(String(100))
    schedule = Column(String(100))
    start_date = Column(Date)
    end_date = Column(Date)

    user = relationship("User", back_populates="user_meds")
    medicine = relationship("Medicine", back_populates="user_meds")
    reminder_logs = relationship("ReminderLog", back_populates="user_medication")
