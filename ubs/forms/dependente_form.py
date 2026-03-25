from django import forms
from ..models import Dependente

class DependenteForm(forms.ModelForm):
    class Meta:
        model = Dependente
        fields = ['responsavel', 'dependente', 'parentesco']

        labels = {
            'responsavel': 'Responsável',
            'dependente': 'Dependente',
            'parentesco': 'Parentesco'
        }