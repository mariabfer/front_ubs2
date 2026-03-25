from django.db import models
from .medication import Medication
from .appointment import Appointment


class ViaMedication(models.TextChoices):
    ORAL = "ORAL", "Oral"
    INTRAVENOUS = "IV", "Intravenosa"
    INTRAMUSCULAR = "IM", "Intramuscular"


class MedicationAppoi(models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.CASCADE,
        related_name="medicacoes"
    )

    dose = models.CharField(max_length=50)
    via = models.CharField(max_length=20, choices=ViaMedication.choices)

    frequency_days = models.IntegerField()
    duraction_adm = models.IntegerField()

    def __str__(self):
        return f"{self.medication} - {self.dose}"