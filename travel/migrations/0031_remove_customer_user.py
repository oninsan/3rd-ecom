# Generated by Django 3.0.7 on 2020-07-17 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0030_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]