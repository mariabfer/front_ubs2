from django.db import models
from .pessoa import Pessoa


class Medico(Pessoa):
    crm = models.CharField(max_length=20, unique=True)
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome_pessoa} - {self.especialidade}"