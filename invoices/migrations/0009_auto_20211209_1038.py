# Generated by Django 3.2.9 on 2021-12-09 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0008_auto_20211209_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='number',
            field=models.CharField(default='7xwnepa92oix', max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='qr_code',
            field=models.CharField(default='zzdjbrle9vi6', max_length=450, unique=True),
        ),
    ]
