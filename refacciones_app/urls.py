from django.urls import path
from refacciones_app import views

urlpatterns = [
    path('refaccion', views.inicio_vistaRefaccion, name='refaccion'),
    path('registrarRefaccion/', views.registrarRefaccion, name='registrarRefaccion'),
    path('seleccionarRefaccion/<codigo>/', views.seleccionarRefaccion, name='seleccionarRefaccion'),
    path('editarRefaccion/', views.editarRefaccion, name='editarRefaccion'),
    path('borrarRefaccion/<codigo>/', views.borrarRefaccion, name='borrarRefaccion'),
]
