from django.urls import path, include
from . import views

urlpatterns = [
    path('calendario/', views.calendario, name="calendario"),
    path('reservar/', views.reservar, name="reservar"),
    path('reserva/', views.reserva, name="reserva"),
    path('administrar/', views.administrar, name="administrar"),
    path('admincalendario/', views.admincalendario, name="admincalendario"),
]