from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the photoshare index.")

def gallery(request):
    return render(request, 'gallery.html')

def viewPhoto(request, pk):
    return render(request, 'photo.html')

def addPhoto(request):
    return render(request, 'add.html')
