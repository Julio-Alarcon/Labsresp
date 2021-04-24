from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def calendario(request):
    template_name="calendario.html"
    context={}
    #context['name'] = request.GET['name']
    return render(request, template_name, context)