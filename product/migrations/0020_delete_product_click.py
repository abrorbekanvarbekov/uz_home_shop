# Generated by Django 4.1.1 on 2022-10-12 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_product_click_cat_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product_click',
        ),
    ]
