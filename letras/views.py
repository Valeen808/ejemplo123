from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home (request):
    return render(request, 'letras/home.html')

def saludo (request):
    return render(request, 'letras/saludo.html')

def presentacion (request):
    return render(request, 'letras/presentacion.html')

def descripcion (request):
    return render(request, 'letras/descripcion.html')