from django.db import models


class Temperature(models.Model):
  year = models.IntegerField(unique=True)
  no_smooth = models.FloatField()
  lowess = models.FloatField()
