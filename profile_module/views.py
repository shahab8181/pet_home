from django.db import models
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest
from django.views import View
from django.views.generic.base import TemplateView 
from django.views.generic.list import ListView
from django.views. generic.detail import DetailView
from account_module.models import User
from order_module.models import Order
from .forms import ChangeInformationForm, ChangePasswordForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

@method_decorator(login_required, name='dispatch')
class DashBoardView(TemplateView):
    template_name = r'profile_module/dashboard.html'



@method_decorator(login_required, name='dispatch')
class ChangeInformationView(View):
    def get(self, request: HttpRequest):
        online_user: User = User.objects.get(id=request.user.id)
        change_information_form: ChangeInformationForm = ChangeInformationForm(instance=online_user)
        return render(request, r'profile_module/change_info.html', context={
            'change_information_form': change_information_form,
            'online_user': online_user
        })

    def post(self, request: HttpRequest):
        online_user: User = User.objects.get(id=request.user.id)
        change_information_form: ChangeInformationForm = ChangeInformationForm(request.POST, request.FILES, instance=online_user)
        if change_information_form.is_valid() == True:
            if online_user is not None:
                change_information_form.save(commit=True)
            else:
                change_information_form.add_error('first_name', 'خطایی رخ داده دوباره امتحان کنید')
        else:
            change_information_form.add_error('first_name', 'خطایی در تکمیل فرم رخ داده')

        return render(request, r'profile_module/change_info.html', context={
            'change_information_form': change_information_form,
            'online_user': online_user
        })



@method_decorator(login_required, name='dispatch')
class RecentInvoicesView(ListView):
    template_name = r'profile_module/recent_invoices.html'
    model = Order
    context_object_name = 'orders'
    paginate_by = 5
    ordering = ['id']

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(user_id=self.request.user.id, is_paid=True).all()
        return query



@method_decorator(login_required, name='dispatch')
class InvoiceDetailView(DetailView):
    template_name = r'profile_module/invoice_detail.html'
    model = Order
    context_object_name = 'order'

    def get_queryset(self):
        query = super().get_queryset()
        query = query.prefetch_related('orderdetail_set')
        return query



@method_decorator(login_required, name='dispatch')
class ChangePasswordView(View):
    def get(self, request: HttpRequest):
        change_password_form: ChangePasswordForm = ChangePasswordForm()
        return render(request, r'profile_module/change_password.html', context={
            'change_password_form': change_password_form
        })

    def post(self, request: HttpRequest):
        change_password_form: ChangePasswordForm = ChangePasswordForm(request.POST)
        if change_password_form.is_valid() == True:
            online_user: User = User.objects.get(id=request.user.id)
            if online_user is not None:
                input_old_password: ChangePasswordForm = change_password_form.cleaned_data.get('old_password')
                input_new_password: ChangePasswordForm = change_password_form.cleaned_data.get('new_password')
                check_password: User & bool = online_user.check_password(input_old_password)
                if check_password == True:
                    online_user.set_password(input_new_password)
                    online_user.save()
                    return redirect(reverse('dashboard-page'))
            else:
                change_password_form.add_error('new_password', 'خطایی رخ داده دوباره امتحان کنید')
        else:
            change_password_form.add_error('new_password', 'خطایی در تکمیل فرم رخ داده')

        return render(request, r'profile_module/change_password.html', context={
            'change_password_form': change_password_form
        })

