from django import forms
from .models import Tarjeta


class TarjetaForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = [
            'cliente',
            'tipo',
            'estado',
            'archivo',
            'score_confiabilidad',
        ]

        labels = {
            'cliente' : 'Cliente',
            'tipo' : 'Tipo',
            'estado' : 'Estado',
            'archivo' : 'archivo',
            'score_confiabilidad' : 'Score_Confiabilidad',
        }
