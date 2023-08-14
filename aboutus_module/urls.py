from django.urls import path
from .views import AboutUsView

urlpatterns = [
    path('about-us/', view=AboutUsView.as_view(), name='aboutus-page')
]
