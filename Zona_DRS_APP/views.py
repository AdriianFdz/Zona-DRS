from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Propietario, Mecanico, Vehiculo, Reparacion

def index(request):
    return  render(request, 'index.html')


def listaPropietarios(request):
    propietarios = Propietario.objects.order_by('nombre')
    nombre_dni_propietarios = ', '.join([propietario.nombre + ' (' + propietario.dni + ')' for propietario in propietarios])
    return render(request, 'listaPropietarios.html', {'propietarios': propietarios});

def listaMecanicos(request):
    mecanicos = Mecanico.objects.order_by('nombre')
    nombre_num_ss_mecanicos = ', '.join([mecanico.nombre + ' (' + mecanico.num_ss + ')' for mecanico in mecanicos])
    return HttpResponse(nombre_num_ss_mecanicos)

def listaVehiculos(request):
    vehiculos = Vehiculo.objects.order_by("matricula")
    vehiculo_matricula_modelo = ', '.join([vehiculo.matricula + ' (' + vehiculo.modelo + ')' for vehiculo in vehiculos])
    return HttpResponse(vehiculo_matricula_modelo)

def listaReparaciones(request):
    reparaciones = Reparacion.objects.order_by('fecha_inicio')
    reparacion_info = '\n'.join([
        f"{reparacion.fecha_inicio} - {reparacion.fecha_fin} | {reparacion.vehiculo.matricula} | " +
        ", ".join([mecanico.nombre for mecanico in reparacion.mecanico.all()])
        for reparacion in reparaciones
    ])
    return HttpResponse(reparacion_info)

def detallePropietario(request, dni):
        propietario = Propietario.objects.get(pk=dni)
        return render(request, 'detallePropietario.html', {'propietario': propietario});
        