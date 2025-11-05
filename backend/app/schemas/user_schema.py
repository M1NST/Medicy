from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    first_name: str
    last_name: Optional[str]
    email: Optional[str]
    phone_num: Optional[str]
    username: str

class UserCreate(UserBase):
    password_hash: str
    role_code: Optional[int] = None

class UserOut(UserBase):
    user_id: int
    class Config:
        orm_mode = True
