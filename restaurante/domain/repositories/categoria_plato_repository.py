from abc import ABC, abstractmethod
from typing import List, Optional
from restaurante.domain.entities.categoria_plato import CategoriaPlato


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