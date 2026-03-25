from django import forms
from ..models import Documento

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['pessoa', 'tipo_documento', 'numero_documento']