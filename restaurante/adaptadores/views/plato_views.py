
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from restaurante.application.exceptions import RestauranteApplicationError
from restaurante.infrastructure.di import get_plato_use_cases
from restaurante.adaptadores.http_errors import responder_error_aplicacion
from restaurante.adaptadores.permissions import SoloAdminParaEscribir
from restaurante.adaptadores.serializers.plato_serializer import PlatoSerializer


class PlatoListCreateView(APIView):
    permission_classes = [SoloAdminParaEscribir]

    def get(self, request):
        platos = get_plato_use_cases().listar()
        serializer = PlatoSerializer(platos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PlatoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        datos = serializer.validated_data

        try:
            plato = get_plato_use_cases().crear(
                codigo=datos["codigo"],
                nombre=datos["nombre"],
                id_categoria=datos["id_categoria"],
                precio=datos["precio"],
                disponible=datos.get("disponible", True),
            )
            return Response(
                PlatoSerializer(plato).data, status=status.HTTP_201_CREATED
            )
        except RestauranteApplicationError as exc:
            return responder_error_aplicacion(exc)


class PlatoDetailView(APIView):
    permission_classes = [SoloAdminParaEscribir]

    def get(self, request, codigo: str):
        try:
            plato = get_plato_use_cases().obtener_por_codigo(codigo)
            return Response(PlatoSerializer(plato).data, status=status.HTTP_200_OK)
        except RestauranteApplicationError as exc:
            return responder_error_aplicacion(exc)

    def put(self, request, codigo: str):
        serializer = PlatoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        datos = serializer.validated_data

        try:
            plato = get_plato_use_cases().actualizar(
                codigo=codigo,
                nombre=datos["nombre"],
                id_categoria=datos["id_categoria"],
                precio=datos["precio"],
                disponible=datos.get("disponible", True),
            )
            return Response(PlatoSerializer(plato).data, status=status.HTTP_200_OK)
        except RestauranteApplicationError as exc:
            return responder_error_aplicacion(exc)

    def delete(self, request, codigo: str):
        try:
            get_plato_use_cases().eliminar(codigo)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except RestauranteApplicationError as exc:
            return responder_error_aplicacion(exc)
