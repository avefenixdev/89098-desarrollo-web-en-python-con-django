from django.shortcuts import render
from django.http import HttpResponse

def inicio_productos(request):
    #return HttpResponse('Listado de productos')
    return render(request, 'productos/index.html')