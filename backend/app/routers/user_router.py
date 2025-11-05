# app/routers/user_router.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.users import User
from pydantic import BaseModel
from typing import List, Optional  # ✅ ใช้ Optional แทน |
 
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# schema สำหรับรับข้อมูล
class UserCreate(BaseModel):
    username: str
    email: str
    phone: Optional[str] = None  # ✅ ใช้ Optional
    password_hash: str

class UserOut(BaseModel):
    user_id: int
    username: str
    email: str
    phone: Optional[str] = None
    class Config:
        orm_mode = True

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        username=user.username,
        email=user.email,
        phone=user.phone,
        password_hash=user.password_hash
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
