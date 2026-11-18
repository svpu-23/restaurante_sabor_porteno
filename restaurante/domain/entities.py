from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional


@dataclass
class Mesa:
    capacidad: int
    activa: bool = True
    numero: Optional[int] = None


@dataclass
class CategoriaPlato:
    nombre: str
    id_categoria: Optional[int] = None


@dataclass
class Plato:
    codigo: str
    nombre: str
    id_categoria: int
    precio: Decimal
    disponible: bool = True


@dataclass
class Pedido:
    numero_mesa: int
    garzon: str
    propina: Decimal = Decimal("0.00")
    total: Decimal = Decimal("0.00")
    estado: str = "abierto"
    fecha: Optional[datetime] = None
    id_pedido: Optional[int] = None


@dataclass
class DetallePedido:
    id_pedido: int
    codigo_plato: str
    cantidad: int
    precio_unitario: Decimal
    observacion: Optional[str] = None