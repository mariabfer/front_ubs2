from django import forms
from ..models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['cep', 'state', 'city', 'neigh', 'street', 'number']

        labels = {
            'cep': 'CEP',
            'state': 'Estado',
            'city': 'Cidade',
            'neigh': 'Bairro',
            'street': 'Rua',
            'number': 'Número'
        }