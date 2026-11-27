from rest_framework import serializers


class DetalleAgregarSerializer(serializers.Serializer):
    codigo_plato = serializers.CharField(max_length=20)
    cantidad = serializers.IntegerField(min_value=1)
    observacion = serializers.CharField(
        max_length=255, required=False, allow_blank=True, allow_null=True
    )


class DetalleActualizarSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField(min_value=1)
    observacion = serializers.CharField(
        max_length=255, required=False, allow_blank=True, allow_null=True
    )


class DetalleRespuestaSerializer(serializers.Serializer):
    id_pedido = serializers.IntegerField(read_only=True)
    codigo_plato = serializers.CharField()
    cantidad = serializers.IntegerField()
    precio_unitario = serializers.DecimalField(max_digits=10, decimal_places=2)
    observacion = serializers.CharField(allow_null=True)

