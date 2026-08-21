from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def lista_usuarios(request):
    #return HttpResponse('Listado de usuarios')
    return render(request, "usuarios/inicio.html")