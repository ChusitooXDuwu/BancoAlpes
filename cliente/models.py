from django.db import models
from django_cryptography.fields import encrypt


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=10)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado_docuemntos = models.CharField(max_length=50)
    

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

