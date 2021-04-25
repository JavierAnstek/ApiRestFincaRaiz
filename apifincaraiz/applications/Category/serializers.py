from rest_framework import serializers, pagination
from .models import Categories


# paginación de registros
class CategoryPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100


# el serializer se puede conectar a un modelo
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        # el modelo del cual tomará los datos
        model = Categories
        # los campos que vamos a serializar
        fields = ('id', 'name', 'status')