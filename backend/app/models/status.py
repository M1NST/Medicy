from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.session import Base

class Status(Base):
    __tablename__ = "status"

    status_code = Column(Integer, primary_key=True, autoincrement=True)
    status_name = Column(String(50), nullable=False)

    reminders = relationship("Reminder", back_populates="status")
