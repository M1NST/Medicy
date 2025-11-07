from sqlalchemy import create_engine, text, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os, time

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "root")
DB_NAME = os.getenv("DB_NAME", "medicy_db")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def get_engine(retries=5, delay=2):
    for attempt in range(retries):
        try:
            engine = create_engine(DATABASE_URL, pool_pre_ping=True, pool_recycle=3600)
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print(f"Database connection successful on attempt {attempt + 1}")
            return engine
        except exc.OperationalError as e:
            if attempt < retries - 1:
                print(f"Database connection attempt {attempt + 1} failed. Retrying in {delay}s...")
                time.sleep(delay)
                delay *= 2
            else:
                raise e

engine = get_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
