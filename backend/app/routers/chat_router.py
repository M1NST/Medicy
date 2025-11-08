# backend/app/routers/chat_router.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_ # 1. [เพิ่ม] Import 'or_'
from app import models, schemas
from app.db.session import get_db

router = APIRouter()

# 2. [แก้ไข] แก้ไขฟังก์ชัน 'get_chats'
@router.get("/", response_model=list[schemas.ChatOut])
def get_chats(
    user_id_1: int,     # 3. [เพิ่ม] รับ user_id_1 เป็น Query Parameter
    user_id_2: int,     # 4. [เพิ่ม] รับ user_id_2 เป็น Query Parameter
    db: Session = Depends(get_db)
):
    """
    ดึงข้อความแชททั้งหมดระหว่างผู้ใช้สองคน (user_id_1 และ user_id_2)
    """
    # 5. [แก้ไข] เปลี่ยน Query ให้กรองข้อมูล
    chats = db.query(models.Chat).filter(
        or_(
            # (A ส่งหา B)
            (models.Chat.sender_id == user_id_1) & (models.Chat.receiver_id == user_id_2),
            # (B ส่งหา A)
            (models.Chat.sender_id == user_id_2) & (models.Chat.receiver_id == user_id_1)
        )
    ).order_by(models.Chat.sent_at).all() # 6. [เพิ่ม] .order_by() เพื่อเรียงตามเวลา
    
    return chats


@router.post("/", response_model=schemas.ChatOut)
def create_chat(
    chat: schemas.ChatCreate, 
    db: Session = Depends(get_db)
):
    """
    สร้างข้อความแชทใหม่
    """
    # (ฟังก์ชันนี้เหมือนเดิม ไม่ต้องแก้)
    db_chat = models.Chat(
        sender_id=chat.sender_id,
        receiver_id=chat.receiver_id,
        message=chat.message
    )
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat