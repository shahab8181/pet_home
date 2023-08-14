from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from product_module.models import Product
from account_module.models import User
from blog_module.models import Blog
from product_module.models import Product

# Create your models here.

class QuestionAnswer(models.Model):
    question = models.CharField(max_length=500, verbose_name='سوال')
    answer = models.TextField(verbose_name='جواب', null=True)
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')

    def __str__(self):
        return f'{self.id} سوال - جواب شماره'
    
    class Meta:
        verbose_name = 'سوال'
        verbose_name_plural = 'سوالات'
    


class SiteSetting(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان تنظیم')
    info = models.CharField(max_length=500, verbose_name='درباره شرکت', null=True)
    logo = models.ImageField(upload_to='logo/', verbose_name='لوگو سایت', blank=True)
    short_text = models.CharField(max_length=800, verbose_name='متن کوتاه')
    text = models.TextField(verbose_name='متن کامل')
    product_count = models.IntegerField(verbose_name='تعداد کل محصولات', editable=False, blank=False)
    years_of_activity = models.IntegerField(verbose_name='سال های فعالیت')
    number_of_team_members = models.IntegerField(verbose_name='تعداد افراد تیم')
    number_of_satisfied_customers = models.IntegerField(verbose_name='تعداد مشتریان راضی')
    question = models.ManyToManyField(QuestionAnswer, related_name='questions', verbose_name='سوالات')
    address = models.TextField(verbose_name='ادرس')
    email = models.EmailField(verbose_name='ایمیل')
    phone_number = models.IntegerField(verbose_name='شماره تماس', validators=[MinValueValidator(9000000000), MaxValueValidator(9999999999)])
    image = models.ImageField(verbose_name='عکس', upload_to='setting_images/')
    copy_right = models.TextField(verbose_name='متن کپی رایت')
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی / تنظیمات غیر اصلی')

    def __str__(self):
        return f'{self.title} {self.id}'
    
    def products_count(self):
        return Product.objects.all().count()

    def save(self, **kwargs):
        self.product_count = Product.objects.all().count()
        return super().save(**kwargs)

    class Meta:
        verbose_name = 'تنظیم'
        verbose_name_plural = 'تنظیمات'
    


class Slider(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان اسلاید')
    image = models.ImageField(upload_to='slider/', verbose_name='عکس اسلاید')
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'اسلاید'
        verbose_name_plural = 'اسلاید ها'



class SiteBanner(models.Model):

    class SiteBannerPosition(models.TextChoices):
        home_page = ('home_page', 'صفحه اصلی')
        product_list = ('product_list', 'صفحه لیست محصولات')
        product_detail = ('product_detail', 'صفحه جزعیات محصولات')

    title = models.CharField(max_length=300, verbose_name='عنوان بنر')
    image = models.ImageField(verbose_name='عکس بنر', upload_to='banner/')
    url_on_banner = models.URLField(max_length=300, verbose_name='url روی عکس')
    position = models.CharField(max_length=200 ,verbose_name='محل قرار گیری بنر', choices=SiteBannerPosition.choices)
    is_active = models.BooleanField(verbose_name='فعال /غیر فعال')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'بنر'
        verbose_name_plural = 'بنر ها'



class Visit(models.Model):

    class ProductOrBlog(models.TextChoices):
        product_detail = ('product_detail', 'تعداد بازدید محصولات')
        blog_detail = ('blog_detail', 'تعداد بازدید وبلاگ')

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='کاربر')
    ip = models.CharField(max_length=300, verbose_name='ای پی', null=True)
    product_or_blog = models.CharField(max_length=300, verbose_name='محصول یا بلاگ', choices=ProductOrBlog.choices, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True, verbose_name='بلاگ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name='محصول')
    is_visit = models.BooleanField(verbose_name='بازید شده / نشده', null=True)

    def __str__(self):
        return f'{self.id} - {self.ip}'
    
    class Meta:
        verbose_name = 'بازدید'
        verbose_name_plural = 'بازدید ها'