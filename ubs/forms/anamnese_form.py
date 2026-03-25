from django import forms
from ..models import Anamnese

class AnamneseForm(forms.ModelForm):
    class Meta:
        model = Anamnese
        fields = [
            'cidadao',
            'data_anamnese',
            'peso',
            'altura',
            'pressao_arterial'
        ]

        labels = {
            'cidadao': 'Cidadão',
            'data_anamnese': 'Data da Anamnese',
            'peso': 'Peso (kg)',
            'altura': 'Altura (m)',
            'pressao_arterial': 'Pressão Arterial'
        }