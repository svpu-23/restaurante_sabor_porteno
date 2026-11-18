class ErrorNegocio(Exception):
    """Excepción base para todas las reglas de negocio del restaurante."""
    pass


class EntidadNoEncontradaError(ErrorNegocio):
    """Se lanza cuando se busca un registro por ID y no existe en Oracle."""
    pass


class RegistroDuplicadoError(ErrorNegocio):
    """Se lanza al intentar crear o actualizar un registro con un dato único ya existente."""
    pass


class BorradoProtegidoError(ErrorNegocio):
    """Se lanza al intentar eliminar un registro maestro que tiene dependencias asociadas."""
    pass


class ReglaNegocioInvalidaError(ErrorNegocio):
    """Se lanza cuando un dato viola una regla del dominio (ej. precio negativo o capacidad cero)."""
    pass