from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.http import HttpRequest, JsonResponse
from .forms import ContactUsForm
from site_module.models import SiteSetting
from account_module.models import User
from .models import ContactUs

# Create your views here.

class ContactUsView(View):
    def get(self, request: HttpRequest):
        contact_us_form: ContactUsForm = ContactUsForm()
        setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        return render(request, r'contactus_module/contact-us.html', context={
            'contact_us_form': contact_us_form,
            'setting': setting
        })

    def post(self, request: HttpRequest):
        contact_us_form: ContactUsForm = ContactUsForm(request.POST)
        if contact_us_form.is_valid() == True:
            exsist_user: User & bool = User.objects.filter(email__iexact=contact_us_form.cleaned_data.get('email')).exists()
            if exsist_user == True:
                if request.user.is_authenticated == True:
                    new_message: ContactUs = ContactUs()
                    new_message.email = contact_us_form.cleaned_data.get('email')
                    new_message.issue = contact_us_form.cleaned_data.get('issue')
                    new_message.message_text = contact_us_form.cleaned_data.get('message_text')
                    new_message.save()
                    return redirect(reverse('home-page'))
                else:
                    contact_us_form.add_error('email', 'اول لاگین و یا ثبت نام کنید')
            else:
                contact_us_form.add_error('email', 'همچین کاربری با این ایمیل ثبت نام نکرده... برای تماس با ما می بایستی اول در سایت ثبت نام کنید')
        else:
            contact_us_form.add_error('email', 'خطایی در تکمیل فرم رخ داده')


        return render(request, r'contactus_module/contact-us.html', context={
            'contact_us_form': contact_us_form
        })
        