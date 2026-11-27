from decimal import Decimal
from rest_framework import serializers


class PedidoCrearSerializer(serializers.Serializer):
    numero_mesa = serializers.IntegerField(min_value=1)
    garzon = serializers.CharField(max_length=100)


class PedidoActualizarSerializer(serializers.Serializer):
    numero_mesa = serializers.IntegerField(min_value=1)
    garzon = serializers.CharField(max_length=100)
    propina = serializers.DecimalField(
        max_digits=10, decimal_places=2, min_value=Decimal("0.00")
    )
    estado = serializers.ChoiceField(choices=["abierto", "cerrado", "anulado"])


class PedidoRespuestaSerializer(serializers.Serializer):
    id_pedido = serializers.IntegerField(read_only=True)
    numero_mesa = serializers.IntegerField()
    garzon = serializers.CharField()
    fecha = serializers.DateTimeField(allow_null=True)
    propina = serializers.DecimalField(max_digits=10, decimal_places=2)
    total = serializers.DecimalField(max_digits=10, decimal_places=2)
    estado = serializers.CharField()