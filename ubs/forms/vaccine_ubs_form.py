from django import forms
from ..models import VaccineUbs

class VaccineUbsForm(forms.ModelForm):
    class Meta:
        model = VaccineUbs
        fields = [
            'vaccine',
            'ubs',
            'priority',
            'dose',
            'lote',
            'available_quan',
            'validity',
            'focus_priority'
        ]

        widgets = {
            'validity': forms.DateInput(attrs={'type': 'date'}),
        }