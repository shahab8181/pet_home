from django.shortcuts import render
from django.http import HttpRequest
from .models import AnimalGallery

# Create your views here.

def animalgallery(request: HttpRequest):
    gallery: AnimalGallery = AnimalGallery.objects.filter(is_active=True).all()
    return render(request, r'gallery_module/gallery.html', context={
        'gallery': gallery
    })