from rest_framework import status
from rest_framework.response import Response
from restaurante.application.exceptions import (
    RestauranteApplicationError,
    DatosRestauranteInvalidosError,
    MesaNoEncontradaError,
    CategoriaNoEncontradaError,
    PlatoNoEncontradoError,
    PedidoNoEncontradoError,
    DetallePedidoNoEncontradoError,
)


def responder_error_aplicacion(exc: RestauranteApplicationError) -> Response:
    if isinstance(exc, DatosRestauranteInvalidosError):
        codigo = status.HTTP_400_BAD_REQUEST
    elif isinstance(
        exc,
        (
            MesaNoEncontradaError,
            CategoriaNoEncontradaError,
            PlatoNoEncontradoError,
            PedidoNoEncontradoError,
            DetallePedidoNoEncontradoError,
        ),
    ):
        codigo = status.HTTP_404_NOT_FOUND
    else:
        codigo = status.HTTP_409_CONFLICT

    return Response({"detail": str(exc)}, status=codigo)