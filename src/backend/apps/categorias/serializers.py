from rest_framework import serializers
from .models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'slug', 'descripcion', 'imagen', 'activa', 'fecha_creacion']
        read_only_fields = ['id', 'fecha_creacion', 'slug']
