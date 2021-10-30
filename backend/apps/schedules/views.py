from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.core.models import Room, Campus
from apps.schedules.models import LabPetition
from apps.schedules.forms import LabPetitionForms


# Create your views here.

def calendario(request):
    template_name="calendario.html"
    context={}
    laboratories=Room.objects.all()
    campus=Campus.objects.all()
    context['laboratories']=laboratories
    context['campus']=campus
    return render(request, template_name, context)

def reserva(request):
    template_name="reserva.html"
    context={}
    #context['name'] = request.GET['name']
    return render(request, template_name, context)

def administrar(request):
    template_name="administrar.html"
    context={}
    labpetition=LabPetition.objects.all()
    context['labpetition']=labpetition
    return render(request, template_name, context)

def reservar(request):
    template_name="reservar.html"
    context={}
    if request.POST:
        form_lab=LabPetitionForms(request.POST)
        if form_lab.is_valid():
            form_lab.save()
            return HttpResponseRedirect(reverse('calendario'))
        else:
            print(form_lab.errors)
            messages.error(request, "Error")
    context['formlab']=LabPetitionForms()
    return render(request, template_name, context)

def admincalendario(request):
    template_name="admincalendario.html"
    context={}
    return render(request, template_name, context)