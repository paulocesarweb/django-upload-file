from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import File
import os, datetime

# Create your views here.

def index(request):
    if request.method == 'POST' and request.FILES['file']:
        upload_file = request.FILES['file']
        extension = os.path.splitext(upload_file.name)[1]
        rename = datetime.datetime.now().strftime("%Y_%m_%d %H_%M_%S") + extension
        fss = FileSystemStorage()
        filename = fss.save(rename, upload_file)
        file = File(file=rename)
        file.save()
        upload_file_path = fss.path(filename)
        new_name_url = request.build_absolute_uri()+str(rename)
        return render(request, 'file/index.html', {
            'upload_file_path': new_name_url.replace('file', 'media')
        })
    else:
        return render(request, 'file/index.html')