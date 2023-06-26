from django.contrib import admin
from django.urls import path
from inventario.views import listado,crearProducto,editarProducto,eliminarProducto

#configuracion para style de css
from django.conf import settings
from django.conf.urls.static import static

#agregar + static... para css
urlpatterns = [   
    path("",listado,name="base"),
    path("crear/",crearProducto,name="crear"),
    path("editar/<id_producto>",editarProducto,name="editar"),
    path("eliminar/<id_producto>",eliminarProducto,name="eliminar"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)