from django.http import HttpResponse
from django.shortcuts import render

def images(request):
    return render(request, 'image_uploader/images.html')

def new(request):
    print('new is doing something')
    return render(request, 'image_uploader/success.html')
