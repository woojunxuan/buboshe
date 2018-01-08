# Generated by Django 2.0 on 2018-01-07 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buboshe_app', '0010_auto_20180106_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='belong_to',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.OneToOneField(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
