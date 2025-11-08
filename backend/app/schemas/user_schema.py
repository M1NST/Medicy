from pydantic import BaseModel
from typing import Optional

from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    role_code: int = 1
    phone_num: str | None = None

class UserOut(BaseModel):
    user_id: int
    username: str
    role_code: int
    phone_num: str | None = None
    class Config:
        orm_mode = True
