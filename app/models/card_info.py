from django.db import models

from app.enums import SOLVE_CHOICES


class WarningCardInfo(models.Model):
  title = models.TextField(max_length=100)
  subtitle = models.CharField(max_length=100)
  
class SolveCardInfo(models.Model):
  title = models.TextField(max_length=100)
  subtitle = models.CharField(max_length=100)
  category = models.CharField(max_length=10, choices=SOLVE_CHOICES, default=None)
