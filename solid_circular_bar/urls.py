from django.urls import path
from .views import solid_circular_bar_view

urlpatterns =[
     path('solidcircularbar/', solid_circular_bar_view, name='solidBar')
]