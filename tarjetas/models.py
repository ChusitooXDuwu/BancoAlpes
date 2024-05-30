from django.db import models


class Tarjeta(models.Model):
    id = models.AutoField(primary_key=True)
    id_cliente = models.IntegerField()
    tipo = models.CharField(max_length=255) #oro/plata
    activa = models.BooleanField(default=True)
    cupo = models.FloatField()

    def __str__(self):
        return f'{self.cliente} - {self.tipo} - {self.estado}'
# Create your models here.
