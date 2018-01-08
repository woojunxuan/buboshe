# Generated by Django 2.0 on 2018-01-06 07:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('buboshe_app', '0009_auto_20180104_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email_verify_code',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(default=django.utils.timezone.now, max_length=32),
            preserve_default=False,
        ),
    ]