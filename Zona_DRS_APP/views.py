from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Propietario, Mecanico, Vehiculo, Reparacion

def index(request):
    return HttpResponse('primera vista')


def listaPropietarios(request):
    propietarios = Propietario.objects.order_by('nombre')
    nombre_dni_propietarios = ', '.join([propietario.nombre + ' (' + propietario.dni + ')' for propietario in propietarios])
    return HttpResponse(nombre_dni_propietarios)