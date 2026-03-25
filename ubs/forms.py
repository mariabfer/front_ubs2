from django import forms
from .models.address import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['cep', 'state', 'city', 'neigh', 'street', 'number']