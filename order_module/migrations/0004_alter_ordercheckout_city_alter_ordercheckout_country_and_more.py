# Generated by Django 4.1.7 on 2023-07-31 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_module', '0003_alter_orderdetail_options_ordercheckout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercheckout',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='شهر'),
        ),
        migrations.AlterField(
            model_name='ordercheckout',
            name='country',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='کشور | منطقه'),
        ),
        migrations.AlterField(
            model_name='ordercheckout',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='ordercheckout',
            name='first_name',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='ordercheckout',
            name='last_name',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='ordercheckout',
            name='phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='تلفن'),
        ),
        migrations.AlterField(
            model_name='ordercheckout',
            name='postal_code',
            field=models.IntegerField(blank=True, null=True, verbose_name='کد پستی'),
        ),
        migrations.AlterField(
            model_name='ordercheckout',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='استان'),
        ),
        migrations.AlterField(
            model_name='ordercheckout',
            name='street_address',
            field=models.TextField(blank=True, null=True, verbose_name='ادرس خیابان'),
        ),
    ]
