from sqlalchemy import Column, Integer, String, Text
from app.db.session import Base

class Medicine(Base):
    __tablename__ = "medicine"

    med_id = Column(Integer, primary_key=True, autoincrement=True)
    med_name = Column(String(100), nullable=False)
    description = Column(Text)
