from django.urls import path
from .views import thin_disk_view

urlpatterns = [
    path('disk/', thin_disk_view)
]
