from django.http import HttpResponse
from django.shortcuts import render


def inicio(request):
    return render(request, "inicio.html")


def saludo(request):
    return HttpResponse("Hola, esta es una vista de Django.")
