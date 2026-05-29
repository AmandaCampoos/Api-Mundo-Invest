from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from app.core.database import Base


class WebhookEvent(Base):

    __tablename__ = "webhook_events"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    event_id = Column(
        String,
        unique=True,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )