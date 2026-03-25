from django import forms
from ..models import Ubs

class UbsForm(forms.ModelForm):
    class Meta:
        model = Ubs
        fields = ['name', 'address']