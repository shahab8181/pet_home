from django.urls import path
from .views import main_page

urlpatterns = [
    path('', view=main_page, name='home-page'),
]
