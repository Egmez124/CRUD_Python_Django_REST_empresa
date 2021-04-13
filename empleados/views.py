# Create your views here.
from rest_framework import generics

from empleados.models import Empleado
from empleados.serializers import EmpleadoSerializer


class EmpleadoGenericView(generics.ListCreateAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer


class EmpleadoDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
