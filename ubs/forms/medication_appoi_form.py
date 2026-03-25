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

        labels = {
            'medication': 'Medicamento',
            'appointment': 'Consulta',
            'dose': 'Dose',
            'via': 'Via de Administração',
            'frequency_days': 'Frequência (dias)',
            'duraction_adm': 'Duração do Tratamento'
        }

