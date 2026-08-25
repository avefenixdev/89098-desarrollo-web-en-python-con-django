from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio_clientes(request):
    # return HttpResponse('Listado de clientes')
    return render(request, 'clientes/index.html')