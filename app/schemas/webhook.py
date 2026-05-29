from pydantic import BaseModel


class WebhookPayload(BaseModel):
    event_id: str
    card_id: str
    cliente_email: str
    timestamp: str