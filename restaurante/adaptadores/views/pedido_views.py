from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from restaurante.application.exceptions import RestauranteApplicationError
from restaurante.infrastructure.di import get_pedido_use_cases
from restaurante.adaptadores.http_errors import responder_error_aplicacion
from restaurante.adaptadores.permissions import EsPersonalRestaurante
from restaurante.adaptadores.serializers.pedido_serializer import (
    PedidoCrearSerializer,
    PedidoActualizarSerializer,
    PedidoRespuestaSerializer,
)


class PedidoListCreateView(APIView):
    permission_classes = [EsPersonalRestaurante]

    def get(self, request):
        pedidos = get_pedido_use_cases().listar()
        serializer = PedidoRespuestaSerializer(pedidos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PedidoCrearSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        datos = serializer.validated_data

        try:
            pedido = get_pedido_use_cases().crear(
                numero_mesa=datos["numero_mesa"],
                garzon=datos["garzon"],
            )
            return Response(
                PedidoRespuestaSerializer(pedido).data,
                status=status.HTTP_201_CREATED,
            )
        except RestauranteApplicationError as exc:
            return responder_error_aplicacion(exc)


class PedidoDetailView(APIView):
    permission_classes = [EsPersonalRestaurante]

    def get(self, request, id_pedido: int):
        try:
            pedido = get_pedido_use_cases().obtener_por_id(id_pedido)
            return Response(
                PedidoRespuestaSerializer(pedido).data,
                status=status.HTTP_200_OK,
            )
        except RestauranteApplicationError as exc:
            return responder_error_aplicacion(exc)

    def put(self, request, id_pedido: int):
        serializer = PedidoActualizarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        datos = serializer.validated_data

        try:
            pedido = get_pedido_use_cases().actualizar(
                id_pedido=id_pedido,
                numero_mesa=datos["numero_mesa"],
                garzon=datos["garzon"],
                propina=datos["propina"],
                estado=datos["estado"],
            )
            return Response(
                PedidoRespuestaSerializer(pedido).data,
                status=status.HTTP_200_OK,
            )
        except RestauranteApplicationError as exc:
            return responder_error_aplicacion(exc)

    def delete(self, request, id_pedido: int):
        try:
            get_pedido_use_cases().eliminar(id_pedido)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except RestauranteApplicationError as exc:
            return responder_error_aplicacion(exc)


class PedidoCerrarView(APIView):
    """Cierra un pedido abierto y calcula el 10% de propina sugerida."""

    permission_classes = [EsPersonalRestaurante]

    def post(self, request, id_pedido: int):
        propina_sugerida = bool(request.data.get("propina_sugerida", True))
        try:
            pedido = get_pedido_use_cases().cerrar(
                id_pedido=id_pedido, propina_sugerida=propina_sugerida
            )
            return Response(
                PedidoRespuestaSerializer(pedido).data,
                status=status.HTTP_200_OK,
            )
        except RestauranteApplicationError as exc:
            return responder_error_aplicacion(exc)