from decimal import Decimal
from typing import List
from django.db import transaction
from restaurante.domain.entities.pedido import Pedido
from restaurante.domain.repositories.mesa_repository import MesaRepository
from restaurante.domain.repositories.pedido_repository import PedidoRepository
from restaurante.domain.repositories.detalle_pedido_repository import DetallePedidoRepository
from restaurante.application.exceptions import (
    DatosRestauranteInvalidosError,
    MesaNoEncontradaError,
    MesaInactivaError,
    PedidoNoEncontradoError,
    PedidoCerradoError,
    PedidoConDetallesError,
)

ESTADOS_VALIDOS = {"abierto", "cerrado", "anulado"}


class PedidoUseCases:
    def __init__(
        self,
        pedido_repo: PedidoRepository,
        mesa_repo: MesaRepository,
        detalle_repo: DetallePedidoRepository,
    ):
        self.pedido_repo = pedido_repo
        self.mesa_repo = mesa_repo
        self.detalle_repo = detalle_repo

    def listar(self) -> List[Pedido]:
        return self.pedido_repo.listar()

    def obtener_por_id(self, id_pedido: int) -> Pedido:
        pedido = self.pedido_repo.obtener_por_id(id_pedido)
        if not pedido:
            raise PedidoNoEncontradoError(f"El pedido #{id_pedido} no existe.")
        return pedido

    def crear(self, numero_mesa: int, garzon: str) -> Pedido:
        garzon_limpio = garzon.strip()
        if not garzon_limpio:
            raise DatosRestauranteInvalidosError("El nombre del garzón es obligatorio.")

        mesa = self.mesa_repo.obtener_por_numero(numero_mesa)
        if not mesa:
            raise MesaNoEncontradaError(f"La mesa número {numero_mesa} no existe.")
        if not mesa.activa:
            raise MesaInactivaError(f"La mesa número {numero_mesa} se encuentra inactiva.")

        with transaction.atomic(using="negocio"):
            nuevo_pedido = Pedido(
                numero_mesa=numero_mesa,
                garzon=garzon_limpio,
                propina=Decimal("0.00"),
                total=Decimal("0.00"),
                estado="abierto",
            )
            return self.pedido_repo.crear(nuevo_pedido)

    def actualizar(
        self,
        id_pedido: int,
        numero_mesa: int,
        garzon: str,
        propina: Decimal,
        estado: str,
    ) -> Pedido:
        pedido_actual = self.obtener_por_id(id_pedido)

        garzon_limpio = garzon.strip()
        if not garzon_limpio:
            raise DatosRestauranteInvalidosError("El nombre del garzón es obligatorio.")
        if propina < Decimal("0"):
            raise DatosRestauranteInvalidosError("La propina no puede ser negativa.")

        estado_limpio = estado.strip().lower()
        if estado_limpio not in ESTADOS_VALIDOS:
            raise DatosRestauranteInvalidosError(
                f"Estado inválido '{estado}'. Debe ser: {', '.join(sorted(ESTADOS_VALIDOS))}."
            )

        mesa = self.mesa_repo.obtener_por_numero(numero_mesa)
        if not mesa:
            raise MesaNoEncontradaError(f"La mesa número {numero_mesa} no existe.")
        if not mesa.activa:
            raise MesaInactivaError(f"La mesa número {numero_mesa} se encuentra inactiva.")

        with transaction.atomic(using="negocio"):
            detalles = self.detalle_repo.listar_por_pedido(id_pedido)
            subtotal = sum(
                (d.precio_unitario * d.cantidad for d in detalles),
                Decimal("0.00"),
            )
            pedido_actualizado = Pedido(
                id_pedido=id_pedido,
                numero_mesa=numero_mesa,
                garzon=garzon_limpio,
                fecha=pedido_actual.fecha,
                propina=propina,
                total=subtotal + propina,
                estado=estado_limpio,
            )
            return self.pedido_repo.actualizar(pedido_actualizado)

    def cerrar(self, id_pedido: int, propina_sugerida: bool = True) -> Pedido:
        pedido = self.obtener_por_id(id_pedido)
        if pedido.estado != "abierto":
            raise PedidoCerradoError(
                f"El pedido #{id_pedido} ya se encuentra en estado '{pedido.estado}'."
            )

        with transaction.atomic(using="negocio"):
            detalles = self.detalle_repo.listar_por_pedido(id_pedido)
            subtotal = sum(
                (d.precio_unitario * d.cantidad for d in detalles),
                Decimal("0.00"),
            )
            propina = (
                (subtotal * Decimal("0.10")).quantize(Decimal("0.01"))
                if propina_sugerida
                else Decimal("0.00")
            )
            pedido_cerrado = Pedido(
                id_pedido=pedido.id_pedido,
                numero_mesa=pedido.numero_mesa,
                garzon=pedido.garzon,
                fecha=pedido.fecha,
                propina=propina,
                total=subtotal + propina,
                estado="cerrado",
            )
            return self.pedido_repo.actualizar(pedido_cerrado)

    def eliminar(self, id_pedido: int) -> None:
        pedido = self.obtener_por_id(id_pedido)
        if pedido.estado == "cerrado":
            raise PedidoCerradoError(
                f"No se puede eliminar el pedido #{id_pedido} porque ya está cerrado."
            )
        if self.detalle_repo.listar_por_pedido(id_pedido):
            raise PedidoConDetallesError(
                f"No se puede eliminar el pedido #{id_pedido} porque tiene platos asociados."
            )

        with transaction.atomic(using="negocio"):
            self.pedido_repo.eliminar(id_pedido)