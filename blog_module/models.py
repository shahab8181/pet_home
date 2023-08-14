from django.db import models
from account_module.models import User
from django.utils.text import slugify

# Create your models here.

class BlogCategory(models.Model):
    name = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.SlugField(max_length=300, verbose_name='عنوان در url', null=True)
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'دسته بندی وبلاگ'
        verbose_name_plural = 'دسته بندی های وبلاگ'



class Blog(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, null=True, blank=True, verbose_name='دسته بندی وبلاگ', related_name='categories')
    image = models.ImageField(upload_to='blog/', verbose_name='عکس وبلاگ', null=True)
    short_description = models.CharField(max_length=500, verbose_name='متن کوتاه')
    description = models.TextField(verbose_name='متن')
    date_created = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    view = models.IntegerField(verbose_name='تعداد بازدید')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='نوسینده', related_name='uesrs', editable=False)
    slug = models.SlugField(max_length=300, verbose_name='اسلاگ / ایدی', db_index=True, allow_unicode=True, null=True, blank=True)
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.title
    
    def save(self, **kwargs):
        self.slug = slugify(f'blog {self.id}')
        super().save(**kwargs)
    
    class Meta:
        verbose_name = 'وبلاگ'
        verbose_name_plural = 'وبلاگ ها'
