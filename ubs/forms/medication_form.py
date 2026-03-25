from django import forms
from ..models import Medication

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['name_medication', 'category_med']