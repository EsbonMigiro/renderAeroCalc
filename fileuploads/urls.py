from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    path('api/files/', views.get_all_files, name='get_all_files'),
    path('pdf/<str:pdf_file_name>/', views.view_pdf, name='view_pdf'),
]