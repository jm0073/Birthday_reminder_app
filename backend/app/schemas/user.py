from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str
    phone_number: Optional[str] = None
    profile_pic_url: Optional[str] = None
    timezone: Optional[str] = "UTC"

class UserResponse(BaseModel):
    id: UUID
    name: str
    username: str
    email: EmailStr
    phone_number: Optional[str] = None
    profile_pic_url: Optional[str] = None
    timezone: str
    created_at: datetime

    class Config:
        orm_mode = True