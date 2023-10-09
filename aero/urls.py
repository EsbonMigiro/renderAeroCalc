from django.urls import path
from .views import aeroview

urlpatterns=[
    path('aero/',aeroview , name= 'aero')
]