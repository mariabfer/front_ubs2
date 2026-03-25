from django import forms
from ..models import Email

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email', 'tipo', 'pessoa', 'ubs']

        labels = {
            'email': 'E-mail',
            'tipo': 'Tipo',
            'pessoa': 'Pessoa',
            'ubs': 'UBS'
        }