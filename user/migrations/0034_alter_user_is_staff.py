# Generated by Django 4.0.6 on 2022-09-25 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0033_user_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
