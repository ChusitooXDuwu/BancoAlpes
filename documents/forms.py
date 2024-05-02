from django import forms
from .models import Documento


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Documento
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
