# Generated by Django 3.0.7 on 2020-07-11 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0009_costumerinfo_booking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='costumerinfo',
            name='full_address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='costumerinfo',
            name='zipcode',
            field=models.CharField(max_length=100, null=True),
        ),
    ]