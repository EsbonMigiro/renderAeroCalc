from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import UploadedFile
from .forms import UploadFileForm

from django.http import FileResponse
from django.conf import settings
import os

from django.utils._os import safe_join
from django.core.exceptions import SuspiciousOperation





def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_file')
    else:
        form = UploadFileForm()
    files = UploadedFile.objects.all()
    return render(request, 'upload_file.html', {'form': form, 'files': files})

def download_file(request, file_id):
    uploaded_file = UploadedFile.objects.get(pk=file_id)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response


# def get_all_files(request):
#     files = UploadedFile.objects.all()
#     file_list = []
#     for file in files:
#         file_data = {
#             'id': file.id,
#             'file_name': file.file.name,
#             'file_url': file.file.url,
#         }
#         file_list.append(file_data)
#     return JsonResponse({'files': file_list})

import os
from django.http import JsonResponse
from .models import UploadedFile

def get_all_files(request):
    files = UploadedFile.objects.all()
    file_list = []
    for file in files:
        file_name = os.path.basename(file.file.name)  # Extracting file name without path
        file_api = 'http://127.0.0.1:8000/pdf/'

        file_data = {
            'id': file.id,
            'file_name': file_name,
            'file_url': os.path.join(file_api, file_name)
            
        }
        file_list.append(file_data)
    return JsonResponse({'files': file_list})




from django.http import HttpResponse
from django.conf import settings
from django.core.exceptions import SuspiciousOperation
from django.http import HttpResponse
from django.utils._os import safe_join
import mimetypes

def view_pdf(request, pdf_file_name):
    try:
        pdf_path = safe_join(settings.MEDIA_ROOT, 'uploads', pdf_file_name)
        with open(pdf_path, 'rb') as pdf_file:
            # If the file exists, print "yes"
            print("yes")
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=some_file.pdf'
            return response
    except (FileNotFoundError, SuspiciousOperation):
        return HttpResponse("File not found", status=404)
    except Exception as e:
        # Log the exception for debugging purposes
        print(str(e))
        return HttpResponse("Internal Server Error", status=500)
