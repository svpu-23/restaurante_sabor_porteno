from typing import List, Optional
from restaurante.domain.entities.detalle_pedido import DetallePedido
from restaurante.domain.repositories.detalle_pedido_repository import DetallePedidoRepository
from restaurante.infrastructure.models.detalle_pedido_model import DetallePedidoModel


class DjangoDetallePedidoRepository(DetallePedidoRepository):
    def _a_entidad(self, modelo: DetallePedidoModel) -> DetallePedido:
        return DetallePedido(
            id_pedido=modelo.pedido_id,
            codigo_plato=modelo.plato_id,
            cantidad=modelo.cantidad,
            precio_unitario=modelo.precio_unitario,
            observacion=modelo.observacion,
        )

    def listar_por_pedido(self, id_pedido: int) -> List[DetallePedido]:
        return [
            self._a_entidad(d)
            for d in DetallePedidoModel.objects.filter(pedido_id=id_pedido).order_by("plato_id")
        ]

    def obtener_por_pk(self, id_pedido: int, codigo_plato: str) -> Optional[DetallePedido]:
        modelo = DetallePedidoModel.objects.filter(
            pedido_id=id_pedido, plato_id=codigo_plato
        ).first()
        return self._a_entidad(modelo) if modelo else None

    def agregar(self, detalle: DetallePedido) -> DetallePedido:
        modelo = DetallePedidoModel.objects.create(
            pedido_id=detalle.id_pedido,
            plato_id=detalle.codigo_plato,
            cantidad=detalle.cantidad,
            precio_unitario=detalle.precio_unitario,
            observacion=detalle.observacion,
        )
        return self._a_entidad(modelo)

    def actualizar(self, detalle: DetallePedido) -> DetallePedido:
        DetallePedidoModel.objects.filter(
            pedido_id=detalle.id_pedido, plato_id=detalle.codigo_plato
        ).update(
            cantidad=detalle.cantidad,
            precio_unitario=detalle.precio_unitario,
            observacion=detalle.observacion,
        )
        return detalle

    def eliminar(self, id_pedido: int, codigo_plato: str) -> None:
        DetallePedidoModel.objects.filter(
            pedido_id=id_pedido, plato_id=codigo_plato
        ).delete()