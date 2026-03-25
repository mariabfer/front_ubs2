from django.db import models


class Medication(models.Model):
    name_medication = models.CharField(max_length=100)
    category_med = models.CharField(max_length=100)

    def __str__(self):
        return self.name_medication