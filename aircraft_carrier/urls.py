from django.urls import path
from .views import aircraft_carrier_view

urlpatterns = [
    path('aircraftcarrier/', aircraft_carrier_view )

]