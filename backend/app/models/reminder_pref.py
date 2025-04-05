# backend/app/models/reminder_pref.py

from sqlalchemy import Column, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from ..core.database import Base

class ReminderPreference(Base):
    __tablename__ = "reminder_preferences"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    email_enabled = Column(Boolean, default=True)
    telegram_enabled = Column(Boolean, default=False)
    sms_enabled = Column(Boolean, default=False)
    push_enabled = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)