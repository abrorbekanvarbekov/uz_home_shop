# Generated by Django 4.1 on 2022-09-08 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_user_managers_user_create_time_user_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]