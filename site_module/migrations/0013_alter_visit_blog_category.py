# Generated by Django 4.1.7 on 2023-07-14 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_module', '0006_alter_blogcategory_url_title'),
        ('site_module', '0012_visit_blog_category_visit_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='blog_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog_module.blog', verbose_name='بلاگ'),
        ),
    ]
