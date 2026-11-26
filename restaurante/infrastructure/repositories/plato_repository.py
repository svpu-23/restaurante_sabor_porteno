from typing import List, Optional
from restaurante.domain.entities.plato import Plato
from restaurante.domain.repositories.plato_repository import PlatoRepository
from restaurante.infrastructure.models.plato_model import PlatoModel
from restaurante.infrastructure.models.detalle_pedido_model import DetallePedidoModel


class DjangoPlatoRepository(PlatoRepository):
    def _a_entidad(self, modelo: PlatoModel) -> Plato:
        return Plato(
            codigo=modelo.codigo,
            nombre=modelo.nombre,
            id_categoria=modelo.categoria_id,
            precio=modelo.precio,
            disponible=bool(modelo.disponible),
        )

    def listar(self) -> List[Plato]:
        return [self._a_entidad(p) for p in PlatoModel.objects.all().order_by("codigo")]

    def obtener_por_codigo(self, codigo: str) -> Optional[Plato]:
        modelo = PlatoModel.objects.filter(codigo=codigo).first()
        return self._a_entidad(modelo) if modelo else None

    def obtener_por_nombre(self, nombre: str) -> Optional[Plato]:
        modelo = PlatoModel.objects.filter(nombre__iexact=nombre).first()
        return self._a_entidad(modelo) if modelo else None

    def crear(self, plato: Plato) -> Plato:
        modelo = PlatoModel.objects.create(
            codigo=plato.codigo,
            nombre=plato.nombre,
            categoria_id=plato.id_categoria,
            precio=plato.precio,
            disponible=plato.disponible,
        )
        return self._a_entidad(modelo)

    def actualizar(self, plato: Plato) -> Plato:
        PlatoModel.objects.filter(codigo=plato.codigo).update(
            nombre=plato.nombre,
            categoria_id=plato.id_categoria,
            precio=plato.precio,
            disponible=plato.disponible,
        )
        return plato

    def eliminar(self, codigo: str) -> None:
        PlatoModel.objects.filter(codigo=codigo).delete()

    def tiene_detalles(self, codigo: str) -> bool:
        return DetallePedidoModel.objects.filter(plato_id=codigo).exists()