from django import forms
from django.core.exceptions import ValidationError

# forms here.

class RegisterForm(forms.Form):
    first_name = forms.CharField(
        label='نام',
        max_length=300,
        required=True,
        error_messages={
            'max_length' : 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-2',
            'placeholder' : 'نام شما...'
        })
    )

    last_name = forms.CharField(
        label='نام خانوادگی',
        max_length=300,
        required=True,
        error_messages={
            'max_length' : 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-2',
            'placeholder' : 'نام خانوادگی شما...'
        })
    )

    phone_number = forms.CharField(
        label='شماره همراه',
        max_length=12,
        required=True,
        error_messages={
            'max_length' : 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-2',
            'placeholder' : 'شماره همراه شما...'
        })
    )

    email = forms.CharField(
        label='ایمیل شما',
        max_length=300,
        required=True,
        error_messages={
            'max_length' : 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.EmailInput(attrs={
            'class': 'form-control mb-2',
            'placeholder' : 'ایمیل شما...'
        })
    )

    password = forms.CharField(
        label='کلمه عبور',
        max_length=300,
        required=True,
        error_messages={
            'max_length' : 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-2',
            'placeholder' : 'کلمه عبور...'
        })
    )

    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        max_length=300,
        required=True,
        error_messages={
            'max_length' : 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-2',
            'placeholder' : 'تکرار کلمه عبور...'
        })
    )
    
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password ==  confirm_password:
            return confirm_password
        else:
            raise ValidationError('کلمه عبور با تکرار کلمه عبور مطابقت ندارد ')
        
    

class LoginForm(forms.Form):
    email = forms.CharField(
        label='ایمیل شما',
        max_length=300,
        required=True,
        error_messages={
            'max_length' : 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.EmailInput(attrs={
            'class': 'form-control mb-2',
            'placeholder' : 'ایمیل شما...'
        })
    )

    password = forms.CharField(
        label='کلمه عبور',
        max_length=300,
        required=True,
        error_messages={
            'max_length' : 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-2',
            'placeholder' : 'کلمه عبور...'
        })
    )   



class ForgotPasswordForm(forms.Form):
    email = forms.CharField(
        label='ایمیل شما',
        max_length=300,
        required=True,
        error_messages={
            'max_length' : 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.EmailInput(attrs={
            'class': 'form-control mb-2',
            'placeholder' : 'ایمیل شما...'
        })
    )
    


class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(
        label='کلمه عبور جدید',
        max_length=300,
        required=True,
        error_messages={
            'max_length' : 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-2', 
            'placeholder': 'کلمه عبور جدید...'
        })
    )

    confirm_new_password = forms.CharField(
        label='تکرار کلمه عبور جدید',
        max_length=300,
        required=True,
        error_messages={
            'max_length' : 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-2', 
            'placeholder': 'تکرار کلمه عبور جدید...'
        })
    )
    
    def check_clean_password(self):
        new_password = self.cleaned_data.get('new_password')
        confirm_new_password = self.cleaned_data.get('confirm_new_password')

        if new_password == confirm_new_password:
            return new_password
        else:
            raise ValidationError('مطابقت ندارد \'تکرار کلمه عبور\' با \'کلمه عبور جدید\'')