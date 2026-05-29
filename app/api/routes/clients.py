from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.client import ClientCreate

from app.models.client import Client

router = APIRouter()

@router.post("/clientes")
def create_client(
client: ClientCreate,
db: Session = Depends(get_db)
):

    new_client = Client(
    cliente_nome=client.cliente_nome,
    cliente_email=client.cliente_email,
    tipo_solicitacao=client.tipo_solicitacao,
    valor_patrimonio=client.valor_patrimonio,
    
    status="Aguardando Análise",
    prioridade=None
)

    db.add(new_client)

    db.commit()

    db.refresh(new_client)

    return {
    "message": "Cliente criado com sucesso",
    "cliente_id": new_client.id
}

