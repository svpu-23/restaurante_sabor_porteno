from django.urls import path
from restaurante.adaptadores.views.auth_views import (
    CsrfTokenView,
    LoginView,
    LogoutView,
    PerfilUsuarioView,
)
from restaurante.adaptadores.views.mesa_views import MesaListCreateView, MesaDetailView
from restaurante.adaptadores.views.pedido_views import (
    PedidoListCreateView,
    PedidoDetailView,
    PedidoCerrarView,
)

urlpatterns = [
    # Autenticación HttpOnly + CSRF
    path("auth/csrf/", CsrfTokenView.as_view(), name="auth-csrf"),
    path("auth/login/", LoginView.as_view(), name="auth-login"),
    path("auth/logout/", LogoutView.as_view(), name="auth-logout"),
    path("auth/me/", PerfilUsuarioView.as_view(), name="auth-me"),
    # CRUD Mesas
    path("mesas/", MesaListCreateView.as_view(), name="mesas-list-create"),
    path("mesas/<int:numero>/", MesaDetailView.as_view(), name="mesas-detail"),
    # CRUD Pedidos
    path("pedidos/", PedidoListCreateView.as_view(), name="pedidos-list-create"),
    path("pedidos/<int:id_pedido>/", PedidoDetailView.as_view(), name="pedidos-detail"),
    path(
        "pedidos/<int:id_pedido>/cerrar/",
        PedidoCerrarView.as_view(),
        name="pedidos-cerrar",
    ),
]