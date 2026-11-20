from typing import List, Optional
from restaurante.domain.entities import Mesa, CategoriaPlato, Plato
from restaurante.domain.repositories import (
    MesaRepository,
    CategoriaPlatoRepository,
    PlatoRepository,
)
from restaurante.infrastructure.models import (
    MesaModel,
    CategoriaPlatoModel,
    PlatoModel,
    PedidoModel,
    DetallePedidoModel,
)


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


class DjangoCategoriaPlatoRepository(CategoriaPlatoRepository):
    def _a_entidad(self, modelo: CategoriaPlatoModel) -> CategoriaPlato:
        return CategoriaPlato(
            id_categoria=modelo.id_categoria,
            nombre=modelo.nombre,
        )

    def listar(self) -> List[CategoriaPlato]:
        return [
            self._a_entidad(c)
            for c in CategoriaPlatoModel.objects.all().order_by("id_categoria")
        ]

    def obtener_por_id(self, id_categoria: int) -> Optional[CategoriaPlato]:
        modelo = CategoriaPlatoModel.objects.filter(id_categoria=id_categoria).first()
        return self._a_entidad(modelo) if modelo else None

    def obtener_por_nombre(self, nombre: str) -> Optional[CategoriaPlato]:
        modelo = CategoriaPlatoModel.objects.filter(nombre__iexact=nombre).first()
        return self._a_entidad(modelo) if modelo else None

    def crear(self, categoria: CategoriaPlato) -> CategoriaPlato:
        modelo = CategoriaPlatoModel.objects.create(nombre=categoria.nombre)
        return self._a_entidad(modelo)

    def actualizar(self, categoria: CategoriaPlato) -> CategoriaPlato:
        CategoriaPlatoModel.objects.filter(id_categoria=categoria.id_categoria).update(
            nombre=categoria.nombre
        )
        return categoria

    def eliminar(self, id_categoria: int) -> None:
        CategoriaPlatoModel.objects.filter(id_categoria=id_categoria).delete()

    def tiene_platos(self, id_categoria: int) -> bool:
        return PlatoModel.objects.filter(categoria_id=id_categoria).exists()


class DjangoPlatoRepository(PlatoRepository):
    def _a_entidad(self, modelo: PlatoModel) -> Plato:
        return Plato(
            codigo=modelo.codigo,
            nombre=modelo.nombre,
            id_categoria=modelo.categoria_id,
            precio=modelo.precio,
            disponible=bool(modelo.disponible),
        )

    def listar(self) -> List[Plato]:
        return [self._a_entidad(p) for p in PlatoModel.objects.all().order_by("codigo")]

    def obtener_por_codigo(self, codigo: str) -> Optional[Plato]:
        modelo = PlatoModel.objects.filter(codigo=codigo).first()
        return self._a_entidad(modelo) if modelo else None

    def obtener_por_nombre(self, nombre: str) -> Optional[Plato]:
        modelo = PlatoModel.objects.filter(nombre__iexact=nombre).first()
        return self._a_entidad(modelo) if modelo else None

    def crear(self, plato: Plato) -> Plato:
        modelo = PlatoModel.objects.create(
            codigo=plato.codigo,
            nombre=plato.nombre,
            categoria_id=plato.id_categoria,
            precio=plato.precio,
            disponible=plato.disponible,
        )
        return self._a_entidad(modelo)

    def actualizar(self, plato: Plato) -> Plato:
        PlatoModel.objects.filter(codigo=plato.codigo).update(
            nombre=plato.nombre,
            categoria_id=plato.id_categoria,
            precio=plato.precio,
            disponible=plato.disponible,
        )
        return plato

    def eliminar(self, codigo: str) -> None:
        PlatoModel.objects.filter(codigo=codigo).delete()

    def tiene_detalles(self, codigo: str) -> bool:
        return DetallePedidoModel.objects.filter(plato_id=codigo).exists()