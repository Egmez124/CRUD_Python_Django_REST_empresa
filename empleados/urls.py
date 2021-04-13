from django.urls import path

from empleados.views import EmpleadoGenericView, EmpleadoDetailGenericView

app_name = 'Empleado'
urlpatterns = [
    path('', EmpleadoGenericView.as_view()),
    path('<pk>/', EmpleadoDetailGenericView.as_view())
]
