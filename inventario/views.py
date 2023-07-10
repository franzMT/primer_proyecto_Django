from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Productos,Categoria
# Create your views here.


def listado(request):
    productos = Productos.objects.all()
    categorias = Categoria.objects.all()
    context = {"productos":productos,"categorias":categorias}
    return render(request,"listado.html",context)

def crearProducto(request):
    nombre=request.POST["nombre"]
    precio=request.POST["precio"]
    stock=request.POST["stock"]
    categoria_id=request.POST["categoria"]
    categoria=Categoria.objects.get(id=categoria_id) 
    producto=Productos(nombre=nombre,precio=precio,stock=stock,categoria=categoria)
    producto.save()
    return redirect("/")

def eliminarProducto(request,id_producto):
    producto = Productos.objects.get(id=id_producto)
    producto.delete()
    return redirect("/")

def editarProducto(request,id_producto):
    producto = Productos.objects.get(id=id_producto)
    categorias = Categoria.objects.all()
    if request.method == "GET":
        context = {"producto":producto,"categorias":categorias}
        return render(request,"editar.html",context)
    elif request.method == "POST":
        #capturo datos 
        nuevo_nombre = request.POST["nombre"]
        nuevo_precio = request.POST["precio"]
        nuevo_stock = request.POST["stock"]
        categoria_id=request.POST["categoria"]
        categoria=Categoria.objects.get(id=categoria_id)
        #asignar nuevo valor
        producto.nombre = nuevo_nombre
        producto.precio = nuevo_precio
        producto.stock = nuevo_stock
        producto.categoria = categoria
        #guardar
        producto.save()
        return redirect("/")