from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

def lista_productos(request):
    # return HttpResponse('Listado de productos')
    
    productos = [
        { "id": 1, "nombre": "PC", "categoria": "Informatica", "precio": 332.3 },
        { "id": 2, "nombre": "Notebook", "categoria": "Informatica", "precio": 752.3 },
        { "id": 3, "nombre": "Mouse", "categoria": "Informatica", "precio": 32.3 },
        { "id": 4, "nombre": "Monitor", "categoria": "Informatica", "precio": 104.3 }
    ]
    
    return render(request, "productos/inicio.html", { "productos": productos })