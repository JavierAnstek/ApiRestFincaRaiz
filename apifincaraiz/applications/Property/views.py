from django.shortcuts import render
# importa las vistas genéricas
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
    PropertyTypeSerializer, 
    PropertyTypePagination, 
    PropertySerializer,
    PropertyPagination,
    ReviewSerializer,
    ReviewPagination
)
# importa los modelos
from .models import PropertiesTypes, Properties, Reviews

"""
***************************************************************************
*********   VISTAS GENERICAS PARA EL MODELO TIPOS DE PROPIEDADES   ********
***************************************************************************
"""
# clase que retorna lista en json a la api
class PropertyTypeListAPI(ListAPIView):
    """
    Retorna el listado de todas los tipos de propiedades
    """
    # define el serializador a usar
    serializer_class = PropertyTypeSerializer
    # define el serializador de la páginación
    pagination_class = PropertyTypePagination

    # metodo que obtiene todos los registros
    def get_queryset(self):
        return PropertiesTypes.objects.all()


# clase API para registrar un tipo de propiedad
class PropertyTypeCreate(CreateAPIView):
    """
    Permite la creación de registros correspondientes a tipos de propiedades
    """
    # define el serializador a usar
    serializer_class = PropertyTypeSerializer


# clase API para retornar el detalle de un tipo de propiedad
class PropertyTypeDetail(RetrieveAPIView):
    """
    Retorna el detalle de un tipo de propiedad
    """
    # define el serializador a usar
    serializer_class = PropertyTypeSerializer
    # modelo en el cual se va a buscar los datos
    queryset = PropertiesTypes.objects.filter()


# clase para recuperar y modificar un registro
class PropertyTypeUpdate(RetrieveUpdateAPIView):
     # define el serializador a usar
    serializer_class = PropertyTypeSerializer
    # modelo en el cual se va a buscar los datos
    queryset = PropertiesTypes.objects.all()


# clase de vista generica que elimina un registro
class PropertyTypeDelete(DestroyAPIView):
     # define el serializador a usar
    serializer_class = PropertyTypeSerializer
    # modelo en el cual se va a buscar los datos
    queryset = PropertiesTypes.objects.all()


"""
*********************************************************************
*********   VISTAS GENERICAS PARA EL MODELO DE PROPIEDADES   ********
*********************************************************************
"""
# clase que retorna lista en json a la api
class PropertyListAPI(ListAPIView):
    """
    Retorna el listado de todas los tipos de propiedades
    """
    # define el serializador a usar
    serializer_class = PropertySerializer
    # define el serializador de la páginación
    pagination_class = PropertyPagination

    # metodo que obtiene todos los registros
    def get_queryset(self):
        return Properties.objects.all()


# clase API para registrar una propiedad
class PropertyCreate(CreateAPIView):
    """
    Permite la creación de registros correspondientes a propiedades
    """
    # define el serializador a usar
    serializer_class = PropertySerializer


# clase API para retornar el detalle de una propiedad
class PropertyDetail(RetrieveAPIView):
    """
    Retorna el detalle de una categoría
    """
    # define el serializador a usar
    serializer_class = PropertySerializer
    # modelo en el cual se va a buscar los datos
    queryset = Properties.objects.filter()


# clase de vista generica que modifica un registro
class PropertyDelete(DestroyAPIView):
     # define el serializador a usar
    serializer_class = PropertySerializer
    # modelo en el cual se va a buscar los datos
    queryset = Properties.objects.all()


# clase para recuperar y modificar un registro
class PropertyUpdate(RetrieveUpdateAPIView):
     # define el serializador a usar
    serializer_class = PropertySerializer
    # modelo en el cual se va a buscar los datos
    queryset = Properties.objects.all()


"""
****************************************************************
*********   VISTAS GENERICAS PARA EL MODELO DE REVIEW   ********
****************************************************************
"""
# clase API para retornar el detalle de una propiedad
class ReviewsList(ListAPIView):
    """
    Retorna el listado de todas los comentarios correspondientes a una propiedad
    """
    # define el serializador a usar
    serializer_class = ReviewSerializer
    # define el serializador de la páginación
    pagination_class = ReviewPagination

    # metodo que obtiene todos los registros
    def get_queryset(self):
        id = self.kwargs['id']
        return Reviews.objects.filter(property_id=id)
    

# clase API para registrar un comentario
class ReviewsCreate(CreateAPIView):
    """
    Permite la creación de registros correspondientes a comentarios
    """
    # define el serializador a usar
    serializer_class = ReviewSerializer
