from django.db import models
from django.utils.text import slugify

# Create your models here.

class ProductType(models.Model):
    title = models.CharField(max_length=300, verbose_name='نوع محصول', null=True, blank=True)
    url_title = models.SlugField(max_length=300, verbose_name='عنوان در url', null=True)
    image = models.ImageField(upload_to='types/', verbose_name='عکس', null=True)
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'نوع محصول'
        verbose_name_plural = 'انواع محصول'



class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.SlugField(max_length=300, verbose_name='عنوان در url', null=True)
    group = models.ForeignKey(ProductType, on_delete=models.CASCADE, verbose_name='نوع محصول', null=True, blank=True)
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'



class Product(models.Model):
    name = models.CharField(max_length=300, verbose_name='نام')
    image = models.ImageField(upload_to='images/', verbose_name='عکس')
    score = models.DecimalField(verbose_name='امتیاز', decimal_places=1, max_digits=5)
    price = models.IntegerField(verbose_name='قیمت', null=True)
    count = models.IntegerField(verbose_name='تعداد')
    short_description = models.TextField(verbose_name='توضیحات مختصر', null=True)
    description = models.TextField(verbose_name='توضیحات', null=True)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE, null=True, blank=True, verbose_name='نوع')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, blank=True, verbose_name='دسته بندی')
    slug = models.SlugField(max_length=300, verbose_name='اسلاگ / ایدی', allow_unicode=True, null=True, blank=True)
    is_active = models.BooleanField(verbose_name='موجود / ناموجود')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    class Meta:
        ordering = 'price',
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

