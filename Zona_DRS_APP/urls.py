from django.urls import path
from . import views

urlpatterns = [
            path('', views.index, name='index'),
            path('listaPropietarios/', views.listaPropietarios, name='listaPropietarios'),
            path('listaMecanicos/', views.listaMecanicos, name='listaMecanicos'),
            path('listaVehiculos/', views.listaVehiculos, name='listaVehiculos'),
            path('listaReparaciones/', views.listaReparaciones, name='listaReparaciones'),
]