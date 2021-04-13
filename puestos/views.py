# Create your views here.
from rest_framework import generics

from puestos.models import Puesto
from puestos.serializers import PuestoSerializer


class PuestoGenericView(generics.ListCreateAPIView):
    queryset = Puesto.objects.all()
    serializer_class = PuestoSerializer


class PuestoDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Puesto.objects.all()
    serializer_class = PuestoSerializer
