from django.db import models
from .cidadao import Cidadao


class Anamnese(models.Model):
    cidadao = models.ForeignKey(Cidadao, on_delete=models.CASCADE)

    data_anamnese = models.DateField()

    peso = models.FloatField()
    altura = models.FloatField()

    pressao_arterial = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.cidadao} - {self.data_anamnese}"