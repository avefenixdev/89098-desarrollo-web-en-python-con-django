from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path("", views.inicio, name="inicio_productos"),
    path("crear/", views.crear, name="crear"),
    path("editar/<int:id>/", views.editar, name="editar"),
    path("eliminar/<int:id>/", views.eliminar, name="eliminar")
]