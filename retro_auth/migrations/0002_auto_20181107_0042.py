# Generated by Django 2.0.9 on 2018-11-07 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retro_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='api_pk',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
    ]
