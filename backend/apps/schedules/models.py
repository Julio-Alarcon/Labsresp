import django
from django.db import models
from django.contrib.auth.models import User as auth_user
from django.db.models.base import Model
from django.utils import timezone
from apps.core.models import Workstation, Room, Campus
from datetime import datetime, timedelta
import os

# Create your models here.

class Petition(models.Model):
    licenses = [
        (1,"EJ"), (2,"EJ2")
    ]

    name_petition = models.CharField(max_length=100, default="")
    email_petition = models.CharField(max_length=100, default="")
    nrc_petition = models.CharField(max_length=10, default="", blank=True)
    campus_petition = models.ForeignKey(Campus, on_delete=models.SET_NULL,null=True)
    laboratory_petition = models.ForeignKey(Room, on_delete=models.SET_NULL,null=True,blank=True)
    pc_petition = models.CharField(max_length=3, default="")
    day_start_petition = models.DateField(null=True, default=timezone.now())
    time_start_petition = models.TimeField(null=True, default=timezone.now())
    day_finish_petition = models.DateField(null=True, default=timezone.now())
    time_finish_petition = models.TimeField(null=True, default=timezone.now())
    day_petition = models.CharField(max_length=20, default="")
    license_petition = models.CharField(max_length=20, choices=licenses, blank=True)
    memo_petition = models.CharField(max_length=250, default="")
    status_petition = models.CharField(max_length=20, default="Pendiente", blank=True)
    active_petition = models.BooleanField(default=False)
    def __str__(self):
        return "{}".format(self.name_petition)
    def __unicode__(self):
        return "{}".format(self.name_petition)

class Schedule(models.Model):
    petition = models.ForeignKey(Petition, on_delete=models.SET_NULL,null=True, blank=True)
    def __str__(self):
        return "{}".format(self.day)
    def __unicode__(self):
        return "{}".format(self.day)