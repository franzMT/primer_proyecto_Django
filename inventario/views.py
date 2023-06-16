from django.shortcuts import render
from django.http import HttpResponse
from .models import Productos
# Create your views here.


def listado(request):
    productos = Productos.objects.all()
    context = {"productos":productos}
    return render(request,"listado.html",context)
                  