from django.urls import path, include
from . import views

urlpatterns = [
    path('calendario/', views.calendario, name="calendario"),
    path('salas/', views.salas, name="salas"),

]