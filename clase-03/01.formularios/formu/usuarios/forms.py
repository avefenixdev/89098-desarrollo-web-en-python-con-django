from django import forms

class RegistroForm(forms.Form):
    """ CharField, EmailField, etc son input """
    nombre = forms.CharField(
        label="Nombre Completo",
        max_length=50,
        min_length=10,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Escriba su nombre. Ej: Luis, Juan, Laura"
            }
        )
    )
    email = forms.EmailField(
        label="Correo eléctronico"
    )
    edad = forms.IntegerField(
        label="Edad",
        min_value=18
    )
    comentario = forms.CharField(
        widget=forms.Textarea
    )
    pais = forms.ChoiceField(
        label="País de origen",
        choices=[
            ( "AR", "Argentina" ),
            ( "UY", "Uruguay"),
            ( "CL", "Chile")
        ]
    )
    acepto_terminos = forms.BooleanField(
        label="Acepto los términos y condiciones"
    )



""" 
Desafió -> Crear uno nuevo formulario de Productos

* Nombre -> Obligatorio | Máximo 100 caracteres
* Precio -> Numero decimal (averiguar) | Debe ser mayor de 0
* Stock -> Entero | No puede ser negativo
* Categoría -> Va a tener las siguientes opciones -> Electronica | Ropa | Hogar | Juguetes
* Descripción -> Textarea
* Disponible -> Checkbox

Pasos a seguir -> 

1. Crear una App
2. Crear el archivo forms.py para App
3. crear el Template de registro de productos -> templates/productos/registro.html
4. Hacer algo parecido a los Usuarios 
4.1 Tomando los valores y mostrarlos en la consola

Ejemplo de views.py de Usuarios

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

    15 minutos para realizar la tarea!
 """
