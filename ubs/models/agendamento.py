from django.db import models
from .cidadao import Cidadao


class StatusAgendamento(models.TextChoices):
    PENDENTE = "PENDENTE", "Pendente"
    CONFIRMADO = "CONFIRMADO", "Confirmado"
    EM_ESPERA = "EM_ESPERA", "Em espera"


class Agendamento(models.Model):
    cidadao = models.ForeignKey(Cidadao, on_delete=models.CASCADE)

    data_solicitacao = models.DateField()
    hora_agendamento = models.TimeField()

    posicao_atual = models.IntegerField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=StatusAgendamento.choices,
        default=StatusAgendamento.PENDENTE
    )

    prioridade_calculada = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.cidadao} - {self.status}"