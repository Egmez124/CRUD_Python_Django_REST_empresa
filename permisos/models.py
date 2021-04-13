from django.db import models

# Create your models here.
from empleados.models import Empleado


class Permiso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    empleado = models.ForeignKey(
        Empleado,
        related_name='empleados',
        on_delete=models.SET_NULL,
        null=True
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
