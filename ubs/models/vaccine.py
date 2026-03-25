from django.db import models


class Vaccine(models.Model):
    type_vaccine = models.CharField(max_length=100)

    vaccine_manufacturer = models.CharField(max_length=100)

    prevents = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.type_vaccine} - {self.vaccine_manufacturer}"