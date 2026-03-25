from django import forms
from ..models import Medico

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['crm', 'especialidade']