# Generated by Django 2.1.3 on 2018-11-12 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retro', '0003_auto_20181107_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='seguir',
            field=models.BooleanField(default=True),
        ),
    ]
