# Generated by Django 3.0.7 on 2020-07-17 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0028_auto_20200718_0139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
