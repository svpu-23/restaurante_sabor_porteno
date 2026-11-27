from rest_framework import serializers


class MesaSerializer(serializers.Serializer):
    numero = serializers.IntegerField(required=False, allow_null=True, min_value=1)
    capacidad = serializers.IntegerField(min_value=1)
    activa = serializers.BooleanField(default=True)