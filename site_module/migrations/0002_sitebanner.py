# Generated by Django 4.1.7 on 2023-07-05 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان بنر')),
                ('image', models.ImageField(upload_to='banner/', verbose_name='عکس بنر')),
                ('url_on_banner', models.URLField(max_length=300, verbose_name='url روی عکس')),
                ('position', models.CharField(choices=[('home_page', 'صفحه لیست محصولات'), ('product_list', 'صفحه لیست محصولات'), ('product_detail', 'صفحه لیست محصولات')], max_length=200, verbose_name='محل قرار گیری بنر')),
                ('is_active', models.BooleanField(verbose_name='فعال /غیر فعال')),
            ],
            options={
                'verbose_name': 'بنر',
                'verbose_name_plural': 'بنر ها',
            },
        ),
    ]
