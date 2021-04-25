from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView, 
    RetrieveAPIView, 
    DestroyAPIView, 
    UpdateAPIView,
    RetrieveUpdateAPIView
)

from .models import Categories
from .serializers import CategorySerializer, CategoryPagination

# clase que retorna lista en json a la api
class CategoryListAPI(ListAPIView):
    # define el serializador a usar
    serializer_class = CategorySerializer
    # define el paginador a usar
    pagination_class = CategoryPagination
    
    # metodo que obtiene todos los registros
    def get_queryset(self):
        return Categories.objects.all()


# clase API para registrar una categoría
class CategoryCreate(CreateAPIView):
    """
    Permite la creación de registros correspondientes a categorías
    """
    # define el serializador a usar
    serializer_class = CategorySerializer


# clase API para retornar el detalle de una categoría
class CategoryDetail(RetrieveAPIView):
    """
    Retorna el detalle de una categoría
    """
    # define el serializador a usar
    serializer_class = CategorySerializer
    # modelo en el cual se va a buscar los datos
    queryset = Categories.objects.filter()


# clase de vista generica que modifica un registro
class CategoryDelete(DestroyAPIView):
     # define el serializador a usar
    serializer_class = CategorySerializer
    # modelo en el cual se va a buscar los datos
    queryset = Categories.objects.all()


# clase para recuperar y modificar un registro
class CategoryUpdate(RetrieveUpdateAPIView):
     # define el serializador a usar
    serializer_class = CategorySerializer
    # modelo en el cual se va a buscar los datos
    queryset = Categories.objects.all()