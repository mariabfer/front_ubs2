from django.db import models
from .address import Address


class Ubs(models.Model):
    name = models.CharField(max_length=255)

    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        related_name="ubs"
    )

    def __str__(self):
        return self.name