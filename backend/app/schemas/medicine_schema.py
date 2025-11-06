from pydantic import BaseModel
from typing import Optional

class MedicineBase(BaseModel):
    med_name: str
    description: Optional[str] = None

class MedicineCreate(MedicineBase):
    pass

class MedicineOut(MedicineBase):
    med_id: int
    class Config:
        from_attributes = True
