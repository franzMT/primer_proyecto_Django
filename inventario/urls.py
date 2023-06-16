from django.contrib import admin
from django.urls import path
from inventario.views import listado
urlpatterns = [
    
    path("listado/",listado),
]