from django.conf import settings
from django.contrib.auth import authenticate
from django.middleware.csrf import get_token
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from restaurante.adaptadores.serializers.auth_serializer import LoginSerializer


class CsrfTokenView(APIView):
    """Entrega un token CSRF inicial para clientes frontend."""

    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request):
        return Response({"csrfToken": get_token(request)}, status=status.HTTP_200_OK)


class LoginView(APIView):
    """Valida credenciales en SQLite y guarda el JWT en una cookie HttpOnly."""

    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        user = authenticate(request, username=username, password=password)
        if user is None:
            return Response(
                {"detail": "Usuario o contraseña incorrectos."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if not user.is_active:
            return Response(
                {"detail": "La cuenta de usuario está desactivada."},
                status=status.HTTP_403_FORBIDDEN,
            )

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        csrf_token = get_token(request)
        roles = list(user.groups.values_list("name", flat=True))

        response = Response(
            {
                "mensaje": "Inicio de sesión exitoso.",
                "usuario": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "roles": roles,
                    "es_admin": user.is_superuser or "Administrador" in roles,
                },
                "csrfToken": csrf_token,
            },
            status=status.HTTP_200_OK,
        )

        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            samesite="Lax",
            secure=not settings.DEBUG,
            max_age=7200,
            path="/",
        )
        return response


class LogoutView(APIView):
    """Cierra la sesión eliminando la cookie HttpOnly."""

    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        response = Response(
            {"mensaje": "Sesión cerrada correctamente."},
            status=status.HTTP_200_OK,
        )
        response.delete_cookie("access_token", path="/")
        return response


class PerfilUsuarioView(APIView):
    """Devuelve los datos del usuario autenticado actualmente."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        roles = list(user.groups.values_list("name", flat=True))
        return Response(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "roles": roles,
                "es_admin": user.is_superuser or "Administrador" in roles,
            },
            status=status.HTTP_200_OK,
        )