from django import forms
from ..models import FocusPriority

class FocusPriorityForm(forms.ModelForm):
    class Meta:
        model = FocusPriority
        fields = ['vaccine', 'grupo_vulneravel', 'ocupacao']

        labels = {
    'vaccine': 'Vacina',
    'grupo_vulneravel': 'Grupo Vulnerável',
    'ocupacao': 'Ocupação'
}