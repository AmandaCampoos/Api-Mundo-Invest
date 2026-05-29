# Classe responsável por simular requisições HTTP nos testes da API
from fastapi.testclient import TestClient

# Importa a aplicação principal do FastAPI
from app.main import app

# Cria cliente de testes para executar chamadas nos endpoints
client = TestClient(app)


# Função auxiliar para criar um cliente padrão usado nos testes
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


# Testa se o endpoint de criação de cliente retorna sucesso
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

    # Verifica se a API respondeu corretamente
    assert response.status_code == 200

    data = response.json()

    # Valida mensagem de sucesso
    assert data["message"] == "Cliente criado com sucesso"


# Testa se o webhook define prioridade alta para clientes com alto patrimônio
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

    # Verifica resposta de sucesso do webhook
    assert response.status_code == 200

    data = response.json()

    # Confirma aplicação da regra de prioridade alta
    assert data["prioridade"] == "prioridade_alta"


# Testa bloqueio de eventos duplicados
def test_webhook_duplicado():

    criar_cliente()

    # Primeiro processamento do evento
    client.post(
        "/webhooks/pipefy/card-updated",
        json={
            "event_id": "evt_test_1",
            "card_id": "card_1",
            "cliente_email": "maria_teste@email.com",
            "timestamp": "2026-05-18T12:00:00Z"
        }
    )

    # Segunda tentativa com mesmo event_id
    response = client.post(
        "/webhooks/pipefy/card-updated",
        json={
            "event_id": "evt_test_1",
            "card_id": "card_1",
            "cliente_email": "maria_teste@email.com",
            "timestamp": "2026-05-18T12:00:00Z"
        }
    )

    # Verifica se o sistema bloqueou duplicidade
    assert response.status_code == 400

    data = response.json()

    # Confirma mensagem de erro esperada
    assert data["detail"] == "Evento já processado"