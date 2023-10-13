from django.urls import path
from .views import cantilever_beam_view

urlpatterns=[
    path('cantilever/', cantilever_beam_view)
]