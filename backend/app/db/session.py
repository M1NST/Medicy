from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# สร้าง engine สำหรับเชื่อมต่อ MySQL
engine = create_engine(DATABASE_URL, echo=True)

# Session ใช้สำหรับ query และ commit ข้อมูล
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base สำหรับ model ทุกตัว
Base = declarative_base()
