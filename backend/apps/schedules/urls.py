from django.urls import path, include
from . import views

urlpatterns = [
    path('calendario/', views.calendario, name="calendario"),

]