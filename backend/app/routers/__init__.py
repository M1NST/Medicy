# Import all routers
from .user_router import router as user_router
from .medicine_router import router as medicine_router
from .reminder_router import router as reminder_router
from .chat_router import router as chat_router
from .notification_router import router as notification_router
from .user_medications_router import router as user_medications_router

__all__ = [
    'user_router',
    'medicine_router',
    'reminder_router',
    'chat_router',
    'notification_router',
    'user_medications_router'
]