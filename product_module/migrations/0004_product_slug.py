# Generated by Django 4.1.7 on 2023-07-04 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0003_alter_product_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=300, null=True, verbose_name='اسلاگ / ایدی'),
        ),
    ]
