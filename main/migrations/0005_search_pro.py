# Generated by Django 4.1.1 on 2022-11-03 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_alter_shoppingcart_sum_price'),
        ('main', '0004_delete_product_click'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search_pro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
