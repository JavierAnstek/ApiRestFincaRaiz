from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/categories', views.CategoryListAPI.as_view()),
    path('api/categories/create', views.CategoryCreate.as_view()),
    path('api/categories/detail/<pk>', views.CategoryDetail.as_view()),
    path('api/categories/delete/<pk>', views.CategoryDelete.as_view()),
    path('api/categories/update/<pk>', views.CategoryUpdate.as_view()),
]
