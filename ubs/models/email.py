from django.db import models
from .pessoa import Pessoa
from .ubs import Ubs


class TipoEmail(models.TextChoices):
    PESSOA = "PESSOA", "Pessoa"
    UBS = "UBS", "UBS"


class Email(models.Model):
    email = models.EmailField()

    tipo = models.CharField(
        max_length=10,
        choices=TipoEmail.choices
    )

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="emails"
    )

    ubs = models.ForeignKey(
        Ubs,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="emails"
    )

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.tipo == TipoEmail.PESSOA:
            if not self.pessoa or self.ubs:
                raise ValidationError("Email de pessoa deve ter apenas pessoa")

        elif self.tipo == TipoEmail.UBS:
            if not self.ubs or self.pessoa:
                raise ValidationError("Email de UBS deve ter apenas UBS")

    def __str__(self):
        return self.email