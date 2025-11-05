from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    role_code = Column(Integer, ForeignKey("role.role_code"), default=1)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100))
    email = Column(String(100), unique=True)
    phone_num = Column(String(20), unique=True)
    username = Column(String(50), unique=True)
    password_hash = Column(String(255), nullable=False)

    role = relationship("Role", back_populates="users", lazy="joined")
    chats_sent = relationship("Chat", foreign_keys="[Chat.sender_id]", back_populates="sender", lazy="dynamic")
    chats_received = relationship("Chat", foreign_keys="[Chat.receiver_id]", back_populates="receiver", lazy="dynamic")
    notifications = relationship("Notification", back_populates="user", lazy="dynamic")

class Role(Base):
    __tablename__ = "role"

    role_code = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String(50), nullable=False)

    users = relationship("User", back_populates="role")
