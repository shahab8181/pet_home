# Generated by Django 4.1.7 on 2023-07-06 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalgallery',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='ایدی عکس'),
        ),
    ]
