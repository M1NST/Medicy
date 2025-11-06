import os  # <--- 1. เพิ่ม import นี้
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 💾 อ่าน DATABASE_URL จาก Environment Variable (ที่ส่งมาจาก Docker)
# ถ้าไม่เจอ (เช่น รัน local) ให้ใช้ค่า "localhost" เป็นค่าเริ่มต้น
DATABASE_URL = os.environ.get(
    "DATABASE_URL", 
    "mysql+pymysql://root:root@localhost:3306/medicy_db"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency สำหรับ FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()