from django.db import models


class MesaModel(models.Model):
    numero = models.AutoField(primary_key=True, db_column="numero")
    capacidad = models.IntegerField(db_column="capacidad")
    activa = models.BooleanField(default=True, db_column="activa")

    class Meta:
        managed = False
        db_table = "mesas"
        app_label = "restaurante"


class CategoriaPlatoModel(models.Model):
    id_categoria = models.AutoField(primary_key=True, db_column="id_categoria")
    nombre = models.CharField(max_length=100, unique=True, db_column="nombre")

    class Meta:
        managed = False
        db_table = "categorias_plato"
        app_label = "restaurante"


class PlatoModel(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True, db_column="codigo")
    nombre = models.CharField(max_length=100, db_column="nombre")
    categoria = models.ForeignKey(
        CategoriaPlatoModel,
        on_delete=models.DO_NOTHING,
        db_column="id_categoria",
    )
    precio = models.DecimalField(max_digits=10, decimal_places=2, db_column="precio")
    disponible = models.BooleanField(default=True, db_column="disponible")

    class Meta:
        managed = False
        db_table = "platos"
        app_label = "restaurante"


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