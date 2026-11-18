from typing import List
from restaurante.domain.entities import CategoriaPlato
from restaurante.domain.repositories import CategoriaPlatoRepository
from restaurante.domain.exceptions import (
    EntidadNoEncontradaError,
    RegistroDuplicadoError,
    BorradoProtegidoError,
    ReglaNegocioInvalidaError,
)


class CategoriaPlatoUseCases:
    def __init__(self, categoria_repo: CategoriaPlatoRepository):
        self.categoria_repo = categoria_repo

    def listar(self) -> List[CategoriaPlato]:
        return self.categoria_repo.listar()

    def obtener_por_id(self, id_categoria: int) -> CategoriaPlato:
        categoria = self.categoria_repo.obtener_por_id(id_categoria)
        if not categoria:
            raise EntidadNoEncontradaError(f"La categoría con ID {id_categoria} no existe.")
        return categoria

    def crear(self, nombre: str) -> CategoriaPlato:
        nombre_limpio = nombre.strip()
        if not nombre_limpio:
            raise ReglaNegocioInvalidaError("El nombre de la categoría no puede estar vacío.")

        if self.categoria_repo.obtener_por_nombre(nombre_limpio):
            raise RegistroDuplicadoError(f"Ya existe una categoría llamada '{nombre_limpio}'.")

        nueva_categoria = CategoriaPlato(nombre=nombre_limpio)
        return self.categoria_repo.crear(nueva_categoria)

    def actualizar(self, id_categoria: int, nombre: str) -> CategoriaPlato:
        self.obtener_por_id(id_categoria)

        nombre_limpio = nombre.strip()
        if not nombre_limpio:
            raise ReglaNegocioInvalidaError("El nombre de la categoría no puede estar vacío.")

        existente = self.categoria_repo.obtener_por_nombre(nombre_limpio)
        if existente and existente.id_categoria != id_categoria:
            raise RegistroDuplicadoError(f"Ya existe otra categoría llamada '{nombre_limpio}'.")

        categoria_actualizada = CategoriaPlato(id_categoria=id_categoria, nombre=nombre_limpio)
        return self.categoria_repo.actualizar(categoria_actualizada)

    def eliminar(self, id_categoria: int) -> None:
        self.obtener_por_id(id_categoria)

        if self.categoria_repo.tiene_platos(id_categoria):
            raise BorradoProtegidoError(
                f"No se puede eliminar la categoría {id_categoria} porque tiene platos asociados."
            )

        self.categoria_repo.eliminar(id_categoria)