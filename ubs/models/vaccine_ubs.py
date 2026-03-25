from django.db import models
from .vaccine import Vaccine
from .ubs import Ubs
from .focus_priority import FocusPriority


class Priority(models.TextChoices):
    VERY_HIGH = "VERY_HIGH", "Muito Alta"
    HIGH = "HIGH", "Alta"
    MEDIUM = "MEDIUM", "Média"
    LOW = "LOW", "Baixa"


class VaccineUbs(models.Model):
    vaccine = models.ForeignKey(
        Vaccine,
        on_delete=models.CASCADE,
        related_name="estoques"
    )

    ubs = models.ForeignKey(
        Ubs,
        on_delete=models.CASCADE,
        related_name="vacinas"
    )

    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        null=True,
        blank=True
    )

    dose = models.CharField(max_length=50)
    lote = models.CharField(max_length=50)

    available_quan = models.IntegerField()

    validity = models.DateField()

    focus_priority = models.ManyToManyField(
        FocusPriority,
        related_name="vacinas",
        blank=True
    )

    def __str__(self):
        return f"{self.vaccine} - {self.ubs} (Lote: {self.lote})"