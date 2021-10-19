from django.db import models
from django.contrib.auth.models import User as auth_user
from django.db.models.base import Model
from apps.core.models import Workstation, Room
import datetime
import os

# Create your models here.

class Petition(models.Model):
    licenses = [
        (0,"")
    ]

    name_petition = models.CharField(max_length=100, default="")
    email_petition = models.CharField(max_length=100, default="")
    nrc_petition = models.CharField(max_length=10, default="")
    laboratory_petition = models.CharField(max_length=10, default="")
    pc_petition = models.CharField(max_length=3, default="")
    time_start = models.DateTimeField(null=True)
    time_finish = models.DateTimeField(null=True)
    license = models.CharField(max_length=50, default="", choices=licenses)
    memo = models.CharField(max_length=250, default="")
    status = models.CharField(max_length=20, default="")
    def __str__(self):
        return "{}".format(self.name_petition)

class Schedule(models.Model):
    workstation=models.ForeignKey(Workstation,on_delete=models.SET_NULL,null=True,blank=True)