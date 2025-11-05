from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.chat import Chat

# Create router instance
router = APIRouter()

@router.get("/")
def get_chats(db: Session = Depends(get_db)):
    return db.query(Chat).all()

@router.post("/")
def create_chat(chat: dict, db: Session = Depends(get_db)):
    new_chat = Chat(**chat)
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)
    return new_chat

# Make sure router is exported
__all__ = ['router']
