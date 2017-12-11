from django.http import HttpResponse
from django.shortcuts import render
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def images(request):
    return render(request, 'image_uploader/images.html')

def new(request):
    print('new is doing something')
    painting = request.FILES['painting']
    path = default_storage.save('tmp/test.jpg', ContentFile(painting.read()))
    tmp_file = os.path.join(settings.MEDIA_ROOT, path)
    return render(request, 'image_uploader/success.html')
