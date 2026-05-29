
# Mundo Invest API

API desenvolvida com FastAPI para gerenciamento de clientes e simulação de integração com Pipefy utilizando GraphQL.
A aplicação realiza cadastro de clientes, processamento de webhooks, definição de prioridade baseada em patrimônio, persistência em banco de dados local e testes automatizados.



---

# Tecnologias utilizadas

* Python 3.12
* FastAPI
* SQLAlchemy
* SQLite
* Pytest
* Uvicorn

---

# Estrutura do Projeto Basica

```bash
backend/
│
├── app/
│   ├── api/
│   │   └── routes/
│   │       ├── clients.py
│   │       └── webhooks.py
│   │
│   ├── core/
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── client.py
│   │   └── webhook_event.py
│   │
│   ├── schemas/
│   │   ├── client.py
│   │   └── webhook.py
│   │
│   └── main.py
│
├── tests/
│   └── test_main.py
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

# Como executar o projeto localmente

## 1. Clonar repositório

```bash
git clone <url-do-repositorio>
```

---

## 2. Criar ambiente virtual

### Windows

```bash
python -m venv venv
```

---

## 3. Ativar ambiente virtual

### PowerShell

```bash
venv\Scripts\activate
```

---

## 4. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 5. Executar aplicação

```bash
uvicorn app.main:app --reload
```

A API ficará disponível em:

```txt
http://127.0.0.1:8000
```

Swagger:

```txt
http://127.0.0.1:8000/docs
```

---

# Executar os testes

```bash
pytest -v
```

Resultado esperado:

```bash
3 passed
```

---

# Endpoint - Criar Cliente

## POST /clientes

### Exemplo curl

```bash
curl -X POST "http://127.0.0.1:8000/clientes" ^
-H "Content-Type: application/json" ^
-d "{\"cliente_nome\":\"Maria\",\"cliente_email\":\"maria@email.com\",\"tipo_solicitacao\":\"Investimento\",\"valor_patrimonio\":300000}"
```

---

# Endpoint - Webhook Pipefy

## POST /webhooks/pipefy/card-updated

### Exemplo curl

```bash
curl -X POST "http://127.0.0.1:8000/webhooks/pipefy/card-updated" ^
-H "Content-Type: application/json" ^
-d "{\"event_id\":\"evt_123\",\"card_id\":\"card_456\",\"cliente_email\":\"maria@email.com\",\"timestamp\":\"2026-05-18T12:00:00Z\"}"
```

---

# Regras de negócio

* Clientes com patrimônio maior ou igual a R$100.000 recebem:

```txt
prioridade_alta
```

* Eventos duplicados de webhook não são processados novamente.

---

# Visão de Produção (AWS)

Em ambiente de produção, esta arquitetura pode escalar utilizando serviços AWS.

## API Gateway

Responsável por receber requisições HTTP externas.

## AWS Lambda

Executaria os endpoints da API de forma serverless, escalando automaticamente conforme demanda.

## Banco de Dados

### DynamoDB

Poderia ser utilizado para armazenamento de eventos de webhook com alta escalabilidade.

### Amazon RDS

Poderia armazenar os dados relacionais de clientes utilizando PostgreSQL.

## Benefícios da arquitetura

* Escalabilidade automática
* Alta disponibilidade
* Redução de custo operacional
* Processamento assíncrono de webhooks
* Facilidade de monitoramento com CloudWatch

---

# Autor

Amanda Campos Ximenes
