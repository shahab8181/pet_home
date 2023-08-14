# Generated by Django 4.1.7 on 2023-07-07 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='عنوان')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیر فعال')),
            ],
            options={
                'verbose_name': 'دسته بندی وبلاگ',
                'verbose_name_plural': 'دسته بندی های وبلاگ',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان')),
                ('short_description', models.CharField(max_length=500, verbose_name='متن کوتاه')),
                ('description', models.TextField(verbose_name='متن')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('view', models.IntegerField(verbose_name='تعداد بازدید')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیر فعال')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='blog_module.blogcategory', verbose_name='دسته بندی وبلاگ')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uesrs', to=settings.AUTH_USER_MODEL, verbose_name='نوسینده')),
            ],
            options={
                'verbose_name': 'وبلاگ',
                'verbose_name_plural': 'وبلاگ ها',
            },
        ),
    ]
