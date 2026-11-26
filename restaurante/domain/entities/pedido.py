from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional


@dataclass
class Pedido:
    numero_mesa: int
    garzon: str
    propina: Decimal = Decimal("0.00")
    total: Decimal = Decimal("0.00")
    estado: str = "abierto"
    fecha: Optional[datetime] = None
    id_pedido: Optional[int] = None