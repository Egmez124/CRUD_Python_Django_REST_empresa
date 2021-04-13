from django.db import models

# Create your models here.
class Puesto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
