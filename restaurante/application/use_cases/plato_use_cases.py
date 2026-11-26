from decimal import Decimal
from typing import List
from restaurante.domain.entities.plato import Plato
from restaurante.domain.repositories.plato_repository import PlatoRepository
from restaurante.domain.repositories.categoria_plato_repository import CategoriaPlatoRepository
from restaurante.application.exceptions import (
    DatosRestauranteInvalidosError,
    CategoriaNoEncontradaError,
    PlatoNoEncontradoError,
    PlatoDuplicadoError,
    PlatoEnPedidosError,
)


class PlatoUseCases:
    def __init__(self, plato_repo: PlatoRepository, categoria_repo: CategoriaPlatoRepository):
        self.plato_repo = plato_repo
        self.categoria_repo = categoria_repo

    def listar(self) -> List[Plato]:
        return self.plato_repo.listar()

    def obtener_por_codigo(self, codigo: str) -> Plato:
        codigo_limpio = codigo.strip().upper()
        plato = self.plato_repo.obtener_por_codigo(codigo_limpio)
        if not plato:
            raise PlatoNoEncontradoError(f"El plato con código '{codigo_limpio}' no existe.")
        return plato

    def crear(
        self,
        codigo: str,
        nombre: str,
        id_categoria: int,
        precio: Decimal,
        disponible: bool = True,
    ) -> Plato:
        codigo_limpio = codigo.strip().upper()
        nombre_limpio = nombre.strip()

        if not codigo_limpio or not nombre_limpio:
            raise DatosRestauranteInvalidosError("El código y el nombre del plato son obligatorios.")
        if precio < Decimal("0"):
            raise DatosRestauranteInvalidosError("El precio del plato no puede ser negativo.")

        if self.plato_repo.obtener_por_codigo(codigo_limpio):
            raise PlatoDuplicadoError(f"Ya existe un plato con el código '{codigo_limpio}'.")
        if self.plato_repo.obtener_por_nombre(nombre_limpio):
            raise PlatoDuplicadoError(f"Ya existe un plato llamado '{nombre_limpio}'.")

        if not self.categoria_repo.obtener_por_id(id_categoria):
            raise CategoriaNoEncontradaError(f"La categoría con ID {id_categoria} no existe.")

        nuevo_plato = Plato(
            codigo=codigo_limpio,
            nombre=nombre_limpio,
            id_categoria=id_categoria,
            precio=precio,
            disponible=disponible,
        )
        return self.plato_repo.crear(nuevo_plato)

    def actualizar(
        self,
        codigo: str,
        nombre: str,
        id_categoria: int,
        precio: Decimal,
        disponible: bool,
    ) -> Plato:
        codigo_limpio = codigo.strip().upper()
        self.obtener_por_codigo(codigo_limpio)

        nombre_limpio = nombre.strip()
        if not nombre_limpio:
            raise DatosRestauranteInvalidosError("El nombre del plato no puede estar vacío.")
        if precio < Decimal("0"):
            raise DatosRestauranteInvalidosError("El precio del plato no puede ser negativo.")

        existente = self.plato_repo.obtener_por_nombre(nombre_limpio)
        if existente and existente.codigo != codigo_limpio:
            raise PlatoDuplicadoError(f"Ya existe otro plato llamado '{nombre_limpio}'.")

        if not self.categoria_repo.obtener_por_id(id_categoria):
            raise CategoriaNoEncontradaError(f"La categoría con ID {id_categoria} no existe.")

        plato_actualizado = Plato(
            codigo=codigo_limpio,
            nombre=nombre_limpio,
            id_categoria=id_categoria,
            precio=precio,
            disponible=disponible,
        )
        return self.plato_repo.actualizar(plato_actualizado)

    def eliminar(self, codigo: str) -> None:
        codigo_limpio = codigo.strip().upper()
        self.obtener_por_codigo(codigo_limpio)

        if self.plato_repo.tiene_detalles(codigo_limpio):
            raise PlatoEnPedidosError(
                f"No se puede eliminar el plato '{codigo_limpio}' porque tiene pedidos registrados."
            )

        self.plato_repo.eliminar(codigo_limpio)