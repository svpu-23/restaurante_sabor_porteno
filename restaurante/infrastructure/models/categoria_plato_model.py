from django.db import models


class CategoriaPlatoModel(models.Model):
    id_categoria = models.AutoField(primary_key=True, db_column="id_categoria")
    nombre = models.CharField(max_length=100, unique=True, db_column="nombre")

    class Meta:
        managed = False
        db_table = "categorias_plato"
        app_label = "restaurante"