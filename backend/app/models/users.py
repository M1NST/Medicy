from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.db.session import Base

class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    role_code = Column(Integer, ForeignKey("role.role_code"), default=1)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(100))
    phone_num = Column(String(10))
    username = Column(String(50))
    password_hash = Column(String(255))

    role = relationship("Role", back_populates="users")
    notifications = relationship("Notification", back_populates="user")
    chats_sent = relationship("Chat", foreign_keys="[Chat.sender_id]", back_populates="sender")
    chats_received = relationship("Chat", foreign_keys="[Chat.receiver_id]", back_populates="receiver")
    user_meds = relationship("UserMedications", back_populates="user")
