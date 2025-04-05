# backend/app/models/birthday.py

from sqlalchemy import Column, String, DateTime, Date, Time, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from ..core.database import Base

class Birthday(Base):
    __tablename__ = "birthdays"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    person_name = Column(String, nullable=False)
    relation = Column(String)
    birth_date = Column(Date, nullable=False)
    custom_message = Column(String)
    gift_idea = Column(String)
    reminder_time = Column(Time, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)