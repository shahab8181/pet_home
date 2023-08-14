from django import forms
from account_module.models import User
from django.core.exceptions import ValidationError


class ChangeInformationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'avatar', 'address', 'about_user']
        exclude = []

        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'phone_number': 'شماره همراه',
            'avatar': 'اپلود عکس جدید',
            'address': 'ادرس',
            'abour_user': 'درباره کاربر',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={ 'class': 'form-control mb-2', 'placeholder': 'نام...' }),

            'last_name': forms.TextInput(attrs={ 'class': 'form-control mb-2', 'placeholder': 'نام خانوادگی...' }),
            
            'phone_number': forms.TextInput(attrs={ 'class': 'form-control mb-2', 'placeholder': 'شماره همراه...'  }),

            'address': forms.Textarea(attrs={ 'class': 'form-control mb-2', 'placeholder': 'ادرس...'  }),

            'about_user': forms.Textarea(attrs={ 'class': 'form-control mb-2', 'placeholder': 'درباره کاربر...'  }),
        }



class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        label='کلمه عبور فعلی',
        max_length=300,
        required=True,
        error_messages={
            'max_length' : 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-2', 
            'placeholder': 'کلمه عبور فعلی...'
        })
    )

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