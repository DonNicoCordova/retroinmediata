# Generated by Django 2.1.1 on 2018-09-19 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retro_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='rut',
            field=models.CharField(default='Sin Rut', max_length=12),
        ),
    ]
