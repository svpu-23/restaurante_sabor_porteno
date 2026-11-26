from dataclasses import dataclass
from typing import Optional


@dataclass
class CategoriaPlato:
    nombre: str
    id_categoria: Optional[int] = None