from django.db import models
from .ubs import Ubs


class EstadoCivil(models.TextChoices):
    SOLTEIRO = "SOLTEIRO", "Solteiro(a)"
    CASADO = "CASADO", "Casado(a)"
    DIVORCIADO = "DIVORCIADO", "Divorciado(a)"
    VIUVO = "VIUVO", "Viúvo(a)"
    UNIAO_ESTAVEL = "UNIAO_ESTAVEL", "União estável"


class Pessoa(models.Model):
    nome_pessoa = models.CharField(max_length=255)

    estado_civil = models.CharField(
        max_length=20,
        choices=EstadoCivil.choices
    )

    ubs = models.ForeignKey(Ubs, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_pessoa