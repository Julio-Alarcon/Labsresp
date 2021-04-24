from django.db import models
from rest_framework.views import APIView

# Create your models here.

class hours(models.Model):
    hours = models.IntegerField()
    minutes = models.IntegerField()