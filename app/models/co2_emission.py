from django.db import models


class Co2Emission(models.Model):
  country = models.CharField(max_length=50)
  year = models.IntegerField(unique=True)
  amount = models.IntegerField()
