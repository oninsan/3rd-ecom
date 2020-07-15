# Generated by Django 3.0.7 on 2020-07-15 04:30

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel', '0022_costumerinfo_destination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumer',
            name='user',
            field=models.OneToOneField(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
