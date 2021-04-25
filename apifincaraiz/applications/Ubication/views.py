from django.shortcuts import render

# importa las vistas genericas de rest_framework
from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView, 
    RetrieveAPIView, 
    DestroyAPIView, 
    UpdateAPIView, 
    RetrieveUpdateAPIView
)

# importa los serializadores
from .serializers import (
    StateSerializer, 
    CitySerializer, 
    StatePagination, 
    CityPagination
)

# importa los modelos a usar
from .models import States, Cities

"""
**************************************************************
*********   VISTAS GENERICAS PARA EL MODELO ESTADO   *********
**************************************************************
"""
# clase que retorna lista en json a la api
class StateListAPI(ListAPIView):
    """
    Retorna el listado de todas los estados
    """
    # define el serializador a usar
    serializer_class = StateSerializer
    # define el paginador a usar
    pagination_class = StatePagination

    # metodo que obtiene todos los registros
    def get_queryset(self):
        return States.objects.all()


# clase API para registrar un Estado
class StateCreate(CreateAPIView):
    """
    Creación de estados, Permite la creación de registros correspondientes a estados
    """
    # define el serializador a usar
    serializer_class = StateSerializer


# clase API para retornar el detalle de un estado
class StateDetail(RetrieveAPIView):
    """
    Retorna el detalle de un Estado
    """
    # modelo en el cual se va a buscar los datos
    queryset = States.objects.filter()
    # define el serializador a usar
    serializer_class = StateSerializer


# clase de vista generica que modifica un registro
class StateDelete(DestroyAPIView):
     # define el serializador a usar
    serializer_class = StateSerializer
    # modelo en el cual se va a buscar los datos
    queryset = States.objects.all()


# clase para recuperar y modificar un registro
class StateUpdate(RetrieveUpdateAPIView):
     # define el serializador a usar
    serializer_class = StateSerializer
    # modelo en el cual se va a buscar los datos
    queryset = States.objects.all()


"""
****************************************************************
*********   VISTAS GENERICAS PARA EL MODELO CIUDADES   *********
****************************************************************
"""
# clase que retorna lista en json a la api
class CityListAPI(ListAPIView):
    """
    Retorna el listado de todas las ciudades
    """
    # define el serializador a usar
    serializer_class = CitySerializer
    # define el paginador a usar
    pagination_class = CityPagination

    # metodo que obtiene todos los registros
    def get_queryset(self):
        return Cities.objects.all()

# clase API para registrar una Ciudad
class CityCreate(CreateAPIView):
    """
    Permite la creación de registros correspondientes a ciudades
    """
    # define el serializador a usar
    serializer_class = CitySerializer

# clase API para retornar el detalle de una ciudad
class CityDetail(RetrieveAPIView):
    """
    Retorna el detalle de una ciudad
    """
    # define el serializador a usar
    serializer_class = CitySerializer
    # modelo en el cual se va a buscar los datos
    queryset = Cities.objects.filter()


# clase de vista generica que modifica un registro
class CityDelete(DestroyAPIView):
     # define el serializador a usar
    serializer_class = CitySerializer
    # modelo en el cual se va a buscar los datos
    queryset = Cities.objects.all()


# clase para recuperar y modificar un registro
class CityUpdate(RetrieveUpdateAPIView):
         # define el serializador a usar
    serializer_class = CitySerializer
    # modelo en el cual se va a buscar los datos
    queryset = Cities.objects.all()