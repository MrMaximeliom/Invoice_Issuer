# Generated by Django 3.1.11 on 2021-11-24 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20211124_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(default='edcsmrlhxn3e3bzq9x2e', verbose_name='User Slug'),
        ),
    ]
