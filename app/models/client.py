from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime
from datetime import datetime
from app.core.database import Base

# Model responsável pela estrutura da tabela de clientes no banco de dados,
#  incluindo dados cadastrais, status da análise e definição de prioridade.
class Client(Base):

    __tablename__ = "clients"

    id = Column(
    Integer,
    primary_key=True,
    index=True
)

    cliente_nome = Column(
    String,
    nullable=False
)

    cliente_email = Column(
    String,
    unique=True,
    nullable=False
)

    tipo_solicitacao = Column(
    String,
    nullable=False
)

    valor_patrimonio = Column(
    Float,
    nullable=False
)

    status = Column(
    String,
    default="Aguardando Análise"
)

    prioridade = Column(
    String,
    nullable=True
)

    created_at = Column(
    DateTime,
    default=datetime.utcnow
)
