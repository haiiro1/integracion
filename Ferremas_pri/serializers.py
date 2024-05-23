from rest_framework import serializers
from .models import Categoria, Producto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']

class ProductoSerializer(serializers.ModelSerializer):
    categorias = CategoriaSerializer(many=True, read_only=True)

    class Meta:
        model = Producto
        fields = ['id', 'codigo_producto', 'nombre', 'descripcion', 'marca', 'modelo', 'categorias', 'precio', 'stock', 'imagen']