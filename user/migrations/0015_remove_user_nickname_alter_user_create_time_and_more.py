# Generated by Django 4.1 on 2022-09-13 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_user_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='update_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]