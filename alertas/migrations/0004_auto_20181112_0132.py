# Generated by Django 2.0.9 on 2018-11-12 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alertas', '0003_merge_20181112_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alerta',
            name='post',
        ),
        migrations.RemoveField(
            model_name='alerta',
            name='student',
        ),
        migrations.DeleteModel(
            name='Alerta',
        ),
    ]
