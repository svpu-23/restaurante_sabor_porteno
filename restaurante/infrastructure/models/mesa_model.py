from django.db import models


class MesaModel(models.Model):
    numero = models.AutoField(primary_key=True, db_column="numero")
    capacidad = models.IntegerField(db_column="capacidad")
    activa = models.BooleanField(default=True, db_column="activa")

    class Meta:
        managed = False
        db_table = "mesas"
        app_label = "restaurante"