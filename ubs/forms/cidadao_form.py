from django import forms
from ..models import Cidadao

class CidadaoForm(forms.ModelForm):
    class Meta:
        model = Cidadao
        fields = [
            'num_sus',
            'data_nascimento',
            'genero',
            'naturalidade',
            'ocupacao',
            'address',
            'grupos'
        ]

        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }