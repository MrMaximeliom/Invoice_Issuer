# Generated by Django 3.1.11 on 2021-11-24 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20211124_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(default='3cwokdfoc6x2jveryprj', verbose_name='User Slug'),
        ),
    ]
