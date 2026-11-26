from django.db import models
from restaurante.infrastructure.models.pedido_model import PedidoModel
from restaurante.infrastructure.models.plato_model import PlatoModel


class DetallePedidoModel(models.Model):
    pk = models.CompositePrimaryKey("pedido", "plato")
    pedido = models.ForeignKey(
        PedidoModel,
        on_delete=models.DO_NOTHING,
        db_column="id_pedido",
    )
    plato = models.ForeignKey(
        PlatoModel,
        on_delete=models.DO_NOTHING,
        db_column="codigo_plato",
    )
    cantidad = models.IntegerField(db_column="cantidad")
    precio_unitario = models.DecimalField(
        max_digits=10, decimal_places=2, db_column="precio_unitario"
    )
    observacion = models.CharField(
        max_length=255, null=True, blank=True, db_column="observacion"
    )

    class Meta:
        managed = False
        db_table = "detalle_pedido"
        app_label = "restaurante"