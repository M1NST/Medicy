from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Notification(Base):
    __tablename__ = "notification"

    noti_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    title = Column(String(100))
    message = Column(Text)
    created_at = Column(DateTime)
    read_status = Column(Boolean, default=False)

    user = relationship("User", back_populates="notifications")
