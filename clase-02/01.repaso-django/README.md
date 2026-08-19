# Clase 02 

# Iniciando un desarrollo con DJANGO

## Creamos el entorno

```sh
py -m venv <nombre-entorno>
py -m venv app
```

## Activamos el entorno

```sh
.\Scripts\activate
```

## Ver si tenemos activo un entorno virtual

```sh
echo $env:VIRTUAL_ENV
``` 

```sh
python -c "import sys; print(sys.prefix != sys.base_prefix)" # True -> Si tengo entorno
```

## Instalamos DJANGO

```sh
pip install django
```

## Chequear django y version

```sh
django-admin --version
```

## Arrancar el servidor de desarrollo

```sh
py manage.py runserver
```

## Crear un proyecto

```sh
django-admin startproject <nombre-proyecto>
django-admin startproject repaso
```

## Crear un app

```sh
django-admin startapp <nombre-app>
django-admin startapp <prueba>