from django.contrib import admin
from django.forms import ModelForm
from django.http import HttpRequest

from .models import Propietario, Mecanico, Vehiculo, Reparacion, urlImagenesReparacion
from .utils import send_email


class urlImagenesReparacionInline(admin.TabularInline):
    model = urlImagenesReparacion
    extra = 1  # Permite añadir una fila extra para una nueva imagen

class ReparacionConFotos(admin.ModelAdmin):
    inlines = [urlImagenesReparacionInline]  # Asocia el inline con Reparacion
    list_display = ('id', 'fecha_inicio', 'fecha_fin', 'coste', 'vehiculo')  # Campos que se muestran en la lista
   
    def response_add(self, request, obj, post_url_continue=None):
        send_email(obj)
        return super().response_add(request, obj, post_url_continue)

# Register your models here.
admin.site.register(Propietario)
admin.site.register(Mecanico)
admin.site.register(Vehiculo)
admin.site.register(Reparacion, ReparacionConFotos)