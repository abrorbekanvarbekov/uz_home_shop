# Generated by Django 4.0.6 on 2022-09-25 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0028_alter_user_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(default=0, max_length=20, unique=True),
        ),
    ]
