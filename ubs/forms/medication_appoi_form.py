from django import forms
from ..models import MedicationAppoi

class MedicationAppoiForm(forms.ModelForm):
    class Meta:
        model = MedicationAppoi
        fields = [
            'medication',
            'appointment',
            'dose',
            'via',
            'frequency_days',
            'duraction_adm'
        ]