# Generated by Django 4.1.7 on 2023-07-06 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactus_module', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='Issue',
            new_name='issue',
        ),
    ]
