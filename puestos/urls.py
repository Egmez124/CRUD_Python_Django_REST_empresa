from django.urls import path

from puestos.views import PuestoGenericView, PuestoDetailGenericView

app_name = 'Puesto'
urlpatterns = [
    path('', PuestoGenericView.as_view()),
    path('<pk>/', PuestoDetailGenericView.as_view())
]
