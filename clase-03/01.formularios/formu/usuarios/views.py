from django.shortcuts import render
from .forms import RegistroForm
from django.http import HttpResponse

# Create your views here.
def registro(request):

    print(request.method)

    if request.method == "POST":
        form = RegistroForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = RegistroForm()


    return render(
        request,
        "usuarios/registro.html",
        { "form": form }
    )

def guardar(request):

    if request.method == "POST":
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        edad = request.POST.get('edad')
        comentario = request.POST.get('comentario')
        pais = request.POST.get('pais')
        terminos = request.POST.get('acepto_terminos')

        print(nombre)
        print(email)
        print(edad)
        print(comentario)
        print(pais)
        print(terminos)

        return HttpResponse(f"Nombre: { nombre }, Email: {email}, Edad: {edad}, Comentario: {comentario}")

    return HttpResponse("Método no permitido")