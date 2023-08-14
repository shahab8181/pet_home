from django import forms


class CheckOutForm(forms.Form):
    first_name = forms.CharField(
        label='نام',
        max_length=300,
        required=True,
        error_messages={
            'max_length' : 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-2',
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
        })
    )

    company = forms.CharField(
        label='نام شرکت (اختیاری)',
        max_length=300,
        required=False,
        error_messages={
            'max_length' : 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-2',
        })
    )

    country = forms.CharField(
        label='کشور | منطقه',
        max_length=300,
        required=True,
        error_messages={
            'max_length' : 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-2',
        })
    )

    state = forms.CharField(
        label='استان',
        max_length=300,
        required=True,
        error_messages={
            'max_length' : 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-2',
        })
    )

    city = forms.CharField(
        label='شهر',
        max_length=300,
        required=True,
        error_messages={
            'max_length' : 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-2',
        })
    )

    street_address = forms.CharField(
        label='ادرس خیابان',
        max_length=300,
        required=True,
        error_messages={
            'max_length' : 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-2',
        })
    )

    more_complete_address = forms.CharField(
        label='آپارتمان، مجتمع، واحد و... (اختیاری)',
        max_length=400,
        required=False,
        error_messages={
            'max_length' : 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-2',
        })
    )

    postal_code = forms.IntegerField(
        label='کدپستی',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-2',
        })
    )

    phone = forms.IntegerField(
        label='تلفن',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-2',
        })
    )

    email = forms.EmailField(
        label='ایمیل',
        max_length=300,
        required=True,
        error_messages={
            'max_length' : 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.EmailInput(attrs={
            'class': 'form-control mb-2',
        })
    )