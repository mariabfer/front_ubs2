from django.db import models
from .pessoa import Pessoa
from .address import Address
from .grupo_vulneravel import GrupoVulneravel


class Genero(models.TextChoices):
    FEMININO = "F", "Feminino"
    MASCULINO = "M", "Masculino"


class Cidadao(Pessoa):  # Pessoa precisa ser models.Model
    num_sus = models.CharField(max_length=20)

    data_nascimento = models.DateField()

    genero = models.CharField(
        max_length=1,
        choices=Genero.choices
    )

    naturalidade = models.CharField(max_length=100)
    ocupacao = models.CharField(max_length=100)

    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    grupos = models.ManyToManyField(
        GrupoVulneravel,
        related_name="cidadaos",
        blank=True
    )

    def __str__(self):
        return f"{self.nome_pessoa} - SUS: {self.num_sus}"