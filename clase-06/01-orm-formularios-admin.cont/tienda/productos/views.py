from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect("productos_app:inicio_productos") 
    
    else:
        form = ProductoForm()

    return render(
        request, 
        "productos/crear.html",
        {
            "form": form
        }
    )

def editar(request, id):

    producto = get_object_or_404(
        Producto,
        id=id
    )

    if request.method == 'POST':
        form = ProductoForm(
            request.POST,
            instance=producto
        )

        if form.is_valid():
            form.save()
            return redirect("productos_app:inicio_productos")
    else: # GET

        form = ProductoForm(
            instance=producto
        )

    return render(request, 'productos/editar.html', { "form": form})

def eliminar(request):
    return  