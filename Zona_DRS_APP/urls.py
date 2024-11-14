from django.urls import path
from . import views
from .views import (
    IndexView, 
    ListaPropietariosView, DetallePropietarioView, 
    ListaMecanicosView, DetalleMecanicoView,
    ListaVehiculosView, DetalleVehiculoView,
    ListaReparacionesView, DetalleReparacionView
) 
urlpatterns = [
        
    # Vista de inicio
    path('', IndexView.as_view(), name='index'),
    
    # Propietarios
    path('listaPropietarios/', ListaPropietariosView.as_view(), name='listaPropietarios'),
    path('propietario/<str:pk>/', DetallePropietarioView.as_view(), name='detallePropietario'),
    
    # Mecánicos
    path('listaMecanicos/', ListaMecanicosView.as_view(), name='listaMecanicos'),
    path('mecanico/<str:pk>/', DetalleMecanicoView.as_view(), name='detalleMecanico'),
    
    # Vehículos
    path('listaVehiculos/', ListaVehiculosView.as_view(), name='listaVehiculos'),
    path('vehiculo/<str:pk>/', DetalleVehiculoView.as_view(), name='detalleVehiculo'),
    
    # Reparaciones
    path('listaReparaciones/', ListaReparacionesView.as_view(), name='listaReparaciones'),
    path('reparacion/<int:pk>/', DetalleReparacionView.as_view(), name='detalleVeparacion'),
    

          
      
]