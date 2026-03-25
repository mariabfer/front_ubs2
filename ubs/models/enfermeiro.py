from django.db import models
from .pessoa import Pessoa


class Enfermeiro(Pessoa):
    cip = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome_pessoa} - CIP: {self.cip}"