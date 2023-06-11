from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def saludar(request):
    return render(request,"base.html")
def despedida(request):
    return HttpResponse("hola mundo estoy en django")
def listado(request):
    return render(request,"listado.html")
                  