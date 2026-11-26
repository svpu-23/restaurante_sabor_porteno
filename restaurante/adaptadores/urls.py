from django.urls import path
from restaurante.adaptadores.views.auth_views import (
    CsrfTokenView,
    LoginView,
    LogoutView,
    PerfilUsuarioView,
)

urlpatterns = [
    path("auth/csrf/", CsrfTokenView.as_view(), name="auth-csrf"),
    path("auth/login/", LoginView.as_view(), name="auth-login"),
    path("auth/logout/", LogoutView.as_view(), name="auth-logout"),
    path("auth/me/", PerfilUsuarioView.as_view(), name="auth-me"),
]