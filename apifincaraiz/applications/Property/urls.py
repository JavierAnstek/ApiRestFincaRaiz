from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # url para el manejo de tipo de propiedades
    path('api/propertyTypes', views.PropertyTypeListAPI.as_view()),
    path('api/propertyTypes/create', views.PropertyTypeCreate.as_view()),
    path('api/propertyTypes/detail/<pk>', views.PropertyTypeDetail.as_view()),
    path('api/propertyTypes/update/<pk>', views.PropertyTypeUpdate.as_view()),
    path('api/propertyTypes/delete/<pk>', views.PropertyTypeDelete.as_view()),
    # url para el manejo de propiedades
    path('api/properties', views.PropertyListAPI.as_view()),
    path('api/properties/create', views.PropertyCreate.as_view()),
    path('api/properties/detail/<pk>', views.PropertyDetail.as_view()),
    path('api/properties/update/<pk>', views.PropertyUpdate.as_view()),
    path('api/properties/delete/<pk>', views.PropertyDelete.as_view()),
    #url para el manejo de comentarios
    path('api/reviews/<id>', views.ReviewsList.as_view()),
    path('api/reviews/create', views.ReviewsCreate.as_view()),

]