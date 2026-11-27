from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from restaurante.application.exceptions import RestauranteApplicationError
from restaurante.infrastructure.di import get_mesa_use_cases
from restaurante.adaptadores.http_errors import responder_error_aplicacion
from restaurante.adaptadores.permissions import SoloAdminParaEscribir
from restaurante.adaptadores.serializers.mesa_serializer import MesaSerializer


class MesaListCreateView(APIView):
    permission_classes = [SoloAdminParaEscribir]

    def get(self, request):
        mesas = get_mesa_use_cases().listar()
        serializer = MesaSerializer(mesas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MesaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        datos = serializer.validated_data

        try:
            mesa = get_mesa_use_cases().crear(
                capacidad=datos["capacidad"],
                activa=datos.get("activa", True),
                numero=datos.get("numero"),
            )
            return Response(
                MesaSerializer(mesa).data, status=status.HTTP_201_CREATED
            )
        except RestauranteApplicationError as exc:
            return responder_error_aplicacion(exc)


class MesaDetailView(APIView):
    permission_classes = [SoloAdminParaEscribir]

    def get(self, request, numero: int):
        try:
            mesa = get_mesa_use_cases().obtener_por_numero(numero)
            return Response(MesaSerializer(mesa).data, status=status.HTTP_200_OK)
        except RestauranteApplicationError as exc:
            return responder_error_aplicacion(exc)

    def put(self, request, numero: int):
        serializer = MesaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        datos = serializer.validated_data

        try:
            mesa = get_mesa_use_cases().actualizar(
                numero=numero,
                capacidad=datos["capacidad"],
                activa=datos.get("activa", True),
            )
            return Response(MesaSerializer(mesa).data, status=status.HTTP_200_OK)
        except RestauranteApplicationError as exc:
            return responder_error_aplicacion(exc)

    def delete(self, request, numero: int):
        try:
            get_mesa_use_cases().eliminar(numero)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except RestauranteApplicationError as exc:
            return responder_error_aplicacion(exc)