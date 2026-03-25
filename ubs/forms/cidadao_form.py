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

        labels = {
            'num_sus': 'Número do SUS',
            'data_nascimento': 'Data de Nascimento',
            'genero': 'Gênero',
            'naturalidade': 'Naturalidade',
            'ocupacao': 'Ocupação',
            'address': 'Endereço',
            'grupos': 'Grupos Vulneráveis'
        }