# Generated by Django 4.1.1 on 2022-10-12 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_product_click'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='feed_id',
        ),
    ]
