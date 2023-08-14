from django.db import models
from account_module.models import User
from product_module.models import Product
from blog_module.models import Blog

# Create your models here.

class Comment(models.Model):

    class CommentPosition(models.TextChoices):
        main_page = ('main_page', 'صفحه اصلی')
        product_detail = ('product_detail', 'صفحه جزعیات محصولات')
        blog_detail = ('blog_detail', 'صفحه جزعیات وبلاگ')

    full_name = models.CharField(max_length=300, null=True, blank=True, verbose_name='کاربر')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='لیست کاربر ها')
    email = models.EmailField(max_length=100, verbose_name='ایمیل', blank=False)
    text = models.TextField(verbose_name='دیدگاه کاربر')
    commentposition = models.CharField(max_length=300, verbose_name='محل و موقعیت کامنت', choices=CommentPosition.choices)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name='محصول')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True, verbose_name='بلاگ')
    date = models.DateTimeField(verbose_name='زمان ایجاد کامنت', auto_now_add=True)
    read_by_admin = models.BooleanField(verbose_name='خوانده شده توسط ادمین یا خیر', default=True)
    is_accepted = models.BooleanField(verbose_name='تایید شده یا خیر', default=False, null=True)
    is_subcomment = models.BooleanField(verbose_name='پاسخ است یا خیر', default=False, null=True)
    is_star = models.BooleanField(verbose_name='ستاره دار است یا خیر', null=True)
    star = models.IntegerField(verbose_name='تعداد ستاره / امتیاز', null=True)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'