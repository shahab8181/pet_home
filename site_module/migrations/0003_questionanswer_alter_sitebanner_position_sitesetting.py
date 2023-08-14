# Generated by Django 4.1.7 on 2023-07-06 08:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0002_sitebanner'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='سوال')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیر فعال')),
            ],
            options={
                'verbose_name': 'سوال',
                'verbose_name_plural': 'سوالات',
            },
        ),
        migrations.AlterField(
            model_name='sitebanner',
            name='position',
            field=models.CharField(choices=[('home_page', 'صفحه اصلی'), ('product_list', 'صفحه لیست محصولات'), ('product_detail', 'صفحه جزعیات محصولات')], max_length=200, verbose_name='محل قرار گیری بنر'),
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان تنظیم')),
                ('logo', models.ImageField(upload_to='logo/', verbose_name='لوگو سایت')),
                ('short_text', models.CharField(max_length=800, verbose_name='متن کوتاه')),
                ('text', models.TextField(verbose_name='متن کامل')),
                ('product_count', models.IntegerField(editable=False, verbose_name='تعداد کل محصولات')),
                ('years_of_activity', models.IntegerField(verbose_name='سال های فعالیت')),
                ('number_of_team_members', models.IntegerField(verbose_name='تعداد افراد تیم')),
                ('number_of_satisfied_customers', models.IntegerField(verbose_name='تعداد مشتریان راضی')),
                ('address', models.TextField(verbose_name='ادرس')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('phone_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(9000000000), django.core.validators.MaxValueValidator(9999999999)], verbose_name='شماره تماس')),
                ('image', models.ImageField(upload_to='setting_images/', verbose_name='عکس')),
                ('copy_right', models.TextField(verbose_name='متن کپی رایت')),
                ('is_main_setting', models.BooleanField(verbose_name='تنظیمات اصلی / تنظیمات غیر اصلی')),
                ('question', models.ManyToManyField(related_name='questions', to='site_module.questionanswer', verbose_name='سوالات')),
            ],
            options={
                'verbose_name': 'تنظیم',
                'verbose_name_plural': 'تنظیمات',
            },
        ),
    ]
