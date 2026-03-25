from django import forms
from ..models import RecordVaccine

class RecordVaccineForm(forms.ModelForm):
    class Meta:
        model = RecordVaccine
        fields = [
            'citizen',
            'vaccine_ubs',
            'nurse',
            'ubs',
            'data'
        ]

        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }

        labels = {
            'citizen': 'Cidadão',
            'vaccine_ubs': 'Vacina (UBS)',
            'nurse': 'Enfermeiro',
            'ubs': 'UBS',
            'data': 'Data da Aplicação'
        }