from django.db import models
from .pessoa import Pessoa
from .ubs import Ubs


class TipoTelefone(models.TextChoices):
    PESSOA = "PESSOA", "Pessoa"
    UBS = "UBS", "UBS"


class Telefone(models.Model):
    numero = models.CharField(max_length=20)

    tipo = models.CharField(
        max_length=10,
        choices=TipoTelefone.choices
    )

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="telefones"
    )

    ubs = models.ForeignKey(
        Ubs,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="telefones"
    )

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.tipo == TipoTelefone.PESSOA:
            if not self.pessoa or self.ubs:
                raise ValidationError("Telefone de pessoa deve ter apenas pessoa")

        elif self.tipo == TipoTelefone.UBS:
            if not self.ubs or self.pessoa:
                raise ValidationError("Telefone de UBS deve ter apenas UBS")

    def __str__(self):
        return self.numero