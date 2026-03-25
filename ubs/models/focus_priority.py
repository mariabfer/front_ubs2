from django.db import models
from .vaccine import Vaccine
from .grupo_vulneravel import GrupoVulneravel


class FocusPriority(models.Model):
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)

    grupo_vulneravel = models.ForeignKey(
        GrupoVulneravel,
        on_delete=models.CASCADE
    )

    ocupacao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.vaccine} - {self.grupo_vulneravel}"