# backend/app/main.py

from fastapi import FastAPI
from app.db.session import Base, engine 
# ต้องมีตัวแปร router ที่ถูก export จาก user_router.py
from app.routers.user_router import router as user_router_instance 

app = FastAPI(title="Medicy API (Connected to MySQL)")

# สร้างตารางเมื่อเริ่มต้น
Base.metadata.create_all(bind=engine) 

app.include_router(user_router_instance, prefix="/api/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "Medicy backend connected to MySQL successfully!"}