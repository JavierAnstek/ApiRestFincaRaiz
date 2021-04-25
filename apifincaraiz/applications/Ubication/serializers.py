from rest_framework import serializers, pagination
from .models import States, Cities


# paginación de registros
class StatePagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100

# el serializer se puede conectar a un modelo
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        # el modelo del cual tomará los datos
        model = States
        # los campos que vamos a serializar
        fields = ('id', 'name', 'status',)


# CIUDADES: paginación de registros
class CityPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100

# serializador que no se conecta directamente a un modelo
class CitySerializer(serializers.ModelSerializer):
    # define los campos a serializar
    # id = serializers.IntegerField()
    # name = serializers.CharField()
    # zip_code = serializers.CharField()
    # state = StateSerializer()
    # status = serializers.BooleanField()

    class Meta:
        # el modelo del cual tomará los datos
        model = Cities
        # los campos que vamos a serializar
        fields = ('id', 'name', 'zip_code', 'state', 'status',)
