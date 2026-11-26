from typing import List, Optional
from restaurante.domain.entities.categoria_plato import CategoriaPlato
from restaurante.domain.repositories.categoria_plato_repository import CategoriaPlatoRepository
from restaurante.infrastructure.models.categoria_plato_model import CategoriaPlatoModel
from restaurante.infrastructure.models.plato_model import PlatoModel


class DjangoCategoriaPlatoRepository(CategoriaPlatoRepository):
    def _a_entidad(self, modelo: CategoriaPlatoModel) -> CategoriaPlato:
        return CategoriaPlato(
            id_categoria=modelo.id_categoria,
            nombre=modelo.nombre,
        )

    def listar(self) -> List[CategoriaPlato]:
        return [
            self._a_entidad(c)
            for c in CategoriaPlatoModel.objects.all().order_by("id_categoria")
        ]

    def obtener_por_id(self, id_categoria: int) -> Optional[CategoriaPlato]:
        modelo = CategoriaPlatoModel.objects.filter(id_categoria=id_categoria).first()
        return self._a_entidad(modelo) if modelo else None

    def obtener_por_nombre(self, nombre: str) -> Optional[CategoriaPlato]:
        modelo = CategoriaPlatoModel.objects.filter(nombre__iexact=nombre).first()
        return self._a_entidad(modelo) if modelo else None

    def crear(self, categoria: CategoriaPlato) -> CategoriaPlato:
        modelo = CategoriaPlatoModel.objects.create(nombre=categoria.nombre)
        return self._a_entidad(modelo)

    def actualizar(self, categoria: CategoriaPlato) -> CategoriaPlato:
        CategoriaPlatoModel.objects.filter(id_categoria=categoria.id_categoria).update(
            nombre=categoria.nombre
        )
        return categoria

    def eliminar(self, id_categoria: int) -> None:
        CategoriaPlatoModel.objects.filter(id_categoria=id_categoria).delete()

    def tiene_platos(self, id_categoria: int) -> bool:
        return PlatoModel.objects.filter(categoria_id=id_categoria).exists()