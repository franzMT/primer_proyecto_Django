from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Productos
# Create your views here.


def listado(request):
    productos = Productos.objects.all()
    context = {"productos":productos}
    return render(request,"listado.html",context)

def crearProducto(request):
    nombre=request.POST["nombre"]
    precio=request.POST["precio"]
    stock=request.POST["stock"]
    producto=Productos(nombre=nombre,precio=precio,stock=stock)
    producto.save()
    return redirect("/")