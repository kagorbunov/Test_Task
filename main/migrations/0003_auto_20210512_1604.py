# Generated by Django 3.1.5 on 2021-05-12 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210512_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='data_end',
            field=models.DateTimeField(verbose_name='Дата окончания'),
        ),
    ]
