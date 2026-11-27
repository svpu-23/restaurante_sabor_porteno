from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from restaurante.application.exceptions import RestauranteApplicationError
from restaurante.infrastructure.di import get_detalle_pedido_use_cases
from restaurante.adaptadores.http_errors import responder_error_aplicacion
from restaurante.adaptadores.permissions import EsPersonalRestaurante
from restaurante.adaptadores.serializers.detalle_pedido_serializer import (
    DetalleAgregarSerializer,
    DetalleActualizarSerializer,
    DetalleRespuestaSerializer,
)


class DetallePedidoListCreateView(APIView):
    permission_classes = [EsPersonalRestaurante]

    def get(self, request, id_pedido: int):
        try:
            detalles = get_detalle_pedido_use_cases().listar_por_pedido(id_pedido)
            serializer = DetalleRespuestaSerializer(detalles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except RestauranteApplicationError as exc:
            return responder_error_aplicacion(exc)

    def post(self, request, id_pedido: int):
        serializer = DetalleAgregarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        datos = serializer.validated_data

        try:
            detalle = get_detalle_pedido_use_cases().agregar(
                id_pedido=id_pedido,
                codigo_plato=datos["codigo_plato"],
                cantidad=datos["cantidad"],
                observacion=datos.get("observacion"),
            )
            return Response(
                DetalleRespuestaSerializer(detalle).data,
                status=status.HTTP_201_CREATED,
            )
        except RestauranteApplicationError as exc:
            return responder_error_aplicacion(exc)


class DetallePedidoDetailView(APIView):
    permission_classes = [EsPersonalRestaurante]

    def put(self, request, id_pedido: int, codigo_plato: str):
        serializer = DetalleActualizarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        datos = serializer.validated_data

        try:
           detalle = get_detalle_pedido_use_cases().actualizar(
                id_pedido=id_pedido,
                codigo_plato=codigo_plato,
                cantidad=datos["cantidad"],
                observacion=datos.get("observacion"),
            )
           return Response(
                DetalleRespuestaSerializer(detalle).data,
                status=status.HTTP_200_OK,
            )
        except RestauranteApplicationError as exc:
            return responder_error_aplicacion(exc)

    def delete(self, request, id_pedido: int, codigo_plato: str):
        try:
            get_detalle_pedido_use_cases().eliminar(
                id_pedido=id_pedido, codigo_plato=codigo_plato
            )
            return Response(status=status.HTTP_204_NO_CONTENT)
        except RestauranteApplicationError as exc:
            return responder_error_aplicacion(exc)