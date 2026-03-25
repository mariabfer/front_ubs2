from django.db import models
from .cidadao import Cidadao
from .enfermeiro import Enfermeiro
from .ubs import Ubs
from .vaccine_ubs import VaccineUbs


class RecordVaccine(models.Model):
    citizen = models.ForeignKey(Cidadao, on_delete=models.CASCADE)
    vaccine_ubs = models.ForeignKey(VaccineUbs, on_delete=models.CASCADE)

    nurse = models.ForeignKey(Enfermeiro, on_delete=models.CASCADE)
    ubs = models.ForeignKey(Ubs, on_delete=models.CASCADE)

    data = models.DateField()

    def __str__(self):
        return f"{self.citizen} - {self.data}"