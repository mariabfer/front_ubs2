from django import forms
from ..models import FilaAtendimento

class FilaAtendimentoForm(forms.ModelForm):
    class Meta:
        model = FilaAtendimento
        fields = [
            'ubs',
            'tipo_atendimento',
            'data_fila',
            'quantidade_maxima',
            'medico',
            'vacina'
        ]

        widgets = {
            'data_fila': forms.DateInput(attrs={'type': 'date'}),
        }