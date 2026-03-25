from django import forms
from ..models import Anamnese

class AnamneseForm(forms.ModelForm):
    class Meta:
        model = Anamnese
        fields = [
            'cidadao',
            'data_anamnese',
            'peso',
            'altura',
            'pressao_arterial'
        ]