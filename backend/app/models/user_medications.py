from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.session import Base

class UserMedication(Base):
    __tablename__ = "user_medications"

    usermed_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.user_id"), nullable=False)
    med_id = Column(Integer, ForeignKey("medicine.med_id"), nullable=False)
    dosage = Column(String(50))
    schedule = Column(String(50))
    start_date = Column(Date)
    end_date = Column(Date)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="user_meds")
    medicine = relationship("Medicine", back_populates="user_meds")
    
    # vvvvv (ลบบรรทัดนี้ทิ้ง เพราะไม่ตรงกับ SQL) vvvvv
    # reminders = relationship("Reminder", back_populates="user_medication")
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
    # (ความสัมพันธ์นี้ถูกต้องตาม SQL)
    reminder_logs = relationship("ReminderLog", back_populates="user_medication")