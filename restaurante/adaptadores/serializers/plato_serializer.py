from decimal import Decimal
from rest_framework import serializers


class PlatoSerializer(serializers.Serializer):
    codigo = serializers.CharField(max_length=20)
    nombre = serializers.CharField(max_length=100)
    id_categoria = serializers.IntegerField(min_value=1)
    precio = serializers.DecimalField(
        max_digits=10, decimal_places=2, min_value=Decimal("0.00")
    )
    disponible = serializers.BooleanField(default=True)
