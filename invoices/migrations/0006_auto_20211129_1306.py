# Generated by Django 3.1.11 on 2021-11-29 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0005_auto_20211124_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceitem',
            name='slug',
            field=models.SlugField(default='', verbose_name='Invoice Item Slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='slug',
            field=models.SlugField(default='dyxnhg18gjnc9kybeh5m', verbose_name='Invoice Slug'),
        ),
    ]
