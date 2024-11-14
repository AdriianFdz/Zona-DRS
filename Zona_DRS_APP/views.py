from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Propietario, Mecanico, Vehiculo, Reparacion
from django.views.generic import ListView, DetailView
from django.views import View  

'''
def index(request):
    return render(request, 'index.html')
'''
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


# Vistas basadas en clases

class ListaPropietariosView(ListView):
    model = Propietario
    template_name = 'listaPropietarios.html'
    context_object_name = 'propietarios'
    queryset = Propietario.objects.order_by('nombre')
    '''
    propietarios = Propietario.objects.order_by('nombre')
    nombre_dni_propietarios = ', '.join([propietario.nombre + ' (' + propietario.dni + ')' for propietario in propietarios])
    return render(request, 'listaPropietarios.html', {'propietarios': propietarios})
    '''
class DetallePropietarioView(DetailView):
    model = Propietario
    template_name = 'detallePropietario.html'
    context_object_name = 'propietario'
    '''
        propietario = Propietario.objects.get(dni=dni)
        vehiculos = Vehiculo.objects.filter(propietario=propietario).order_by('matricula')
        return render(request, 'detallePropietario.html', {'propietario': propietario, 'vehiculos': vehiculos});
    '''
class ListaMecanicosView(ListView):
    model = Mecanico
    template_name = 'listaMecanicos.html'
    context_object_name = 'mecanicos'
    queryset = Mecanico.objects.order_by('nombre')
    '''
    mecanicos = Mecanico.objects.order_by('nombre')
    return render(request, 'listaMecanicos.html', {'mecanicos': mecanicos})
    '''
class DetalleMecanicoView(DetailView):
    model = Mecanico
    template_name = 'detalleMecanico.html'
    context_object_name = 'mecanico'
    '''
    try:
        mecanico = Mecanico.objects.get(num_ss=num_ss)
        reparaciones = Reparacion.objects.filter(mecanico=mecanico).order_by('id')
        return render(request, 'detalleMecanico.html', {'mecanico': mecanico, 'reparaciones': reparaciones})
    except Mecanico.DoesNotExist:
        return HttpResponseNotFound('No existe el mecánico con el número de la Seguridad Social proporcionado.')
    '''
class ListaVehiculosView(ListView):
    model = Vehiculo
    template_name = 'listaVehiculos.html'
    context_object_name = 'vehiculos'
    queryset = Vehiculo.objects.order_by('matricula')
    '''
    vehiculos = Vehiculo.objects.order_by("matricula")
    return render(request, 'listaVehiculos.html', {'vehiculos': vehiculos})
    '''
class DetalleVehiculoView(DetailView):
    model = Vehiculo
    template_name = 'detalleVehiculo.html'
    context_object_name = 'vehiculo'
    '''
    try:
        vehiculo = Vehiculo.objects.get(matricula=matricula)
        reparaciones = Reparacion.objects.filter(vehiculo=vehiculo).order_by('id')
        return render(request, 'detalleVehiculo.html', {'vehiculo': vehiculo, 'reparaciones': reparaciones})
    except Vehiculo.DoesNotExist:
        return HttpResponseNotFound('No existe el vehículo con la matrícula proporcionada.')
    '''
class ListaReparacionesView(ListView):
    model = Reparacion
    template_name = 'listaReparaciones.html'
    context_object_name = 'reparaciones'
    queryset = Reparacion.objects.order_by('id')
    '''
    reparaciones = Reparacion.objects.order_by('id')
    return render(request, 'listaReparaciones.html', {'reparaciones': reparaciones})
    '''
class DetalleReparacionView(DetailView):
    model = Reparacion
    template_name = 'detalleReparacion.html'
    context_object_name = 'reparacion'
    '''
    try:
        reparacion = Reparacion.objects.get(id=id)
        return render(request, 'detalleReparacion.html', {'reparacion': reparacion})
    except Reparacion.DoesNotExist:
        return HttpResponseNotFound('No existe la reparación con el identificador proporcionado.')
    '''