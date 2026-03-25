from django import forms
from ..models import Hypothesis

class HypothesisForm(forms.ModelForm):
    class Meta:
        model = Hypothesis
        fields = ['appointment', 'disease', 'cid']