from django.db import models
from .ubs import Ubs
from .medico import Medico
from .vaccine import Vaccine


class TipoAtendimento(models.TextChoices):
    CONSULTA = "CONSULTA", "Consulta"
    VACINA = "VACINA", "Vacina"


class FilaAtendimento(models.Model):
    ubs = models.ForeignKey(Ubs, on_delete=models.CASCADE)

    tipo_atendimento = models.CharField(
        max_length=20,
        choices=TipoAtendimento.choices
    )

    data_fila = models.DateField()

    quantidade_maxima = models.IntegerField()

    medico = models.ForeignKey(
        Medico,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    vacina = models.ForeignKey(
        Vaccine,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.ubs} - {self.tipo_atendimento}"