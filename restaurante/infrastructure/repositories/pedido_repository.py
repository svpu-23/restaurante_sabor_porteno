from typing import List, Optional
from django.utils import timezone
from restaurante.domain.entities.pedido import Pedido
from restaurante.domain.repositories.pedido_repository import PedidoRepository
from restaurante.infrastructure.models.pedido_model import PedidoModel


class DjangoPedidoRepository(PedidoRepository):
    def _a_entidad(self, modelo: PedidoModel) -> Pedido:
        return Pedido(
            id_pedido=modelo.id_pedido,
            numero_mesa=modelo.mesa_id,
            garzon=modelo.garzon,
            fecha=modelo.fecha,
            propina=modelo.propina,
            total=modelo.total,
            estado=modelo.estado,
        )

    def listar(self) -> List[Pedido]:
        return [
            self._a_entidad(p)
            for p in PedidoModel.objects.all().order_by("-id_pedido")
        ]

    def obtener_por_id(self, id_pedido: int) -> Optional[Pedido]:
        modelo = PedidoModel.objects.filter(id_pedido=id_pedido).first()
        return self._a_entidad(modelo) if modelo else None

    def crear(self, pedido: Pedido) -> Pedido:
        fecha_registro = pedido.fecha or timezone.now()
        modelo = PedidoModel.objects.create(
            mesa_id=pedido.numero_mesa,
            garzon=pedido.garzon,
            fecha=fecha_registro,
            propina=pedido.propina,
            total=pedido.total,
            estado=pedido.estado,
        )
        return self._a_entidad(modelo)

    def actualizar(self, pedido: Pedido) -> Pedido:
        PedidoModel.objects.filter(id_pedido=pedido.id_pedido).update(
            mesa_id=pedido.numero_mesa,
            garzon=pedido.garzon,
            propina=pedido.propina,
            total=pedido.total,
            estado=pedido.estado,
        )
        return pedido

    def eliminar(self, id_pedido: int) -> None:
        PedidoModel.objects.filter(id_pedido=id_pedido).delete()