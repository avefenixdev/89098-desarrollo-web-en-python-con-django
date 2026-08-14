from django.shortcuts import render
from django.http import HttpResponse

def hola(request):
    return HttpResponse("Hola desde Django")
# Create your views here.

def despedirse(request):
    return HttpResponse("Chau chau chau...")

def bienvenida(request):
    return HttpResponse("Bienvenido a nuestra aplicación")

def usuario(request, id):
    return HttpResponse(f"Usuario recibido: {id}")

def pagina_404(request, exception):
    return HttpResponse("La página que estás buscando no existe.", status=404)