from django import forms
from ..models import MedicationUbs

class MedicationUbsForm(forms.ModelForm):
    class Meta:
        model = MedicationUbs
        fields = [
            'medication',
            'ubs',
            'num_lote',
            'available_quantity',
            'validity'
        ]

        widgets = {
            'validity': forms.DateInput(attrs={'type': 'date'}),
        }

        labels = {
            'medication': 'Medicamento',
            'ubs': 'UBS',
            'num_lote': 'Número do Lote',
            'available_quantity': 'Quantidade Disponível',
            'validity': 'Validade'
        }