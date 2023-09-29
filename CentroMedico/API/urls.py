from django.urls import path
from API import views

urlpatterns = [
    path('pacientes/', views.PacienteApi),
    path('paciente/<int:id>/', views.PacienteApi),
]