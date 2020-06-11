from django.db import models


class CardInfo(models.Model):
  CLIMATE = 'climate'
  ARTIC = 'artic'
  LIFE = 'life'

  POSITIVE_CHOICES = (
    (CLIMATE, 'Climate'),
    (ARTIC, 'Artic'),
    (LIFE, 'Life'),
  )

  title = models.TextField(max_length=100)
  subtitle = models.CharField(max_length=100)
  category = models.CharField(max_length=20, choices=POSITIVE_CHOICES, default=None)
  is_positive = models.BooleanField()