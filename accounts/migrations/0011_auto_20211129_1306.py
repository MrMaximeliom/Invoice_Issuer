# Generated by Django 3.1.11 on 2021-11-29 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20211124_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(default='prtvfga5jkkhgetvwenq', verbose_name='User Slug'),
        ),
    ]
