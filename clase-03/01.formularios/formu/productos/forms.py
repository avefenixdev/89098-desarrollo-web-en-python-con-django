from django import forms
""" 
* Nombre -> Obligatorio | Máximo 100 caracteres
* Precio -> Numero decimal (averiguar) | Debe ser mayor de 0
* Stock -> Entero | No puede ser negativo
* Categoría -> Va a tener las siguientes opciones -> Electronica | Ropa | Hogar | Juguetes
* Descripción -> Textarea
* Disponible -> Checkbox 
"""

class RegistroFormProductos(forms.Form):
    """ CharField, EmailField, etc son input """
    nombre = forms.CharField(
        label="Nombre Completo",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Escriba su nombre. Ej: Luis, Juan, Laura"
            }
        )
    )
    precio = forms.DecimalField(
        min_value=1
    )
    stock = forms.IntegerField(
        label="Stock",
        min_value=0
    )
    categoria = forms.ChoiceField(
        choices=[
            ( "ELECTRO", "Electronica" ),
            ( "R", "Ropa"),
            ( "H", "Hogar"),
            ( "J", "Juguetes")
        ]
    )
    descripcion = forms.CharField(
        label="Descripción",
        widget=forms.Textarea
    )
    disponible = forms.BooleanField(
        label="Disponible"
    )