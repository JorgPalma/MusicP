from dataclasses import field
from .models import Producto
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):

    marca = serializers.CharField(read_only=True, source="marca.marca")
    categoria = serializers.CharField(read_only=True, source="categoria.categoria")
    subcategoria = serializers.CharField(read_only=True, source="subcategoria.subcategoria")
    class Meta:
        model = Producto
        fields = '__all__'