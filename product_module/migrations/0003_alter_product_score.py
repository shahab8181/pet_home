# Generated by Django 4.1.7 on 2023-07-04 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0002_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='score',
            field=models.DecimalField(decimal_places=1, max_digits=5, verbose_name='امتیاز'),
        ),
    ]
