# Generated by Django 5.1.6 on 2025-02-16 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video',
            field=models.FileField(default=1, upload_to='videos/'),
            preserve_default=False,
        ),
    ]
