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

    def calcular_prioridade(self):
        if not self.cidadao.grupos.exists():
            return 0

        return sum(
            grupo.peso_prioridade
            for grupo in self.cidadao.grupos.all()
        )

    def save(self, *args, **kwargs):
        self.prioridade_calculada = self.calcular_prioridade()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cidadao} - {self.status}"