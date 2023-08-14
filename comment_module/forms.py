from django import forms

class CommentForm(forms.Form):
    text = forms.CharField(
        label='متن شما',
        max_length=300,
        required=True,
        error_messages={
            'max_length' : 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.Textarea(attrs={
            'class': 'form-control mb-2',
            'placeholder' : 'متن شما...'
        })
    )

    email = forms.CharField(
        label='متن شما',
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


    full_name = forms.CharField(
        label='نام و نام خانوادگی',
        max_length=300,
        required=True,
        error_messages={
            'max_length' : 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-2',
            'placeholder' : 'نام و نام خانوادگی شما...',
        })
    )

