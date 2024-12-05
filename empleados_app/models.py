from django.db import models

# Create your models here.
class Empleado(models.Model):
    id_empleado = models.PositiveIntegerField(primary_key=True)
    numero_de_cel = models.PositiveIntegerField()
    fecha_nac = models.DateField(null=False,blank=False)
    direccion = models.CharField(max_length=255)
    sexo = models.CharField(max_length=10)  # Ejemplo: 'Masculino', 'Femenino'
    correo=models.EmailField(max_length=50)

    def __str__(self):
        return self.nombre