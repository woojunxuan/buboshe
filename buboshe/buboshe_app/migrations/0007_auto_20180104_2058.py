# Generated by Django 2.0 on 2018-01-04 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buboshe_app', '0006_auto_20180104_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='main_category',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='sub_category',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
