from django.db import models
from account_module.models import User
from product_module.models import Product

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='کاربر')
    is_paid = models.BooleanField(verbose_name='پرداخت شده / نشده', null=True)
    final_price = models.IntegerField(verbose_name='قیمت نهایی سبد', null=True)
    date_of_payment = models.DateField(verbose_name='تاریخ پرداخت', null=True, blank=True)
    transportation = models.BooleanField(null=True, verbose_name='حمل نقل رایگان / پولی')
    shipping_price = models.IntegerField(verbose_name='قیمت حمل و نقل', null=True, blank=True)

    def __str__(self):
        return str(self.user)
    
    def transportation_price(self):
        if self.transportation == False:
            return self.shipping_price
        else:
            return 0

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'



class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, verbose_name='رسید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name='محصول')
    count = models.IntegerField(verbose_name='تعداد', null=True, default=0)
    final_price = models.IntegerField(verbose_name='قیمت نهایی', null=True)
    
    def __str__(self):
        return str(self.order)
    
    def totale_price(self):
        return int(self.product.price) * int(self.count)

    class Meta:
        ordering = ['final_price']
        verbose_name = 'جزعیات سبد خرید'
        verbose_name_plural = 'لیست جزعیات سبد خرید'



class OrderCheckOut(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, db_index=True,verbose_name='کاربر')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, db_index=True,verbose_name='رسید')
    first_name = models.CharField(max_length=300, null=True, blank=True, verbose_name='نام')
    last_name = models.CharField(max_length=300, null=True, blank=True, verbose_name='نام خانوادگی')
    company = models.CharField(max_length=300, null=True, blank=True, verbose_name='نام شرکت')
    country = models.CharField(max_length=200, null=True, blank=True, verbose_name='کشور | منطقه')
    state = models.CharField(max_length=100, null=True, blank=True, verbose_name='استان')
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name='شهر')
    street_address = models.TextField(null=True, blank=True, verbose_name='ادرس خیابان')
    more_complete_address = models.TextField(null=True, blank=True, verbose_name='آپارتمان، مجتمع، واحد و... ')
    postal_code = models.IntegerField(null=True, blank=True, verbose_name='کد پستی')
    phone = models.IntegerField(null=True, blank=True, verbose_name='تلفن')
    email = models.EmailField(null=True, blank=True, verbose_name='ایمیل')
    is_post = models.BooleanField(verbose_name='ارسال شده / نشده', null=True)

    def __str__(self):
        return str(self.order)
    
    class Meta:
        db_table = 'ordercheckouts'
        verbose_name = 'جزعیات نهایی سفارش'
        verbose_name_plural = 'لیست جزعیات نهایی سفارش ها'
