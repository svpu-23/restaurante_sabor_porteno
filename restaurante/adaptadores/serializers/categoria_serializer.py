from rest_framework import serializers


class CategoriaPlatoSerializer(serializers.Serializer):
    id_categoria = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(max_length=100)