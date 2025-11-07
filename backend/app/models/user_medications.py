from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class UserMedication(Base):
    __tablename__ = "user_medications"

    usermed_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.user_id"), nullable=False)
    med_name = Column(String(100), nullable=False)
    dosage = Column(String(50), nullable=False)
    when_to_take = Column(String(50), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    time_of_day = Column(Time, nullable=False)

    user = relationship("User", back_populates="user_meds")
