# Create your views here.
from rest_framework import generics

from permisos.models import Permiso
from permisos.serializers import PermisoSerializer


class PermisoGenericView(generics.ListCreateAPIView):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer


class PermisoDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer
