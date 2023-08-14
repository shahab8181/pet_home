from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    class UserGroup(models.TextChoices):
        admin = ('admin', 'مدیر عامل')
        programmer = ('programmer', 'برنامه نویس')
        graphic_designer = ('graphic_designer', 'طراح گرافیک')
        SEO = ('SEO', 'سئو')

    avatar = models.ImageField(verbose_name='تصویر آواتار', null=True, blank=True, upload_to='images/users')
    email_active_code = models.CharField(max_length=300, verbose_name='کد فعالسازی', null=True, blank=True)
    about_user = models.TextField(verbose_name='درباره کاربر', default='')
    address = models.TextField(verbose_name='ادرس', blank=True, null=True)
    phone_number = models.CharField(max_length=300, verbose_name='شماره موبایل')
    user_group = models.CharField(max_length=300, verbose_name='گروه', null=True, choices=UserGroup.choices)
    
    def __str__(self):
        if self.first_name == '' and self.last_name == '':
            return self.username
        else:
            return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


