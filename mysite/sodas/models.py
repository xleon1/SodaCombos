from django.db import models

# Create your models here.
class SodaCombo(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    soda = models.CharField(max_length=100)
    flavor1 = models.CharField(max_length=100)
    flavor2 = models.CharField(max_length=100, null=True, blank=True)
    flavor3 = models.CharField(max_length=100, null=True, blank=True)
