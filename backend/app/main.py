from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Medicy Backend API (no-medicine)")

# CORS for Android emulator / devices (adjust as needed)
origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://10.0.2.2",     # Android emulator
    "*",                   # dev only
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB metadata init
try:
    from app.db.session import Base, engine
    Base.metadata.create_all(bind=engine)
except Exception as e:
    # Keep app booting even if DB is not ready; logs help debugging
    import logging
    logging.getLogger(__name__).warning("DB init skipped: %s", e)

# Dynamically import routers except medicine
from importlib import import_module

router_modules = [
    "app.routers.user_router",
    "app.routers.reminder_router",
    "app.routers.chat_router",
    "app.routers.notification_router",
    "app.routers.user_medications_router",
    # DO NOT include: app.routers.medicine_router
]

for mod_name in router_modules:
    try:
        mod = import_module(mod_name)
        router = getattr(mod, "router", None)
        if router is not None:
            prefix = getattr(mod, "API_PREFIX", None)
            tags = getattr(mod, "API_TAGS", None)
            if prefix is None:
                # infer prefix from module name, e.g., user_router -> /api/users
                name = mod_name.rsplit(".", 1)[-1].replace("_router", "")
                if name.endswith("s"):
                    base = name
                else:
                    base = name + "s"
                prefix = f"/api/{base}"
            if tags is None:
                tags = [prefix.removeprefix("/api/").title()]
            app.include_router(router, prefix=prefix, tags=tags)
    except Exception as e:
        import logging
        logging.getLogger(__name__).warning("Skip router %s: %s", mod_name, e)


@app.get("/")
def root():
    return {"message": "Medicy backend (no-medicine) is up 🚀"}
