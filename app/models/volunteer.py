from django.db import models
from django.utils import timezone
from app.enums import SOLVE_CHOICES


class VolunList(models.Model):
    title = models.TextField(max_length=100)
    subtitle = models.CharField(max_length=100)
    image_url = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()