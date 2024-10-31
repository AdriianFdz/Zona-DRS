from django.db import models

# Create your models here.
class Propietario(models.Model):
    dni = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido1 = models.CharField(max_length=255)
    apellido2 = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre
    
class Mecanico(models.Model):
    num_ss = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido1 = models.CharField(max_length=255)
    apellido2 = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    fecha_inicio_contrato = models.DateField()
    fecha_fin_contrato = models.DateField()
    imagen_url = models.URLField()

    def __str__(self):
        return self.nombre
    
class Vehiculo(models.Model):
    matricula = models.CharField(max_length=7, primary_key=True)
    tipo = models.CharField(
        max_length=10,
        choices=[
            ('Coche', 'Coche'),
            ('Moto', 'Moto'),
            ('Camión', 'Camión')
        ]
    )
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    fecha_fabricacion = models.DateField()
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)

    def __str__(self):
        return self.matricula
    
class Reparacion(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    coste = models.FloatField()
    imagen_url = models.URLField()
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    mecanico = models.ManyToManyField(Mecanico, related_name='reparaciones')

    def __str__(self):
        return self.id