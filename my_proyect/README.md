# URL y Vistas - Django

Proyecto de aprendizaje para trabajar URL y Vistas con Django, siguiendo los pasos de la guía.

## Pasos del ejercicio

1. Crear la carpeta `my_proyect`.
2. Abrir la carpeta con VS Code.
3. Crear el entorno virtual `.venv`.
4. Instalar Django.
5. Crear el proyecto Django `my_proyect`.
6. Registrar la aplicación `app`.
7. Verificar la estructura del proyecto.
8. Ejecutar el servidor.
9. Crear la aplicación `app`.
10. Crear una vista básica.

## Estructura

```text
my_proyect/
├── manage.py
├── requirements.txt
├── .gitignore
├── my_proyect/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│       └── __init__.py
└── templates/
    └── inicio.html
```

## Instalación y ejecución

Desde la carpeta `my_proyect`:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py manage.py migrate
py manage.py runserver
```

Después abre en el navegador:

```text
http://127.0.0.1:8000/
```

La URL principal está conectada con la vista `inicio` de `app/views.py` y muestra la plantilla `templates/inicio.html`.

## Pruebas

Para comprobar la vista básica:

```powershell
py manage.py test
```

El entorno `.venv` se crea localmente y no se sube al repositorio porque está incluido en `.gitignore`.
