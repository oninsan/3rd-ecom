# Generated by Django 3.0.7 on 2020-07-11 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0016_auto_20200711_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='costumerinfo',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='costumerinfo',
            name='last_name',
        ),
    ]
