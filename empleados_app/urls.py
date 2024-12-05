from django.urls import path
from empleados_app import views

urlpatterns = [
    path('empleado', views.inicio_vistaEmpleado, name='empleado'),
    path('registrarEmpleado/', views.registrarEmpleado, name='registrarEmpleado'),
    path('seleccionarEmpleado/<codigo>/', views.seleccionarEmpleado, name='seleccionarEmpleado'),
    path('editarEmpleado/', views.editarEmpleado, name='editarEmpleado'),
    path('borrarEmpleado/<codigo>/', views.borrarEmpleado, name='borrarEmpleado'),
]
