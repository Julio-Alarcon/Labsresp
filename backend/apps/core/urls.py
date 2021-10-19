from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('calendario/', views.calendario, name="calendario"),    
    path('dashboard/',views.dashboard, name="dashboard"),
]