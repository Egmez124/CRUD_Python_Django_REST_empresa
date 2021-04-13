from django.urls import path

from permisos.views import PermisoGenericView, PermisoDetailGenericView

app_name = 'Permiso'
urlpatterns = [
    path('', PermisoGenericView.as_view()),
    path('<pk>/', PermisoDetailGenericView.as_view())
]
