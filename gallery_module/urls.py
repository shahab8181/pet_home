from django.urls import path
from .views import animalgallery

urlpatterns = [
    path('gallery/', view=animalgallery, name='gallery-page')
]
