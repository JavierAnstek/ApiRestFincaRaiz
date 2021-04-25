from rest_framework import serializers, pagination

# importa los serializadores a usar
from applications.Ubication.serializers import CitySerializer
from applications.Category.serializers import CategorySerializer
# importa los modelos a usar
from .models import PropertiesTypes, Properties, Reviews

# TIPOS DE PROPIEDADES: paginación de registros
class PropertyTypePagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100


# Serializador para el modelo Tipo de Propiedades
class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        # el modelo del cual tomará los datos
        model = PropertiesTypes
        # los campos que vamos a serializar
        fields = ('id', 'name', 'status',)


# PROPIEDADES: paginación de registros
class PropertyPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100


# Serializador para el modelo propiedades
class PropertySerializer(serializers.ModelSerializer):
    # city = CitySerializer()
    # category = CategorySerializer()
    # property_types = PropertyTypeSerializer()

    class Meta:
        # el modelo del cual tomará los datos
        model = Properties
        # los campos que vamos a serializar
        fields = ('id', 'titulo', 'image', 'price', 'transaction_type',
        'baths', 'beds', 'sqrt', 'city', 'category', 'property_types',  'status',)


# REVIEWS: Paginación para comentarios
class ReviewPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100


# Serializador para el modelo comentarios
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        # el modelo del cual tomará los datos
        model = Reviews
        # los campos que vamos a serializar
        fields = ('id', 'feedbak', 'rating', 'avatar', 'property_id', 'create_at', )
