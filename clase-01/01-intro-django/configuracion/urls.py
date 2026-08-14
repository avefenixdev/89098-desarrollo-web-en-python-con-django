
from django.contrib import admin
from django.urls import path

from usuarios import views as usuarios_views
from productos import views as productos_views

"""
URL configuration for configuracion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
urlpatterns = [
    path("admin/", admin.site.urls),
    path("hola/", usuarios_views.hola),
    path("chau/", usuarios_views.despedirse),
    path("bienvenida/", usuarios_views.bienvenida),
    path("usuarios/<int:id>", usuarios_views.usuario),
    path("", productos_views.inicio),
    path("productos/", productos_views.productos),
    path("productos/<int:id>", productos_views.producto)
]

handler404 = "usuarios.views.pagina_404"

""" Parámetros en la URLs """
# path("usuarios/<tipo-dato:identificador>")
