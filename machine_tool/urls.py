from django.urls import path
from .views import machine_tool_view

urlpatterns=[
    path('machine_tool', machine_tool_view, name='machine_tool_view')
]