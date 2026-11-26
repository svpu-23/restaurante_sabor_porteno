from abc import ABC, abstractmethod
from typing import List, Optional
from restaurante.domain.entities.mesa import Mesa


class MesaRepository(ABC):
    @abstractmethod
    def listar(self) -> List[Mesa]:
        pass

    @abstractmethod
    def obtener_por_numero(self, numero: int) -> Optional[Mesa]:
        pass

    @abstractmethod
    def crear(self, mesa: Mesa) -> Mesa:
        pass

    @abstractmethod
    def actualizar(self, mesa: Mesa) -> Mesa:
        pass

    @abstractmethod
    def eliminar(self, numero: int) -> None:
        pass

    @abstractmethod
    def tiene_pedidos(self, numero: int) -> bool:
        pass