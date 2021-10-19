from django import forms
from django.forms import fields
from datetime import datetime
from . import models

licenses = [
    (0, ""),
]

class FormPetition(forms.Form):
    nombre = forms.CharField(label="Nombre ",required=True)
    email = forms.EmailField(label="Correo ", required=True)
    nrc = forms.CharField(label="NRC ", required=True)
    laboratory = forms.CharField(label="Laboratorio ", required=True)
    time_start = forms.CharField(label="Hora inicio ", required=True)
    time_finish = forms.CharField(label="Hora termino ", required=True)
    license = fields.TypedChoiceField(label="Licencia ", required=True, choices = licenses)
    memo = forms.CharField(max_length=250)
    status = forms.CharField(max_length=20, initial="waiting")