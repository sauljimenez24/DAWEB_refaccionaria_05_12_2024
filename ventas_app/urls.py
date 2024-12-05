from django.urls import path
from ventas_app import views

urlpatterns = [
    path('venta', views.inicio_vistaVenta, name='venta'),
    path('registrarVenta/', views.registrarVenta, name='registrarVenta'),
    path('seleccionarVenta/<codigo>/', views.seleccionarVenta, name='seleccionarVenta'),
    path('editarVenta/', views.editarVenta, name='editarVenta'),
    path('borrarVenta/<codigo>/', views.borrarVenta, name='borrarVenta'),
]
