# Generated by Django 4.1.7 on 2023-08-04 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_module', '0008_order_final_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordercheckout',
            name='is_post',
            field=models.BooleanField(null=True, verbose_name='ارسال شده / نشده'),
        ),
    ]
