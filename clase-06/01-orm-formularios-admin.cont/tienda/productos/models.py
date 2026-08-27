from django.db import models
from categorias.models import Categoria

class Producto(models.Model):

    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=20, default="")
    descripcion = models.TextField(
        blank=True
    )
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    stock = models.PositiveIntegerField(
        default=0
    )
    activo = models.BooleanField(
        default=True
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="productos",
        null=True
    )

    def __str__(self):
        return self.nombre
