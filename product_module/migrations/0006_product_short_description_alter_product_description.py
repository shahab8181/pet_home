# Generated by Django 4.1.7 on 2023-07-05 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0005_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.TextField(null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(null=True, verbose_name='توضیحات'),
        ),
    ]
