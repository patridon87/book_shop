# Generated by Django 4.0.5 on 2022-07-19 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(default=123, max_length=1500, verbose_name='ФИО Автора или авторов'),
            preserve_default=False,
        ),
    ]
