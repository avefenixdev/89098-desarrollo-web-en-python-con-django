from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("Bienvenidos a nuestra tienda")

def productos(request):
    return HttpResponse("Listado de productos")

def producto(request, id):
    return HttpResponse(f"Producto seleccionado: {id}")