from django import forms
from ..models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = [
            'cidadao',
            'data_solicitacao',
            'hora_agendamento',
            'posicao_atual',
            'status',
            'prioridade_calculada'
        ]

        labels = {
            'cidadao': 'Cidadão',
            'data_solicitacao': 'Data da Solicitação',
            'hora_agendamento': 'Hora do Agendamento',
            'posicao_atual': 'Posição na Fila',
            'status': 'Status',
            'prioridade_calculada': 'Prioridade'
        }

        widgets = {
            'data_solicitacao': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'hora_agendamento': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }