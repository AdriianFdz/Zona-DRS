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
    return render(request, 'listaMecanicos.html', {'mecanicos': mecanicos})

def detalleMecanico(request, num_ss):
    try:
        mecanico = Mecanico.objects.get(num_ss=num_ss)
        return render(request, 'detalleMecanico.html', {'mecanico': mecanico})
    except Mecanico.DoesNotExist:
        return HttpResponseNotFound('No existe el mecánico con el número de la Seguridad Social proporcionado.')

def listaVehiculos(request):
    vehiculos = Vehiculo.objects.order_by("matricula")
    return render(request, 'listaVehiculos.html', {'vehiculos': vehiculos});

def listaReparaciones(request):
    reparaciones = Reparacion.objects.order_by('fecha_inicio')
    reparacion_info = '\n'.join([
        f"{reparacion.fecha_inicio} - {reparacion.fecha_fin} | {reparacion.vehiculo.matricula} | " +
        ", ".join([mecanico.nombre for mecanico in reparacion.mecanico.all()])
        for reparacion in reparaciones
    ])
    return HttpResponse(reparacion_info)

def detallePropietario(request, dni):
        propietario = Propietario.objects.get(dni=dni)
        return render(request, 'detallePropietario.html', {'propietario': propietario});
        