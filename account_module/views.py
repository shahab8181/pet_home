from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.http import HttpRequest, HttpResponse
from .forms import RegisterForm, LoginForm, ForgotPasswordForm, ResetPasswordForm
from account_module.models import User
from django.contrib.auth import login, logout
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from tools.email_service import send_email

# Create your views here.

class RegisterView(View):
    def get(self, request: HttpRequest):
        register_form: RegisterForm = RegisterForm()
        return render(request, r'account_module/register.html', context={
            'register_form': register_form
        })

    def post(self, request: HttpRequest):
        register_form: RegisterForm = RegisterForm(request.POST)
        if register_form.is_valid() == True:
            exist_user: User & bool = User.objects.filter(email__iexact=register_form.cleaned_data.get('email')).exists()
            if exist_user == False:
                new_user: User = User()
                new_user.first_name = register_form.cleaned_data.get('first_name')
                new_user.last_name = register_form.cleaned_data.get('last_name')
                new_user.phone_number = register_form.cleaned_data.get('phone_number')
                new_user.email = register_form.cleaned_data.get('email')
                new_user.set_password(register_form.cleaned_data.get('password'))
                new_user.email_active_code = get_random_string(72)
                new_user.is_active = False
                new_user.is_staff = False
                new_user.is_superuser = False
                send_email(subject='فعالسازی حساب کاربری', to=new_user.email, template_name=r'emails/active_email.html', context={'user': new_user})
                new_user.save()
                return redirect(reverse('login-page'))
            else:
                register_form.add_error('email', 'این کاربر قبلا در سایت ثبت نام کرده')
        else:
            register_form.add_error('email', 'خطایی در تکمیل فرم رخ داده')

        return render(request, r'account_module/register.html', context={
            'register_form': register_form
        })



class ActivatorAccountView(View):
    def get(self, request: HttpRequest, activator_code):
        user: User = User.objects.filter(email_active_code__iexact=activator_code).first()
        if user is not None:
            if user.is_active == False:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                return HttpResponse('حساب کاربری شما فعال شد!')
        else:
            return HttpResponse(':(حساب کاربری قبلا فعال شده یا کد فعال ساز ایمیل منسوخ شده است')



class LoginView(View):
    def get(self, request: HttpRequest):
        login_form: LoginForm = LoginForm()
        return render(request, r'account_module/login.html', context={
            'login_form': login_form
        })

    def post(self, request: HttpRequest):
        login_form: LoginForm = LoginForm(request.POST)
        if login_form.is_valid() == True:
            current_user: User = User.objects.filter(email__iexact=login_form.cleaned_data.get('email')).first()
            if current_user != None:
                if current_user.is_active == True:
                    chk_pass = current_user.check_password(login_form.cleaned_data.get('password'))
                    if chk_pass ==  True:
                        print('user login successfuly.')
                        current_user.is_active = True
                        current_user.save()
                        login(request, current_user)
                        return redirect(reverse('home-page'))
                    else:
                        login_form.add_error('email', 'ایمیل کاربری یا کلمه عبور وارد شده صحیح نمی باشد')
                else:
                    login_form.add_error('email', 'حساب کاربری فعال نشده است!')
            else:
                login_form.add_error('email', 'ایمیل کاربری یا کلمه عبور وارد شده صحیح نمی باشد')
        else:
            login_form.add_error('email', 'خطایی در تکمیل فرم رخ داده')

        return render(request, r'account_module/login.html', context={
            'login_form': login_form
        })


@method_decorator(login_required, name='dispatch')
class LogoutView(View):
    def get(self, request: HttpRequest):
        logout(request)
        return redirect(reverse('login-page'))

    def post(self, request: HttpRequest):
        pass



class ForgotPasswordView(View):
    def get(self, request: HttpRequest):
        forgot_password_form: ForgotPasswordForm = ForgotPasswordForm()
        return render(request, r'account_module/forget_password.html', context={
            'forgot_password_form': forgot_password_form
        })
   
    def post(self, request: HttpRequest):
        forgot_password_form: ForgotPasswordForm = ForgotPasswordForm(request.POST)
        if forgot_password_form.is_valid() == True:
            user: User = User.objects.filter(email__iexact=forgot_password_form.cleaned_data.get('email')).first()
            if user is not None:
                if user.is_active == True:
                    send_email(subject='بازیابی کلمه عبور', to=user.email, template_name=r'emails/reset_password.html', context={'user': user})
                    return redirect(reverse('home-page'))
                else:
                    forgot_password_form.add_error('email', 'حساب کاربری فعال نشده')
            else:
                forgot_password_form.add_error('email', 'همچین کاربری یافت نشد... دوباره امتحان کنید یا در سایت لاگین کنید')
        else:
            forgot_password_form.add_error('email', 'خطایی در تکمیل فرم رخ داده')

        return render(request, r'account_module/forget_password.html', context={
            'forgot_password_form': forgot_password_form
        })
    


class ResetPasswordView(View):
    def get(self, request: HttpRequest, activator_code):
        user: User = User.objects.filter(email_active_code__iexact=activator_code).first()
        if user is None:
            return redirect(reverse('login-page'))
        else:
            reset_password_form: ResetPasswordForm = ResetPasswordForm()
            return render(request, r'account_module/reset_password.html', context={
                'reset_password_form': reset_password_form,
                'user': user
            })  

    def post(self, request: HttpRequest, activator_code):
        reset_password_form: ResetPasswordForm = ResetPasswordForm(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=activator_code).first()
        if reset_password_form.is_valid() == True:
            if user is None:
                print('user_none')
                return redirect(reverse('login-page'))
            else:
                new_user_pass = reset_password_form.cleaned_data.get('new_password')
                user.set_password(new_user_pass)
                user.email_active_code = get_random_string(72)
                user.is_active = True
                user.save()
                return redirect(reverse('login-page'))
        else:
            reset_password_form.add_error('new_password', 'خطایی در تکمیل فرم رخ داده')
                
        return render(request, r'account_module/reset_password.html', context={
            'reset_password_form': reset_password_form,
            'user': user
        })