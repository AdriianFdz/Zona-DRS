from django.urls import path
from . import views

urlpatterns = [
            path('', views.index, name='index'),
            path('listaPropietarios/', views.listaPropietarios, name='listaPropietarios'),
            path('propietario/<str:dni>', views.detallePropietario, name='detallePropietario'),
            path('listaMecanicos/', views.listaMecanicos, name='listaMecanicos'),
            path('mecanico/<str:num_ss>', views.detalleMecanico, name='detalleMecanico'),
            path('listaVehiculos/', views.listaVehiculos, name='listaVehiculos'),
            path('vehiculo/<str:matricula>', views.detalleVehiculo, name='detalleVehiculo'),
            path('listaReparaciones/', views.listaReparaciones, name='listaReparaciones'),
]