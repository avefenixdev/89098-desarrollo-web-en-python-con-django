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