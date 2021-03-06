# Generated by Django 3.1.4 on 2022-01-16 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentary',
            name='author',
        ),
        migrations.AddField(
            model_name='commentary',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commentary',
            name='name',
            field=models.CharField(default='', max_length=30, verbose_name='Имя'),
            preserve_default=False,
        ),
    ]
