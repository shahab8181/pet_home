# Generated by Django 4.1.7 on 2023-07-14 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0010_alter_visit_options_visit_ip_visit_product_or_blog_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='is_visit',
            field=models.BooleanField(null=True, verbose_name='بازید شده / نشده'),
        ),
    ]
