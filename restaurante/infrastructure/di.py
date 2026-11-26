from restaurante.infrastructure.repositories.mesa_repository import DjangoMesaRepository
from restaurante.infrastructure.repositories.categoria_plato_repository import (
    DjangoCategoriaPlatoRepository,
)
from restaurante.infrastructure.repositories.plato_repository import DjangoPlatoRepository
from restaurante.infrastructure.repositories.pedido_repository import DjangoPedidoRepository
from restaurante.infrastructure.repositories.detalle_pedido_repository import (
    DjangoDetallePedidoRepository,
)
from restaurante.application.use_cases.mesa_use_cases import MesaUseCases
from restaurante.application.use_cases.categoria_use_cases import CategoriaPlatoUseCases
from restaurante.application.use_cases.plato_use_cases import PlatoUseCases
from restaurante.application.use_cases.pedido_use_cases import PedidoUseCases
from restaurante.application.use_cases.detalle_pedido_use_cases import DetallePedidoUseCases


# --- Factories de Repositorios ---
def get_mesa_repository() -> DjangoMesaRepository:
    return DjangoMesaRepository()


def get_categoria_plato_repository() -> DjangoCategoriaPlatoRepository:
    return DjangoCategoriaPlatoRepository()


def get_plato_repository() -> DjangoPlatoRepository:
    return DjangoPlatoRepository()


def get_pedido_repository() -> DjangoPedidoRepository:
    return DjangoPedidoRepository()


def get_detalle_pedido_repository() -> DjangoDetallePedidoRepository:
    return DjangoDetallePedidoRepository()


# --- Factories de Casos de Uso ---
def get_mesa_use_cases() -> MesaUseCases:
    return MesaUseCases(get_mesa_repository())


def get_categoria_use_cases() -> CategoriaPlatoUseCases:
    return CategoriaPlatoUseCases(get_categoria_plato_repository())


def get_plato_use_cases() -> PlatoUseCases:
    return PlatoUseCases(get_plato_repository(), get_categoria_plato_repository())


def get_pedido_use_cases() -> PedidoUseCases:
    return PedidoUseCases(
        get_pedido_repository(),
        get_mesa_repository(),
        get_detalle_pedido_repository(),
    )


def get_detalle_pedido_use_cases() -> DetallePedidoUseCases:
    return DetallePedidoUseCases(
        get_detalle_pedido_repository(),
        get_pedido_repository(),
        get_plato_repository(),
    )