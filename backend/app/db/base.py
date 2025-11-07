# Ensure models are imported so SQLAlchemy sees them; exclude medicine
from importlib import import_module

_model_modules = [
    "app.models.users",
    "app.models.role",
    "app.models.status",
    "app.models.reminder",
    "app.models.notification",
    "app.models.chat",
    "app.models.user_medications",  # updated to no FK to medicine
    # DO NOT include: app.models.medicine
]

for _m in _model_modules:
    try:
        import_module(_m)
    except Exception as _e:
        # Skip missing modules; keeps app flexible across repo variants
        pass
