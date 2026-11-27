
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from restaurante.application.exceptions import RestauranteApplicationError
from restaurante.infrastructure.di import get_categoria_use_cases
from restaurante.adaptadores.http_errors import responder_error_aplicacion
from restaurante.adaptadores.permissions import SoloAdminParaEscribir
from restaurante.adaptadores.serializers.categoria_serializer import (
    CategoriaPlatoSerializer,
)


class CategoriaListCreateView(APIView):
    permission_classes = [SoloAdminParaEscribir]

    def get(self, request):
        categorias = get_categoria_use_cases().listar()
        serializer = CategoriaPlatoSerializer(categorias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategoriaPlatoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            categoria = get_categoria_use_cases().crear(
                nombre=serializer.validated_data["nombre"]
            )
            return Response(
                CategoriaPlatoSerializer(categoria).data,
                status=status.HTTP_201_CREATED,
            )
        except RestauranteApplicationError as exc:
            return responder_error_aplicacion(exc)


class CategoriaDetailView(APIView):
    permission_classes = [SoloAdminParaEscribir]

    def get(self, request, id_categoria: int):
        try:
            categoria = get_categoria_use_cases().obtener_por_id(id_categoria)
            return Response(
                CategoriaPlatoSerializer(categoria).data,
                status=status.HTTP_200_OK,
            )
        except RestauranteApplicationError as exc:
            return responder_error_aplicacion(exc)

    def put(self, request, id_categoria: int):
        serializer = CategoriaPlatoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            categoria = get_categoria_use_cases().actualizar(
                id_categoria=id_categoria,
                nombre=serializer.validated_data["nombre"],
            )
            return Response(
                CategoriaPlatoSerializer(categoria).data,
                status=status.HTTP_200_OK,
            )
        except RestauranteApplicationError as exc:
            return responder_error_aplicacion(exc)

    def delete(self, request, id_categoria: int):
        try:
            get_categoria_use_cases().eliminar(id_categoria)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except RestauranteApplicationError as exc:
            return responder_error_aplicacion(exc)
