# Clase 01

## Creando el entorno virtual

```sh
py -m venv intro
``` 

## Activando el entorno virtual

```sh
<nombre-entorno>\Scripts\activate
intro\Scripts\activate
```

> Desactivar entorno

```sh
deactivate
```

## Instalar Django

```sh
pip install django
```

> Herramienta django-admin

```sh
django-admin --version # comprobar si teníamos funcionando django
```

## Creamos proyecto DJANGO

```sh
django-admin startproject <nombre-proyecto> <ruta>
django-admin startproject configuracion ./ # directorio actual
```

## Arrancamos el servidor de django

```sh
py manager.py runserver
```

> http://localhost:8080 

# Estructura del proyecto

> manager.py

Permite ejecutar comandos administrativos

```sh
py manager.py runserver
py manager.py migrate
py manager.py createsuperuser
``` 

> settings.py
Configuración del proyecto.


> urls.py
Me permite definir las urls de mi aplicación

> wsgi.py
Entrada para Web Server Gateway Interface

> asgi.py
Entrada ASGI, que permite trabajar con aplicaciones asíncronicas