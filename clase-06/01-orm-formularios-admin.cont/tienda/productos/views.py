from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def inicio(request):

    productos = Producto.objects.select_related(
        "categoria"
    ).all()

    return render(
        request, 
        'productos/index.html',
        {
            "productos": productos
        }
    )


def crear(request):

    if request.method == "POST":
        form = ProductoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("productos_app.inicio_productos") 
    
    else:
        form = ProductoForm()

    return render(
        request, 
        "productos/crear.html",
        {
            "form": form
        }
    )

def editar(request):
    return

def eliminar(request):
    return  