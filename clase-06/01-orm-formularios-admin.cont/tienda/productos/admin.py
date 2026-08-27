from django.contrib import admin
from .models import Producto

@admin.register(Producto)
# admin.site.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display=['nombre', 'stock', 'precio']