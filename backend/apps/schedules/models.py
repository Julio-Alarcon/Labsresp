import django
from django.db import models
from django.contrib.auth.models import User as auth_user
from django.db.models.base import Model
from django.utils import timezone
from apps.core.models import Workstation, Room, Campus
from datetime import datetime, timedelta
import os

# Create your models here.

class DayPetition(models.Model):
    day_petition = models.CharField(max_length=50, null=True, blank=True)

class Module(models.Model):
    hour_start = models.TimeField(null=True)
    hour_finish = models.TimeField(null=True)

class LabPetition(models.Model):
    licenses=[
        ("1","EJ1"),
        ("2","EJ2")
        ]
    STATUS_PETITION = (
        ('P','Pendiente'),
        ('A','Aceptado'),
        ('R','Rechazado'),
    )
    name_petition = models.CharField(max_length=50, default="")
    email_petition = models.CharField(max_length=100, default="")
    nrc_petition = models.CharField(max_length=10, default="", blank=True)
    campus_petition = models.ForeignKey(Campus, on_delete=models.SET_NULL, null=True)
    laboratory_petition = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    cant_pc_petition = models.IntegerField(default="")
    day_petition = models.ForeignKey(DayPetition, on_delete=models.SET_NULL, null=True, blank=True)
    day_start_petition = models.DateField(null=True)
    day_finish_petition = models.DateField(null=True)
    time_start_petition = models.TimeField(null=True)
    time_finish_petition = models.TimeField(null=True)
    memo_petition = models.CharField(max_length=250, default="")
    #license_petition = models.CharField(max_length=50, choices=licenses)
    status_petition = models.CharField(max_length=1, default="P", choices=STATUS_PETITION, blank=True)

class Event(models.Model):
    name_event = models.CharField(max_length=20, default="", blank=True)
    day_event = models.ForeignKey(DayPetition, on_delete=models.SET_NULL, null=True, blank=True)
    module_event = models.ForeignKey(Module, on_delete=models.SET_NULL,null=True, blank=True)

class Schedule(models.Model):
    lab_schedule = models.ForeignKey(LabPetition, on_delete=models.SET_NULL,null=True, blank=True)
    event_schedule = models.ForeignKey(Event, on_delete=models.SET_NULL,null=True, blank=True)
    


# class UserWortation(models.Model):
#     email = models.CharField(primary_key=True)
#     name = models.CharField(max_length=50, blank=True, null=True)
#     identifier = models.CharField(max_length=50, blank=True, null=True)


# class Subject(models.Model):
#     code = models.CharField(max_length=50)
#     name = models.CharField(max_length=50)


# class Course(models.Model):
#     SHIFTS = (
#         ('D', 'Diurno'),
#         ('V', 'Vespertino'),
#     )
#     section = models.IntegerField()
#     code = models.IntegerField()
#     #period = foreign
#     shift = models.CharField(max_length=1, choices=SHIFTS)


# class ListCourse(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     user_worktation = models.ForeignKey(
#         UserWortation, on_delete=models.CASCADE)
