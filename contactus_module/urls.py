from django.urls import path
from .views import ContactUsView

urlpatterns = [
    path('contact-us/', view=ContactUsView.as_view(), name='contactus-page')
]
