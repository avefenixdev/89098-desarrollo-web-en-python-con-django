# Arranco un proyecto django

```sh
py -m venv <nombre-entorno>
py -m venv formu
```

## Activamos el entorno

```sh
.\Scripts\activate
```  

## Instalamos django dentro del entorno

```sh
pip install django
```

## Verificabamos que tuvieramos django

```sh
django-admin --version
```

## Creamos el proyecto

```sh
django-admin startproject desarrollo ./
```

## Arrancamos el servidor de desarrollo

```sh
py manage.py runserver
```

## Creamos una app

```sh
py manage.py startapp usuarios
```
