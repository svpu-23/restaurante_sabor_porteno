from django.db import models
from restaurante.infrastructure.models.categoria_plato_model import CategoriaPlatoModel


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