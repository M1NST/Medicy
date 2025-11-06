"""Import model modules (not class names) to avoid import-order/circular issues.

Avoid importing class names at package import time; importing modules ensures
SQLAlchemy mappers are registered when each model module is imported and
reduces the chance of referencing a class name before it's defined.
"""

from . import role
from . import users
from . import medicine
from . import user_medications
from . import status
from . import reminder
from . import notification
from . import chat
