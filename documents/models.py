from django.db import models
from cliente.models import Cliente

class Documento(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=None)
    tipo = models.CharField(max_length=100) #si es cedula, recibo, pasaporte, etc
    #create a checker called gender, so its male , female, gay, or prefer not to say
    
    fecha_subida = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50)   #si ya fue confirmado o no *******ASR*****
    archivo = models.CharField(max_length=50)
    score_confiabilidad = models.FloatField(default=0.0)  #score ese importante para analisis debe ser x un api hay que mockearlo
    

    def __str__(self):
        return f'{self.cliente} - {self.tipo} - {self.estado}'
# Create your models here.
