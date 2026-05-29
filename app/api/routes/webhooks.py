from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.webhook_event import WebhookEvent
from app.models.client import Client
from app.schemas.webhook import WebhookPayload

router = APIRouter()


@router.post("/pipefy/card-updated")
def receive_webhook(
    payload: WebhookPayload,
    db: Session = Depends(get_db)
):

    # verifica se webhook já foi processado
    evento_existente = db.query(WebhookEvent).filter(
        WebhookEvent.event_id == payload.event_id
    ).first()

    if evento_existente:
        raise HTTPException(
            status_code=400,
            detail="Webhook já processado"
        )

    # salva evento
    novo_evento = WebhookEvent(
        event_id=payload.event_id,
        card_id=payload.card_id
    )

    db.add(novo_evento)

    # procura cliente
    cliente = db.query(Client).filter(
        Client.cliente_email == payload.cliente_email
    ).first()

    if not cliente:
        return {"error": "Cliente não encontrado"}

    # regra de prioridade
    if cliente.valor_patrimonio >= 100000:
        prioridade = "prioridade_alta"
    else:
        prioridade = "prioridade_normal"

    cliente.prioridade = prioridade

    db.commit()

    return {
        "message": "Webhook processado",
        "prioridade": prioridade
    }