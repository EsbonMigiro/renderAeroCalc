from django.urls import path 
from .views import aero_view


urlpatterns = [
    path('calc/', aero_view, name= 'aero_view')


]