# Generated by Django 2.1.2 on 2018-11-10 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retro_auth', '0002_auto_20181107_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='umbral',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
