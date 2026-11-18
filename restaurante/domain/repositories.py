from abc import ABC, abstractmethod
from typing import List, Optional
from restaurante.domain.entities import (
    Mesa,
    CategoriaPlato,
    Plato,
    Pedido,
    DetallePedido,
)


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


class CategoriaPlatoRepository(ABC):
    @abstractmethod
    def listar(self) -> List[CategoriaPlato]:
        pass

    @abstractmethod
    def obtener_por_id(self, id_categoria: int) -> Optional[CategoriaPlato]:
        pass

    @abstractmethod
    def obtener_por_nombre(self, nombre: str) -> Optional[CategoriaPlato]:
        pass

    @abstractmethod
    def crear(self, categoria: CategoriaPlato) -> CategoriaPlato:
        pass

    @abstractmethod
    def actualizar(self, categoria: CategoriaPlato) -> CategoriaPlato:
        pass

    @abstractmethod
    def eliminar(self, id_categoria: int) -> None:
        pass

    @abstractmethod
    def tiene_platos(self, id_categoria: int) -> bool:
        pass


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