from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from enum import Enum

class policieStatus(str, Enum):
    issued = 'Emitida'
    active = 'Activa'
    annulled = 'Anulada'

class createPolicie(BaseModel):
    id:UUID
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