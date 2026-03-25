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

        labels = {
            'ubs': 'UBS',
            'tipo_atendimento': 'Tipo de Atendimento',
            'data_fila': 'Data',
            'quantidade_maxima': 'Quantidade Máxima',
            'medico': 'Médico',
            'vacina': 'Vacina'
        }