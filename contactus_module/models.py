from django.db import models

# Create your models here.

class ContactUs(models.Model):
    email = models.EmailField(verbose_name='ایمیل کاربر')
    issue = models.CharField(max_length=50, verbose_name='موضوع پیام')
    message_text = models.TextField(verbose_name='متن پیام')

    def __str__(self):
        return f'پیام ارسالی {self.id}'
    
    class Meta:
        verbose_name = 'پیام ارسالی'
        verbose_name_plural = 'پیام های ارسالی'