from django.urls import path
from restaurante.adaptadores.views.auth_views import (
    CsrfTokenView,
    LoginView,
    LogoutView,
    PerfilUsuarioView,
)
from restaurante.adaptadores.views.mesa_views import MesaListCreateView, MesaDetailView
from restaurante.adaptadores.views.categoria_views import (
    CategoriaListCreateView,
    CategoriaDetailView,
)
from restaurante.adaptadores.views.plato_views import PlatoListCreateView, PlatoDetailView
from restaurante.adaptadores.views.pedido_views import (
    PedidoListCreateView,
    PedidoDetailView,
    PedidoCerrarView,
)
from restaurante.adaptadores.views.detalle_pedido_views import (
    DetallePedidoListCreateView,
    DetallePedidoDetailView,
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
    # CRUD Categorías de Plato
    path("categorias/", CategoriaListCreateView.as_view(), name="categorias-list-create"),
    path(
        "categorias/<int:id_categoria>/",
        CategoriaDetailView.as_view(),
        name="categorias-detail",
    ),
    # CRUD Platos
    path("platos/", PlatoListCreateView.as_view(), name="platos-list-create"),
    path("platos/<str:codigo>/", PlatoDetailView.as_view(), name="platos-detail"),
    # CRUD Pedidos
    path("pedidos/", PedidoListCreateView.as_view(), name="pedidos-list-create"),
    path("pedidos/<int:id_pedido>/", PedidoDetailView.as_view(), name="pedidos-detail"),
    path(
        "pedidos/<int:id_pedido>/cerrar/",
        PedidoCerrarView.as_view(),
        name="pedidos-cerrar",
    ),
    # CRUD Detalle de Pedido (PK compuesta: id_pedido + codigo_plato)
    path(
        "pedidos/<int:id_pedido>/detalles/",
        DetallePedidoListCreateView.as_view(),
        name="detalles-list-create",
    ),
    path(
        "pedidos/<int:id_pedido>/detalles/<str:codigo_plato>/",
        DetallePedidoDetailView.as_view(),
        name="detalles-detail",
    ),
]