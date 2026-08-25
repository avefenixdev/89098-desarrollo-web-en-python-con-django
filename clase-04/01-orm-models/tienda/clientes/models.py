from django.db import models

# Modelos tienen que estar en mayúscula y en singular (Django -> le agrega según corresponda el plural)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    edad = models.IntegerField()
    fecha_registro = models.DateField()
    
    """ toString -> Definir como se va representar el contenido del objeto"""
    def __str__(self): 
        return f"{self.nombre} {self.apellido}"