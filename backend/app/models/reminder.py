from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from app.db.session import Base
from datetime import datetime

class Reminder(Base):
    __tablename__ = "reminder"

    rem_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    med_id = Column(Integer, ForeignKey("medicine.med_id"))
    reminder_time = Column(DateTime, nullable=False)
    status = Column(String(20), default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
