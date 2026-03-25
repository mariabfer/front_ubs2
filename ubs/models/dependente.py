from django.db import models
from .pessoa import Pessoa


class Dependente(models.Model):
    responsavel = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        related_name="dependentes"
    )

    dependente = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        related_name="responsavel_de"
    )

    parentesco = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.dependente} ({self.parentesco})"