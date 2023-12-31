"""
URL configuration for django_demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url
from core.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
	path('admin/', admin.site.urls),
	path('wel/', ReactView.as_view(), name="something"),
    path('', include('fileuploads.urls')),
    path('', include('computation.urls')),
    path('', include('aero_calc.urls')),
    path('', include('aero.urls')),
    path('', include('machine_tool.urls')),
    path('', include('solid_circular_bar.urls')),
    path('', include('aircraft_carrier.urls')),
    path('', include('jetcarrier.urls')),
    path('', include('beam_stress.urls')),
    path('', include('cantilever_beam.urls')),
    path('', include('thin_disk.urls')),


]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)