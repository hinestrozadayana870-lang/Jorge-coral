# URL y Vistas - Django

Proyecto de aprendizaje basado en URL y Vistas con Django.

## Pasos realizados

1. Carpeta del proyecto: `my_proyect`
2. Proyecto configurado: `my_proyect`
3. Aplicación creada: `app`
4. Aplicación registrada en `INSTALLED_APPS`
5. URLs principales conectadas con `app.urls`
6. Vista básica creada en `app/views.py`
7. Plantilla HTML creada en `templates/inicio.html`
8. Vista adicional disponible en `/saludo/`
9. Pruebas básicas incluidas en `app/tests.py`

## Instalación local

Desde la carpeta `my_proyect`:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py manage.py migrate
py manage.py runserver
```

Después abre `http://127.0.0.1:8000/`.

Para probar la segunda vista abre `http://127.0.0.1:8000/saludo/`.

## Verificar las pruebas

```powershell
py manage.py test
```
