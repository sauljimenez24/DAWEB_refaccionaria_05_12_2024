from django.db import models

# Create your models here.
class Proveedor(models.Model):
    id_proveedor = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo=models.EmailField(max_length=50)
    telefono = models.PositiveIntegerField()
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre