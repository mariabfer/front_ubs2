from django.db import models
from .ubs import Ubs
from .agendamento import Agendamento
from .medico import Medico


class Appointment(models.Model):
    scheduling = models.ForeignKey(
        Agendamento,
        on_delete=models.CASCADE,
        related_name="consultas"
    )

    doctor = models.ForeignKey(
        Medico,
        on_delete=models.CASCADE
    )

    ubs = models.ForeignKey(
        Ubs,
        on_delete=models.CASCADE
    )

    data = models.DateField()

    reason = models.TextField()
    life_habits = models.TextField()

    def __str__(self):
        return f"{self.doctor} - {self.data}"