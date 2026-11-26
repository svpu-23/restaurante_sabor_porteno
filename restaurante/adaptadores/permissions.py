from rest_framework.permissions import BasePermission, SAFE_METHODS


def _tiene_grupo(user, nombres_grupos: tuple[str, ...]) -> bool:
    if not user or not user.is_authenticated:
        return False
    if user.is_superuser:
        return True
    return user.groups.filter(name__in=nombres_grupos).exists()


class EsAdministrador(BasePermission):
    """Permite acceso solo a usuarios con rol Administrador o superusuario."""

    message = "Se requieren permisos de Administrador para realizar esta acción."

    def has_permission(self, request, view):
        return _tiene_grupo(request.user, ("Administrador",))


class EsPersonalRestaurante(BasePermission):
    """Permite acceso a personal autenticado (Administrador o Garzon)."""

    message = "Solo el personal autorizado del restaurante puede acceder."

    def has_permission(self, request, view):
        return _tiene_grupo(request.user, ("Administrador", "Garzon"))


class SoloAdminParaEscribir(BasePermission):
    """Lectura (GET) para todo el personal; escritura/borrado solo para Administrador."""

    message = "Solo un Administrador puede crear, modificar o eliminar este recurso."

    def has_permission(self, request, view):
        if not _tiene_grupo(request.user, ("Administrador", "Garzon")):
            return False
        if request.method in SAFE_METHODS:
            return True
        return _tiene_grupo(request.user, ("Administrador",))