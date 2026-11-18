from typing import List, Optional
from restaurante.domain.entities import Mesa
from restaurante.domain.repositories import MesaRepository
from restaurante.domain.exceptions import (
    EntidadNoEncontradaError,
    RegistroDuplicadoError,
    BorradoProtegidoError,
    ReglaNegocioInvalidaError,
)


class MesaUseCases:
    def __init__(self, mesa_repo: MesaRepository):
        self.mesa_repo = mesa_repo

    def listar(self) -> List[Mesa]:
        return self.mesa_repo.listar()

    def obtener_por_numero(self, numero: int) -> Mesa:
        mesa = self.mesa_repo.obtener_por_numero(numero)
        if not mesa:
            raise EntidadNoEncontradaError(f"La mesa número {numero} no existe.")
        return mesa

    def crear(self, capacidad: int, activa: bool = True, numero: Optional[int] = None) -> Mesa:
        if capacidad <= 0:
            raise ReglaNegocioInvalidaError("La capacidad de la mesa debe ser mayor a 0.")

        if numero is not None:
            if numero <= 0:
                raise ReglaNegocioInvalidaError("El número de mesa debe ser mayor a 0.")
            if self.mesa_repo.obtener_por_numero(numero):
                raise RegistroDuplicadoError(f"Ya existe una mesa con el número {numero}.")

        nueva_mesa = Mesa(capacidad=capacidad, activa=activa, numero=numero)
        return self.mesa_repo.crear(nueva_mesa)

    def actualizar(self, numero: int, capacidad: int, activa: bool) -> Mesa:
        self.obtener_por_numero(numero)

        if capacidad <= 0:
            raise ReglaNegocioInvalidaError("La capacidad de la mesa debe ser mayor a 0.")

        mesa_actualizada = Mesa(numero=numero, capacidad=capacidad, activa=activa)
        return self.mesa_repo.actualizar(mesa_actualizada)

    def eliminar(self, numero: int) -> None:
        self.obtener_por_numero(numero)

        if self.mesa_repo.tiene_pedidos(numero):
            raise BorradoProtegidoError(
                f"No se puede eliminar la mesa {numero} porque tiene pedidos registrados."
            )

        self.mesa_repo.eliminar(numero)