from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import date, time, datetime

class BirthdayCreate(BaseModel):
    user_id: UUID
    person_name: str
    relation: Optional[str] = None
    birth_date: date
    custom_message: Optional[str] = None
    gift_idea: Optional[str] = None
    reminder_time: time

class BirthdayResponse(BaseModel):
    id: UUID
    user_id: UUID
    person_name: str
    relation: Optional[str]
    birth_date: date
    custom_message: Optional[str]
    gift_idea: Optional[str]
    reminder_time: time
    created_at: datetime

    class Config:
        orm_mode = True