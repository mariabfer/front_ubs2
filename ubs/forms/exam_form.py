from django import forms
from ..models import Exam

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = [
            'appointment',
            'name_exam',
            'type',
            'status',
            'result',
            'data'
        ]

        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }

        labels = {
            'appointment': 'Consulta',
            'name_exam': 'Nome do Exame',
            'type': 'Tipo',
            'status': 'Status',
            'result': 'Resultado',
            'data': 'Data do Exame'
        }