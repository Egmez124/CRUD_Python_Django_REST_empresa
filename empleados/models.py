from django.db import models

# Create your models here.
from puestos.models import Puesto


class Empleado(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=100)
    puesto = models.ForeignKey(
        Puesto,
        related_name='puestos',
        on_delete=models.SET_NULL,
        null=True
    )
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.nombre
