from django import forms
from .models import Tarjeta


class TarjetaForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = [
            'id',
            'id_cliente', # This is the field that was changed from 'cliente' to 'id_cliente'
            'tipo',
            'activa',
            'cupo',
        ]
        labels = {
            'id' : 'ID',
            'id_cliente' : 'ID Cliente',
            'tipo' : 'Tipo',
            'activa' : 'Activa',
            'cupo' : 'Cupo',
        }
      