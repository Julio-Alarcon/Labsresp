from django import forms
from django.db.models.base import Model
from django.db.models.fields import DateField
from django.forms import fields
from datetime import datetime
from django.forms import widgets
from django.forms.forms import Form
from django.forms.widgets import DateInput, TimeInput
from apps.schedules.models import LabPetition
from django.forms import ModelForm, Textarea

class LabPetitionForms(forms.ModelForm):
    class Meta:
        model = LabPetition
        fields = [
            'name_petition',
            'email_petition',
            'nrc_petition',
            'campus_petition',
            'laboratory_petition',
            'cant_pc_petition',
            'day_petition',
            'day_start_petition',
            'day_finish_petition',
            'time_start_petition',
            'time_finish_petition',
            'memo_petition',
        ]
        labels = {
            'name_petition':'Nombre:',
            'email_petition':'Email:',
            'nrc_petition':'NRC:',
            'campus_petition':'Sede:',
            'laboratory_petition':'Laboratorio:',
            'cant_pc_petition':'Computadores:',
            'day_petition':'Día:',
            'day_start_petition':'Fecha inicio:',
            'day_finish_petition':'Fecha termino:',
            'time_start_petition':'Hora inicio:',
            'time_finish_petition':'Hora termino:',
            'memo_petition':'Mensaje:',
        }

        widgets={
            'memo_petition':Textarea(attrs={'cols': 40, 'rows': 5}),
            'day_start_petition':DateInput(attrs={'id':'kt_datepicker_3', 'data-date-format':'mm/dd/yyyy', 'readonly':'readonly'}),
            'day_finish_petition':DateInput(attrs={'id':'kt_datepicker_3', 'data-date-format':'mm/dd/yyyy', 'readonly':'readonly'}),
            'time_start_petition':TimeInput(attrs={'id':'kt_timepicker_5'}),
            'time_finish_petition':TimeInput(attrs={'id':'kt_timepicker_5'})
        }

    def __init__(self,*args, **kwargs):
        super(LabPetitionForms, self).__init__(*args,**kwargs)
        self.fields['name_petition'].widget.attrs.update({'class':'form-control'})
        self.fields['email_petition'].widget.attrs.update({'class':'form-control'})
        self.fields['nrc_petition'].widget.attrs.update({'class':'form-control'})
        self.fields['campus_petition'].widget.attrs.update({'class':'form-control'})
        self.fields['laboratory_petition'].widget.attrs.update({'class':'form-control'})
        self.fields['cant_pc_petition'].widget.attrs.update({'class':'form-control'})
        self.fields['day_petition'].widget.attrs.update({'class':'form-control'})
        self.fields['day_start_petition'].widget.attrs.update({'class':'form-control'})
        self.fields['day_finish_petition'].widget.attrs.update({'class':'form-control'})
        self.fields['time_start_petition'].widget.attrs.update({'class':'form-control'})
        self.fields['time_finish_petition'].widget.attrs.update({'class':'form-control'})
        self.fields['memo_petition'].widget.attrs.update({'class':'form-control'})
        