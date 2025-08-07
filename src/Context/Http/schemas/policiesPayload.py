from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from enum import Enum

class policieStatus(str, Enum):
    issued = 'Emitida'
    active = 'Activa'
    annulled = 'Anulada'

class createPolicie(BaseModel):
    id:UUID | None = Field(default=None, title="id of policie")
    rutTitular: str
    fechaEmision: datetime
    planSalud: str
    prima: int
    estado:policieStatus
class Policie(BaseModel):
    id:UUID
    rutTitular: str
    fechaEmision: datetime
    planSalud: str
    prima: int
    estado:policieStatus