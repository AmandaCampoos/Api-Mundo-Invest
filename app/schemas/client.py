from pydantic import BaseModel
from pydantic import EmailStr

class ClientCreate(BaseModel):

    cliente_nome: str
    cliente_email: str
    tipo_solicitacao: str
    valor_patrimonio: float