# Pasos para crear una App DJANGO

1. Creamos el entorno

```sh
py -m venv <nombre-entorno>
py -m venv dev
```

2. Activamos el entorno

```sh
.\Scripts\activate
```  

3. Instalamos DJANGO

```sh
pip install django
```

4. Creamos el proyecto

```sh
django-admin startproject <nombre-proyecto>
django-admin startproject tienda
```

5. Nos movimos al directorio tienda

```sh
cd tienda/
```

6. Dentro de la carpeta tienda.

```sh
py manage.py startapp <nombre-de-la-app>
py manage.py startapp productos
py manage.py startapp clientes
```

7. Arrancamos el servidor de desarrollo

```sh
py manage.py runserver
```

# .gitignore 

<https://gist.github.com/santoshpy/6f982faf1eacdac153ffd86a3a694239>

## Migraciones son el mecanismo que tiene Django para llevar los cambios que hacemos en nuestro modelos de Python a la estructura de base de datos.

```sh
py manage.py makemigrations # No modifica la base de datos. Solo crea el script que va a modificar la base datos
```

## Para ejecutar las migraciones

```sh
py manage.py migrate # Crea las entidades y columnas en la DB.
```

# Instalar Drivers de Postgres

<https://github.com/psycopg/psycopg/>

```sh
pip install "psycopg[binary]"
```

# Cambio el motor de DB de mi Proyecto

<https://docs.djangoproject.com/en/6.1/ref/databases/>

```py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "tienda",
        "USER": "postgres",
        "PASSWORD": "admin",
        "HOST": "localhost",
        "PORT": "5432"
    }
}
```