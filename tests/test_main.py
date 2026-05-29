from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def criar_cliente():

    client.post(
        "/clientes",
        json={
            "cliente_nome": "Maria",
            "cliente_email": "maria_teste@email.com",
            "tipo_solicitacao": "Teste",
            "valor_patrimonio": 300000
        }
    )


def test_create_client():

    response = client.post(
        "/clientes",
        json={
            "cliente_nome": "João",
            "cliente_email": "joao@email.com",
            "tipo_solicitacao": "Teste",
            "valor_patrimonio": 50000
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Cliente criado com sucesso"


def test_webhook_prioridade_alta():

    criar_cliente()

    response = client.post(
        "/webhooks/pipefy/card-updated",
        json={
            "event_id": "evt_test_1",
            "card_id": "card_1",
            "cliente_email": "maria_teste@email.com",
            "timestamp": "2026-05-18T12:00:00Z"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["prioridade"] == "prioridade_alta"


def test_webhook_duplicado():

    criar_cliente()

    client.post(
        "/webhooks/pipefy/card-updated",
        json={
            "event_id": "evt_test_1",
            "card_id": "card_1",
            "cliente_email": "maria_teste@email.com",
            "timestamp": "2026-05-18T12:00:00Z"
        }
    )

    response = client.post(
        "/webhooks/pipefy/card-updated",
        json={
            "event_id": "evt_test_1",
            "card_id": "card_1",
            "cliente_email": "maria_teste@email.com",
            "timestamp": "2026-05-18T12:00:00Z"
        }
    )

    assert response.status_code == 400

    data = response.json()

    assert data["detail"] == "Evento já processado"