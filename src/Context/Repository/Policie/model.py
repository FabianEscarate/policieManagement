from sqlmodel import Field, SQLModel
from uuid import UUID, uuid4
from datetime import datetime
from enum import Enum

class policieStatus(str, Enum):
    issued = 'Emitida'
    active = 'Activa'
    annulled = 'Anulada'

class Policie(SQLModel, table=True):
    id: UUID | None = Field(default_factory=uuid4, primary_key=True)
    rutTitular: str = Field(index=True)
    fechaEmision: datetime
    planSalud: str
    prima: int = Field()
    estado: policieStatus

class UpdateStatePolicie(SQLModel):
    estado:policieStatus | None = Field(default=None)