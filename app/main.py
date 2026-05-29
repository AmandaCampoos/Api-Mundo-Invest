from fastapi import FastAPI

from app.core.database import Base
from app.core.database import engine
from app.api.routes.clients import router as client_router

from app.models.client import Client
from app.api.routes.webhooks import router as webhook_router
from app.models.webhook_event import WebhookEvent

Base.metadata.create_all(bind=engine)

app = FastAPI(
title="Mundo Invest API",
version="1.0.0"
)
app.include_router(client_router)
@app.get("/")
def root():return {
"message": "Mundo Invest API online"
}
app.include_router(webhook_router)

