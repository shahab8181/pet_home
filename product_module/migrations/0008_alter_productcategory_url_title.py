# Generated by Django 4.1.7 on 2023-07-07 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0007_productcategory_url_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='url_title',
            field=models.SlugField(max_length=300, null=True, verbose_name='عنوان در url'),
        ),
    ]
