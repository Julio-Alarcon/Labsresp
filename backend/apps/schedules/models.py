from django.db import models
from django.contrib.auth.models import User as auth_user
from apps.core.models import Workstation, Room
import datetime
import os

# Create your models here.

class Petition(models.Model):
    licenses = [
        (0,"")
    ]

    name_petition = models.CharField(max_length=100)
    email_petition = models.CharField(max_length=100)
    nrc_petition = models.CharField(max_length=10)
    laboratory_petition = models.CharField(max_length=10)
    pc_petition = models.CharField(max_length=3)
    time_start = models.DateField()
    time_finish = models.DateField()
    license = models.CharField(max_length=50, choices=licenses)
    memo = models.CharField(max_length=250)
    status = models.CharField(max_length=20)
    def __str__(self):
        return "{}".format(self.name_petition)
