from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return HttpResponse("<h1>Hola Django</h1>")

def inicio_html(request):
    return HttpResponse("""
    <!DOCTYPE html>
        <html>
        <head>
            <title>Mi sitio</title>
        </head>
        <body>
            <h1>Bienvenido</h1>
            <p>Esta es mi página principal.</p>
        </body>
    </html>
    """)

""" Para evitar mezclar html con python (django) usamos templates """

""" Un Template, no ayuda a construir de manera
dinamica los documentos html """

def inicio_template(request):
    """ Pasando información a la vista """
    usuarios = [
        { "nombre": "Luis", "edad": 25 },
        { "nombre": "Laura", "edad": 30 }
    ]
    """ django -> Es un motor de plantillas """
    """ https://docs.djangoproject.com/en/6.0/topics/templates/ """
    return render(request, "inicio.html", { "usuarios": usuarios })
    