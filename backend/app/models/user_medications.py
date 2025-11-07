from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class UserMedication(Base):
    __tablename__ = "user_medications"

    usermed_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey("user.user_id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)

    # Removed: med_id FK to medicine
    # Added: med_name stored directly
    med_name = Column(String(100), nullable=True)

    dosage = Column(String(50), nullable=True)
    schedule = Column(String(50), nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)

    # Keep relationships minimal to avoid coupling with repo variants
    user = relationship("User", lazy="joined", foreign_keys=[user_id])
    # Removed: relationship('Medicine', ...)
    # Optional: logs relation if your project defines ReminderLog and backrefs
    try:
        logs = relationship("ReminderLog", cascade="all, delete-orphan")
    except Exception:
        pass
