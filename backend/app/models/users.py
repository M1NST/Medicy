from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base
from datetime import datetime

class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), unique=True, nullable=False)
    role_code = Column(Integer, ForeignKey("role.role_code"), default=1)
    phone_num = Column(String(10))
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(100))
    password_hash = Column(String(255))

    role = relationship("Role", back_populates="users")
    notifications = relationship("Notification", back_populates="user")  # ✅ แก้ตรงนี้
    chats_sent = relationship("Chat", foreign_keys="[Chat.sender_id]", back_populates="sender")
    chats_received = relationship("Chat", foreign_keys="[Chat.receiver_id]", back_populates="receiver")
    user_meds = relationship("UserMedication", back_populates="user")
