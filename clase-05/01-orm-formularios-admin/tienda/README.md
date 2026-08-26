# Desafío (Enunciado)

1. Crear el entorno

```sh
py -m venv <entorno>
py -m venv dev
```

2. Activarlo

```sh
.\Scripts\activate
```  
3. Instalar django

<https://pypi.org/>
<https://pypi.org/project/Django/>

```sh
pip install Django
``` 
4. Crear el proyecto

```sh
django-admin startproject tienda
``` 

5. Arrancar el servidor de desarrollo

```sh
py manage.py runserver
```

6. Crear las 3 Apps (productos, clientes, categorias)

```sh
django-admin startapp productos
django-admin startapp clientes
django-admin startapp categorias
```

6.1. Declarar las app en el settings.py del proyecto

```py
INSTALLED_APPS = [
    "categorias.apps.CategoriasConfig",
    "productos.apps.ProductosConfig",
    "clientes.apps.ClientesConfig"
]
```

7. Crear una vista de productos, vista de clientes, vista de categorias

8. Instalar driver postgres

```sh
pip install "psycopg[binary]"
```

9. Configurar motor de postgres en django

```py
"default": {
        "ENGINE": "django.db.backends.postgres",
        "NAME": "tienda",
        "USER": "postgres",
        "PASSWORD": "admin",
        "HOST": "localhost",
        "PORT": "5432",
}
```

# Activar el superuser para poder usar el admin nativo de django

```sh
py manage.py migrate # crea la estructura de entidades en la DB
```  

# Crear el usuario superuser

```sh
py manage.py createsuperuser
```

# En la URL 

```
localhost:8000/admin
```