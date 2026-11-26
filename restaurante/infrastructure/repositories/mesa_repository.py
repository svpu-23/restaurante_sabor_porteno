from typing import List, Optional
from restaurante.domain.entities.mesa import Mesa
from restaurante.domain.repositories.mesa_repository import MesaRepository
from restaurante.infrastructure.models.mesa_model import MesaModel
from restaurante.infrastructure.models.pedido_model import PedidoModel


class DjangoMesaRepository(MesaRepository):
    def _a_entidad(self, modelo: MesaModel) -> Mesa:
        return Mesa(
            numero=modelo.numero,
            capacidad=modelo.capacidad,
            activa=bool(modelo.activa),
        )

    def listar(self) -> List[Mesa]:
        return [self._a_entidad(m) for m in MesaModel.objects.all().order_by("numero")]

    def obtener_por_numero(self, numero: int) -> Optional[Mesa]:
        modelo = MesaModel.objects.filter(numero=numero).first()
        return self._a_entidad(modelo) if modelo else None

    def crear(self, mesa: Mesa) -> Mesa:
        datos = {"capacidad": mesa.capacidad, "activa": mesa.activa}
        if mesa.numero is not None:
            datos["numero"] = mesa.numero
        modelo = MesaModel.objects.create(**datos)
        return self._a_entidad(modelo)

    def actualizar(self, mesa: Mesa) -> Mesa:
        MesaModel.objects.filter(numero=mesa.numero).update(
            capacidad=mesa.capacidad,
            activa=mesa.activa,
        )
        return mesa

    def eliminar(self, numero: int) -> None:
        MesaModel.objects.filter(numero=numero).delete()

    def tiene_pedidos(self, numero: int) -> bool:
        return PedidoModel.objects.filter(mesa_id=numero).exists()