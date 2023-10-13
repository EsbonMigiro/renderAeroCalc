from django.urls import path
from .views import beam_stress_view

urlpatterns = [
    path('beamstress/', beam_stress_view)
]

