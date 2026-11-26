from abc import ABC, abstractmethod
from typing import List, Optional
from restaurante.domain.entities.pedido import Pedido


class PedidoRepository(ABC):
    @abstractmethod
    def listar(self) -> List[Pedido]:
        pass

    @abstractmethod
    def obtener_por_id(self, id_pedido: int) -> Optional[Pedido]:
        pass

    @abstractmethod
    def crear(self, pedido: Pedido) -> Pedido:
        pass

    @abstractmethod
    def actualizar(self, pedido: Pedido) -> Pedido:
        pass

    @abstractmethod
    def eliminar(self, id_pedido: int) -> None:
        pass