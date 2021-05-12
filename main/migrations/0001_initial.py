# Generated by Django 3.1.5 on 2021-05-12 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.CharField(default=None, max_length=50, null=True, verbose_name='Приоритет выполнения')),
            ],
            options={
                'verbose_name': ('Приоритет выполнения',),
                'verbose_name_plural': 'Приоритеты выполнения',
            },
        ),
        migrations.CreateModel(
            name='step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.CharField(max_length=50, verbose_name='Уровень выполнения')),
            ],
            options={
                'verbose_name': ('Уровень выполнения',),
                'verbose_name_plural': 'Уровни выполнения',
            },
        ),
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Задача')),
                ('description', models.TextField(verbose_name='Описание')),
                ('data_start', models.DateTimeField(auto_now_add=True, verbose_name='Дата начала')),
                ('data_end', models.DateTimeField(auto_now=True, verbose_name='Дата окончания')),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.priority', verbose_name='Приоритет выполнения')),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.step', verbose_name='Уровень выполнения')),
            ],
            options={
                'verbose_name': ('Диод',),
                'verbose_name_plural': 'Диоды',
            },
        ),
    ]
