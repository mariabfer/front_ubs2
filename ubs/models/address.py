from django.db import models

class Address(models.Model):
    cep = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    neigh = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street}, {self.number} - {self.city}/{self.state} ({self.cep})"