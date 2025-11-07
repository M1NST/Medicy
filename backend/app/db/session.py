import os
import time
from sqlalchemy import create_engine, exc, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Read environment variables with defaults
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", "3306")
DB_USER = os.environ.get("DB_USER", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "root")
DB_NAME = os.environ.get("DB_NAME", "medicy_db")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Add retry logic for database connection
def get_engine(retries=5, delay=2):
    for attempt in range(retries):
        try:
            engine = create_engine(
                DATABASE_URL,
                pool_pre_ping=True,  # Adds connection health checks
                pool_recycle=3600    # Recycle connections after 1 hour
            )
            # Test the connection
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print(f"Database connection successful on attempt {attempt + 1}")
            return engine
        except exc.OperationalError as e:
            if attempt < retries - 1:
                print(f"Database connection attempt {attempt + 1} failed. Retrying in {delay} seconds...")
                time.sleep(delay)
                delay *= 2  # Exponential backoff
            else:
                print("All database connection attempts failed")
                raise e


# Create engine with retry mechanism
engine = get_engine()

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create declarative base
Base = declarative_base()

def get_db():
    """
    Dependency function to get DB session.
    Used as FastAPI dependency injection.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()