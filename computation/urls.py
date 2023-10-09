from django.urls import path
from .views import compute_ab
from .views import index

urlpatterns = [
    path('api/computing/', compute_ab, name='compute_sum'),
    path('index/', index, name='index'),

]