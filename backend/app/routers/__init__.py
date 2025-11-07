# Auto-import routers (excluding medicine)
__all__ = []

def _try(name, asname):
    try:
        mod = __import__(name, fromlist=["router"])
        router = getattr(mod, "router", None)
        if router is not None:
            globals()[asname] = router
            __all__.append(asname)
    except Exception:
        pass

_try("app.routers.user_router", "user_router")
_try("app.routers.reminder_router", "reminder_router")
_try("app.routers.chat_router", "chat_router")
_try("app.routers.notification_router", "notification_router")
_try("app.routers.user_medications_router", "user_medications_router")

# Intentionally NOT importing: app.routers.medicine_router
