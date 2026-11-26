from abc import ABC, abstractmethod
from typing import List, Optional
from restaurante.domain.entities.detalle_pedido import DetallePedido


class DetallePedidoRepository(ABC):
    @abstractmethod
    def listar_por_pedido(self, id_pedido: int) -> List[DetallePedido]:
        pass

    @abstractmethod
    def obtener_por_pk(self, id_pedido: int, codigo_plato: str) -> Optional[DetallePedido]:
        pass

    @abstractmethod
    def agregar(self, detalle: DetallePedido) -> DetallePedido:
        pass

    @abstractmethod
    def actualizar(self, detalle: DetallePedido) -> DetallePedido:
        pass

    @abstractmethod
    def eliminar(self, id_pedido: int, codigo_plato: str) -> None:
        pass