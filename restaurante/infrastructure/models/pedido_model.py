from django.db import models
from restaurante.infrastructure.models.mesa_model import MesaModel


class PedidoModel(models.Model):
    id_pedido = models.AutoField(primary_key=True, db_column="id_pedido")
    mesa = models.ForeignKey(
        MesaModel,
        on_delete=models.DO_NOTHING,
        db_column="numero_mesa",
    )
    garzon = models.CharField(max_length=100, db_column="garzon")
    fecha = models.DateTimeField(db_column="fecha")
    propina = models.DecimalField(max_digits=10, decimal_places=2, db_column="propina")
    total = models.DecimalField(max_digits=10, decimal_places=2, db_column="total")
    estado = models.CharField(max_length=20, db_column="estado")

    class Meta:
        managed = False
        db_table = "pedidos"
        app_label = "restaurante"