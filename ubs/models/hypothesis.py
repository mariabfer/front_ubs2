from django.db import models
from .appointment import Appointment


class Hypothesis(models.Model):
    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.CASCADE,
        related_name="hipoteses"
    )

    disease = models.CharField(max_length=100)
    cid = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.disease} ({self.cid})"