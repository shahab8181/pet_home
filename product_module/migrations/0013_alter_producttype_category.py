# Generated by Django 4.1.7 on 2023-07-23 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0012_producttype_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttype',
            name='category',
            field=models.ManyToManyField(to='product_module.productcategory'),
        ),
    ]
