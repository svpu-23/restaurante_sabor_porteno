class RestauranteApplicationError(Exception):
    """Excepción base para errores de aplicación en Restaurante Sabor Porteño."""
    pass


class DatosRestauranteInvalidosError(RestauranteApplicationError):
    """Se lanza cuando los datos ingresados no cumplen las reglas del negocio."""
    pass


# --- Excepciones de Mesas ---
class MesaNoEncontradaError(RestauranteApplicationError):
    pass


class MesaDuplicadaError(RestauranteApplicationError):
    pass


class MesaConPedidosError(RestauranteApplicationError):
    pass


class MesaInactivaError(RestauranteApplicationError):
    pass


# --- Excepciones de Categorías de Plato ---
class CategoriaNoEncontradaError(RestauranteApplicationError):
    pass


class CategoriaDuplicadaError(RestauranteApplicationError):
    pass


class CategoriaConPlatosError(RestauranteApplicationError):
    pass


# --- Excepciones de Platos ---
class PlatoNoEncontradoError(RestauranteApplicationError):
    pass


class PlatoDuplicadoError(RestauranteApplicationError):
    pass


class PlatoEnPedidosError(RestauranteApplicationError):
    pass


class PlatoNoDisponibleError(RestauranteApplicationError):
    pass


# --- Excepciones de Pedidos y Detalle ---
class PedidoNoEncontradoError(RestauranteApplicationError):
    pass


class PedidoCerradoError(RestauranteApplicationError):
    pass


class PedidoConDetallesError(RestauranteApplicationError):
    pass


class DetallePedidoNoEncontradoError(RestauranteApplicationError):
    pass


class DetallePedidoDuplicadoError(RestauranteApplicationError):
    pass