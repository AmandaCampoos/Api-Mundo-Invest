from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.core.database import Base


class WebhookEvent(Base):

    __tablename__ = "webhook_events"

    id = Column(Integer, primary_key=True, index=True)

    event_id = Column(String, unique=True, nullable=False)

    card_id = Column(String, nullable=False, index=True)  

    created_at = Column(DateTime, default=datetime.utcnow)