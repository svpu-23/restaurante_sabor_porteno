from dataclasses import dataclass
from typing import Optional


@dataclass
class Mesa:
    capacidad: int
    activa: bool = True
    numero: Optional[int] = None