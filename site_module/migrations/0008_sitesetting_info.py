# Generated by Django 4.1.7 on 2023-07-06 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0007_alter_sitesetting_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='info',
            field=models.CharField(max_length=500, null=True, verbose_name='درباره شرکت'),
        ),
    ]
