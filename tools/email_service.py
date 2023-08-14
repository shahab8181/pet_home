from django.http import HttpRequest
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings


def send_email(subject, to, template_name, context):
    try:
        html_message = render_to_string(template_name, context=context)
        plain_message = strip_tags(html_message)
        email = settings.EMAIL_HOST_USER
        send_mail(subject, message=plain_message, from_email=email, recipient_list=[to], html_message=html_message)
    except:
        print('Email Send System Error!')