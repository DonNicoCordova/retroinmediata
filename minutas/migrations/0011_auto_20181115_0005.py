# Generated by Django 2.1.2 on 2018-11-15 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minutas', '0010_auto_20181113_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minute',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='Minuta/'),
        ),
    ]
