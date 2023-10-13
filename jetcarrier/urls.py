from django.urls import path
from .views import jetcarrier_view

urlpatterns = [
    path('jetcarrier/', jetcarrier_view)
]
