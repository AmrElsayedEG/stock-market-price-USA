from django.db import models
from django.db.models.signals import post_save
# Create your models here.

class DailyPrice(models.Model):
    symbol = models.CharField(max_length=7)
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
