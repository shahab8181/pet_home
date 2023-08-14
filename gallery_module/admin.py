from django.contrib import admin
from .models import AnimalGallery

# Register your models here.

@admin.register(AnimalGallery)
class AnimalGallery(admin.ModelAdmin):
    list_display = ['title']
