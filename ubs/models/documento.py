from django.db import models
from .pessoa import Pessoa


class TipoDocumento(models.TextChoices):
    CPF = "CPF", "CPF"
    RG = "RG", "RG"
    CNH = "CNH", "CNH"


class Documento(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name="documentos")

    tipo_documento = models.CharField(
        max_length=30,
        choices=TipoDocumento.choices
    )

    numero_documento = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tipo_documento} - {self.numero_documento}"