# Generated by Django 4.2 on 2023-04-20 15:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_room_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='users',
            field=models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL),
        ),
    ]