from django.contrib import admin

from .models import Propietario, Mecanico, Vehiculo, Reparacion

# Register your models here.

admin.site.register(Propietario)
admin.site.register(Mecanico)
admin.site.register(Vehiculo)
admin.site.register(Reparacion)