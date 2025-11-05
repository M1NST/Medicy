from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.session import Base

class Role(Base):
    __tablename__ = "role"

    role_code = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String(50), nullable=False)

    users = relationship("User", back_populates="role")
