from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Propietario, Mecanico, Vehiculo, Reparacion

def index(request):
    return  render(request, 'index.html')


def listaPropietarios(request):
    propietarios = Propietario.objects.order_by('nombre')
    nombre_dni_propietarios = ', '.join([propietario.nombre + ' (' + propietario.dni + ')' for propietario in propietarios])
    return render(request, 'listaPropietarios.html', {'propietarios': propietarios})

def detallePropietario(request, dni):
        propietario = Propietario.objects.get(dni=dni)
        vehiculos = Vehiculo.objects.filter(propietario=propietario)
        return render(request, 'detallePropietario.html', {'propietario': propietario, 'vehiculos': vehiculos});

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
    return render(request, 'listaVehiculos.html', {'vehiculos': vehiculos})

def detalleVehiculo(request, matricula):
    try:
        vehiculo = Vehiculo.objects.get(matricula=matricula)
        reparaciones = Reparacion.objects.filter(vehiculo=vehiculo)
        return render(request, 'detalleVehiculo.html', {'vehiculo': vehiculo, 'reparaciones': reparaciones})
    except Vehiculo.DoesNotExist:
        return HttpResponseNotFound('No existe el vehículo con la matrícula proporcionada.')

def listaReparaciones(request):
    reparaciones = Reparacion.objects.order_by('id')
    return render(request, 'listaReparaciones.html', {'reparaciones': reparaciones})

def detalleReparacion(request, id):
    try:
        reparacion = Reparacion.objects.get(id=id)
        return render(request, 'detalleReparacion.html', {'reparacion': reparacion})
    except Reparacion.DoesNotExist:
        return HttpResponseNotFound('No existe la reparación con el identificador proporcionado.')
        