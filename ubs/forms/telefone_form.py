from django import forms
from ..models import Telefone

class TelefoneForm(forms.ModelForm):
    class Meta:
        model = Telefone
        fields = ['numero', 'tipo', 'pessoa', 'ubs']