from decimal import Decimal
from typing import List, Optional
from django.db import transaction
from restaurante.domain.entities.detalle_pedido import DetallePedido
from restaurante.domain.entities.pedido import Pedido
from restaurante.domain.repositories.pedido_repository import PedidoRepository
from restaurante.domain.repositories.plato_repository import PlatoRepository
from restaurante.domain.repositories.detalle_pedido_repository import DetallePedidoRepository
from restaurante.application.exceptions import (
    DatosRestauranteInvalidosError,
    PedidoNoEncontradoError,
    PedidoCerradoError,
    PlatoNoEncontradoError,
    PlatoNoDisponibleError,
    DetallePedidoNoEncontradoError,
    DetallePedidoDuplicadoError,
)


class DetallePedidoUseCases:
    def __init__(
        self,
        detalle_repo: DetallePedidoRepository,
        pedido_repo: PedidoRepository,
        plato_repo: PlatoRepository,
    ):
        self.detalle_repo = detalle_repo
        self.pedido_repo = pedido_repo
        self.plato_repo = plato_repo

    def _recalcular_total_pedido(self, pedido: Pedido) -> None:
        detalles = self.detalle_repo.listar_por_pedido(pedido.id_pedido)
        subtotal = sum(
            (d.precio_unitario * d.cantidad for d in detalles),
            Decimal("0.00"),
        )
        pedido_actualizado = Pedido(
            id_pedido=pedido.id_pedido,
            numero_mesa=pedido.numero_mesa,
            garzon=pedido.garzon,
            fecha=pedido.fecha,
            propina=pedido.propina,
            total=subtotal + pedido.propina,
            estado=pedido.estado,
        )
        self.pedido_repo.actualizar(pedido_actualizado)

    def listar_por_pedido(self, id_pedido: int) -> List[DetallePedido]:
        if not self.pedido_repo.obtener_por_id(id_pedido):
            raise PedidoNoEncontradoError(f"El pedido #{id_pedido} no existe.")
        return self.detalle_repo.listar_por_pedido(id_pedido)

    def agregar(
        self,
        id_pedido: int,
        codigo_plato: str,
        cantidad: int,
        observacion: Optional[str] = None,
    ) -> DetallePedido:
        codigo_limpio = codigo_plato.strip().upper()
        if cantidad <= 0:
            raise DatosRestauranteInvalidosError("La cantidad debe ser mayor a 0.")

        pedido = self.pedido_repo.obtener_por_id(id_pedido)
        if not pedido:
            raise PedidoNoEncontradoError(f"El pedido #{id_pedido} no existe.")
        if pedido.estado != "abierto":
            raise PedidoCerradoError(
                f"No se pueden agregar platos al pedido #{id_pedido} (estado: {pedido.estado})."
            )

        plato = self.plato_repo.obtener_por_codigo(codigo_limpio)
        if not plato:
            raise PlatoNoEncontradoError(f"El plato '{codigo_limpio}' no existe.")
        if not plato.disponible:
            raise PlatoNoDisponibleError(f"El plato '{plato.nombre}' no está disponible.")

        if self.detalle_repo.obtener_por_pk(id_pedido, codigo_limpio):
            raise DetallePedidoDuplicadoError(
                f"El plato '{codigo_limpio}' ya está agregado en el pedido #{id_pedido}."
            )

        obs_limpia = observacion.strip() if observacion and observacion.strip() else None

        with transaction.atomic(using="negocio"):
            nuevo_detalle = DetallePedido(
                id_pedido=id_pedido,
                codigo_plato=codigo_limpio,
                cantidad=cantidad,
                precio_unitario=plato.precio,
                observacion=obs_limpia,
            )
            creado = self.detalle_repo.agregar(nuevo_detalle)
            self._recalcular_total_pedido(pedido)
            return creado

    def actualizar(
        self,
        id_pedido: int,
        codigo_plato: str,
        cantidad: int,
        observacion: Optional[str] = None,
    ) -> DetallePedido:
        codigo_limpio = codigo_plato.strip().upper()
        if cantidad <= 0:
            raise DatosRestauranteInvalidosError("La cantidad debe ser mayor a 0.")

        pedido = self.pedido_repo.obtener_por_id(id_pedido)
        if not pedido:
            raise PedidoNoEncontradoError(f"El pedido #{id_pedido} no existe.")
        if pedido.estado != "abierto":
            raise PedidoCerradoError(
                f"No se puede modificar el pedido #{id_pedido} (estado: {pedido.estado})."
            )

        detalle_existente = self.detalle_repo.obtener_por_pk(id_pedido, codigo_limpio)
        if not detalle_existente:
            raise DetallePedidoNoEncontradoError(
                f"El plato '{codigo_limpio}' no está registrado en el pedido #{id_pedido}."
            )

        obs_limpia = observacion.strip() if observacion and observacion.strip() else None

        with transaction.atomic(using="negocio"):
            detalle_actualizado = DetallePedido(
                id_pedido=id_pedido,
                codigo_plato=codigo_limpio,
                cantidad=cantidad,
                precio_unitario=detalle_existente.precio_unitario,
                observacion=obs_limpia,
            )
            actualizado = self.detalle_repo.actualizar(detalle_actualizado)
            self._recalcular_total_pedido(pedido)
            return actualizado

    def eliminar(self, id_pedido: int, codigo_plato: str) -> None:
        codigo_limpio = codigo_plato.strip().upper()

        pedido = self.pedido_repo.obtener_por_id(id_pedido)
        if not pedido:
            raise PedidoNoEncontradoError(f"El pedido #{id_pedido} no existe.")
        if pedido.estado != "abierto":
            raise PedidoCerradoError(
                f"No se puede modificar el pedido #{id_pedido} (estado: {pedido.estado})."
            )

        if not self.detalle_repo.obtener_por_pk(id_pedido, codigo_limpio):
            raise DetallePedidoNoEncontradoError(
                f"El plato '{codigo_limpio}' no está registrado en el pedido #{id_pedido}."
            )

        with transaction.atomic(using="negocio"):
            self.detalle_repo.eliminar(id_pedido, codigo_limpio)
            self._recalcular_total_pedido(pedido)