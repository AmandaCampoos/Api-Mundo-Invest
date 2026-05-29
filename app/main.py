from fastapi import FastAPI

from app.core.database import Base, engine

from app.api.routes.clients import router as client_router
from app.api.routes.webhooks import router as webhook_router

from app.models.client import Client
from app.models.webhook_event import WebhookEvent

# Arquivo principal da aplicação: inicializa o FastAPI, 
# cria as tabelas do banco de dados e registra todas as rotas disponíveis da API.

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mundo Invest API",
    version="1.0.0"
)

# rotas
app.include_router(client_router)
app.include_router(webhook_router, prefix="/webhooks")


@app.get("/")
def root():
    return {
        "message": "Mundo Invest API online"
    }


print("ROTAS REGISTRADAS:")
for r in app.routes:
    print(r.path)