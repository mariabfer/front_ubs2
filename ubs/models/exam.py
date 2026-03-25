from django.db import models
from .appointment import Appointment


class ExamType(models.TextChoices):
    LAB = "LAB", "Laboratorial"
    IMG = "IMG", "Imagem"


class StatusExam(models.TextChoices):
    REQUESTED = "REQUESTED", "Solicitado"
    DONE = "DONE", "Realizado"


class Exam(models.Model):
    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.CASCADE,
        related_name="exames"
    )

    name_exam = models.CharField(max_length=100)

    type = models.CharField(max_length=20, choices=ExamType.choices)

    status = models.CharField(max_length=20, choices=StatusExam.choices)

    result = models.TextField(null=True, blank=True)

    data = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name_exam