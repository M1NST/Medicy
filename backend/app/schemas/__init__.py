# backend/app/schemas/__init__.py

"""
(ฉบับแก้ไขครั้งที่ 3 - อิงตามไฟล์จริง 100%)
Import Pydantic models จากไฟล์ลูก โดยใช้ชื่อคลาสที่ถูกต้อง
(เช่น UserSchema, ChatSchema, ReminderSchema)
"""

# 1. Import สคีมาจาก user_schema.py
from .user_schema import  UserCreate, UserOut

# 2. Import สคีมาจาก user_medication_schema.py
from .user_medication_schema import  UserMedicationCreate, UserMedicationOut

# 3. Import สคีมาจาก chat_schema.py
from .chat_schema import  ChatCreate, ChatOut

# 4. Import สคีมาจาก notification_schema.py
from .notification_schema import  NotificationCreate, NotificationOut

# 5. Import สคีมาจาก reminder_schema.py
from .reminder_schema import  ReminderCreate, ReminderOut