from django.db import models

# Create your models here.
class SodaCombo(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    soda = models.CharField(max_length=100)
    # All are optional below this point
    # There are combos with no syrups but do have purees
    flavor1 = models.CharField(max_length=100, null=True, blank=True)
    flavor2 = models.CharField(max_length=100, null=True, blank=True)
    flavor3 = models.CharField(max_length=100, null=True, blank=True)
    flavor4 = models.CharField(max_length=100, null=True, blank=True)
    addon1 = models.CharField(max_length=100, null=True, blank=True)
    addon2 = models.CharField(max_length=100, null=True, blank=True)
    splash = models.CharField(max_length=100, null=True, blank=True)
