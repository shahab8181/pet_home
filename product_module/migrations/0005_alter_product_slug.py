# Generated by Django 4.1.7 on 2023-07-04 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0004_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=300, null=True, verbose_name='اسلاگ / ایدی'),
        ),
    ]