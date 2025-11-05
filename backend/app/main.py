from fastapi import FastAPI
from app.db.session import Base, engine
from app.routers import (
    user_router, medicine_router, reminder_router, chat_router,
    notification_router, user_medications_router
)

app = FastAPI(title="Medicy API (MySQL Connected)")

# ✅ สร้างตารางถ้ายังไม่มี
Base.metadata.create_all(bind=engine)

# ✅ Include routers
app.include_router(user_router, prefix="/api/users", tags=["Users"])
app.include_router(medicine_router, prefix="/api/medicines", tags=["Medicines"])
app.include_router(reminder_router, prefix="/api/reminders", tags=["Reminders"])
app.include_router(chat_router, prefix="/api/chats", tags=["Chats"])
app.include_router(notification_router, prefix="/api/notifications", tags=["Notifications"])
app.include_router(user_medications_router, prefix="/api/user_medications", tags=["User Medications"])  


@app.get("/")
def root():
    return {"message": "Medicy backend connected to MySQL successfully 🚀"}
