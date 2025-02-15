# Generated by Django 5.1.6 on 2025-02-15 17:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_channel_banner_channel_description_channel_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='channel',
            options={'ordering': ['name'], 'verbose_name': 'Channel', 'verbose_name_plural': 'Channels'},
        ),
        migrations.AlterModelOptions(
            name='myuser',
            options={'ordering': ['username'], 'verbose_name': 'MyUser', 'verbose_name_plural': 'MyUsers'},
        ),
        migrations.AlterField(
            model_name='channel',
            name='owner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
