from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.session import Base, engine

from app.models import (
    role,
    users,
    user_medications,
    reminder,
    status,
    notification,
    chat,
)

from app.routers import (
    user_router,
    user_medications_router,
    reminder_router,
    notification_router,
    chat_router,
)

app = FastAPI(title="Medicy Backend API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/api/users", tags=["Users"])
app.include_router(user_medications_router, prefix="/api/user_medications", tags=["User Medications"])
app.include_router(reminder_router, prefix="/api/reminders", tags=["Reminders"])
app.include_router(notification_router, prefix="/api/notifications", tags=["Notifications"])
app.include_router(chat_router, prefix="/api/chats", tags=["Chats"])

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Medicy backend is running 🚀"}
