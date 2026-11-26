from abc import ABC, abstractmethod
from typing import List, Optional
from restaurante.domain.entities.plato import Plato


class PlatoRepository(ABC):
    @abstractmethod
    def listar(self) -> List[Plato]:
        pass

    @abstractmethod
    def obtener_por_codigo(self, codigo: str) -> Optional[Plato]:
        pass

    @abstractmethod
    def obtener_por_nombre(self, nombre: str) -> Optional[Plato]:
        pass

    @abstractmethod
    def crear(self, plato: Plato) -> Plato:
        pass

    @abstractmethod
    def actualizar(self, plato: Plato) -> Plato:
        pass

    @abstractmethod
    def eliminar(self, codigo: str) -> None:
        pass

    @abstractmethod
    def tiene_detalles(self, codigo: str) -> bool:
        pass