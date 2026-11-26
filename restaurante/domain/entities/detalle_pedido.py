from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass
class DetallePedido:
    id_pedido: int
    codigo_plato: str
    cantidad: int
    precio_unitario: Decimal
    observacion: Optional[str] = None