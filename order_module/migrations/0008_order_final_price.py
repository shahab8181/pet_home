# Generated by Django 4.1.7 on 2023-08-04 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_module', '0007_alter_orderdetail_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='final_price',
            field=models.IntegerField(null=True, verbose_name='قیمت نهایی سبد'),
        ),
    ]
