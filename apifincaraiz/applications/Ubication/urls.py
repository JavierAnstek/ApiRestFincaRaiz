from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # rutas para la gestión de estados
    path('api/states', views.StateListAPI.as_view()),
    path('api/states/create', views.StateCreate.as_view()),
    path('api/states/detail/<pk>', views.StateDetail.as_view()),
    path('api/states/update/<pk>', views.StateUpdate.as_view()),
    path('api/states/delete/<pk>', views.StateDelete.as_view()),
    # rutas para la gestión de ciudades
    path('api/cities', views.CityListAPI.as_view()),
    path('api/cities/create', views.CityCreate.as_view()),
    path('api/cities/detail/<pk>', views.CityDetail.as_view()),
    path('api/cities/update/<pk>', views.CityUpdate.as_view()),
    path('api/cities/delete/<pk>', views.CityDelete.as_view()),
]
