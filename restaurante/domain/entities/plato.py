from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Plato:
    codigo: str
    nombre: str
    id_categoria: int
    precio: Decimal
    disponible: bool = True