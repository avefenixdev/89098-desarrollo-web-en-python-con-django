from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = [
            "nombre",
            "categoria",
            "descripcion",
            "color",
            "stock",
            "precio"
        ]

        widgets = {

            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nombre del producto. ej: PC, Notebook"
                }
            ),

            "color": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese color del producto. ej: rojo, blanco"
                }
            ),

            "descripcion": forms.Textarea(
                attrs={
                    "class": 'form-control',
                    "rows": 4,
                    "placeholder": "Escriba un texto descriptivo del producto"
                }
            ),

            "precio": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": '1',
                    "min": "0"
                }
            ),

            "stock": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "0"
                }
            ),
            "categoria": forms.Select(
                attrs={
                    "class": "form-select"
                }
            )


        }

