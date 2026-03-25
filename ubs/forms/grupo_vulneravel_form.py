from django import forms
from ..models import GrupoVulneravel

class GrupoVulneravelForm(forms.ModelForm):
    class Meta:
        model = GrupoVulneravel
        fields = ['nome_grupo', 'peso_prioridade', 'descricao']

        labels = {
            'nome_grupo': 'Nome do Grupo',
            'peso_prioridade': 'Peso de Prioridade',
            'descricao': 'Descrição'
        }