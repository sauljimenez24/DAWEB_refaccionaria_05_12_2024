from django.db import models

# Create your models here.
class Venta(models.Model):
    id_venta = models.PositiveIntegerField(primary_key=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    id_cliente = models.PositiveIntegerField()
    id_empleado = models.PositiveIntegerField()
    id_refaccion = models.PositiveIntegerField()
    total=models.DecimalField(max_digits=10, decimal_places=2)
    fecha_venta = models.DateField(null=False,blank=False)

    def __str__(self):
        return self.id_venta