from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
# admin.site.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display=['nombre', 'apellido', 'email', 'activo']
