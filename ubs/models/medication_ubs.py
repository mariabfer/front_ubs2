from django.db import models
from .medication import Medication
from .ubs import Ubs


class MedicationUbs(models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    ubs = models.ForeignKey(Ubs, on_delete=models.CASCADE)

    num_lote = models.CharField(max_length=50)
    available_quantity = models.IntegerField()
    validity = models.DateField()

    def __str__(self):
        return f"{self.medication} - {self.ubs}"