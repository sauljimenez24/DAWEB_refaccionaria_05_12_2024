from django.db import models

# Create your models here.
class Refaccion(models.Model):
    id_refaccion=models.PositiveIntegerField(primary_key=True)
    nombre_refaccion=models.CharField(max_length=100)
    cantidad=models.PositiveIntegerField()
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    marca=models.CharField(max_length=100)
    id_provedor=models.PositiveIntegerField()
    

    def __str__(self):
        return self.nombre_refaccion