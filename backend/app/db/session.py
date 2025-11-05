from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 💾 เชื่อมต่อ MySQL (ปรับ user, password, host, db ให้ตรงของคุณ)
DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/medicy_db"

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
