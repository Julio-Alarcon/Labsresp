from django.contrib import admin
from apps.schedules.models import DayPetition, LabPetition, Module, Event, Schedule

admin.site.register(DayPetition)
admin.site.register(LabPetition)
admin.site.register(Module)
admin.site.register(Event)
admin.site.register(Schedule)