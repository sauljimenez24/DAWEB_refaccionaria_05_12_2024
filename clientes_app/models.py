from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=50) 
    edad = models.PositiveIntegerField() 
    num_cel = models.PositiveIntegerField()
    sexo = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre