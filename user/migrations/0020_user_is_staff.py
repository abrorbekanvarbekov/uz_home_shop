# Generated by Django 4.1 on 2022-09-14 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_alter_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
