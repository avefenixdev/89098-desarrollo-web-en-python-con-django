from django import forms

class RegistroForm(forms.Form):

    nombre = forms.CharField()
    email = forms.EmailField()
    edad = forms.IntegerField()