from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.chat import Chat
from app.schemas.chat_schema import ChatCreate, ChatOut

router = APIRouter()

@router.get("/", response_model=list[ChatOut])
def get_chats(db: Session = Depends(get_db)):
    return db.query(Chat).all()

@router.post("/", response_model=ChatOut)
def create_chat(chat: ChatCreate, db: Session = Depends(get_db)):
    new_chat = Chat(**chat.dict())
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)
    return new_chat

__all__ = ['router']