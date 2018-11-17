# Generated by Django 2.0.9 on 2018-11-17 03:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('retro_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('time', models.PositiveIntegerField()),
                ('userprofile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='retro_auth.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('AC', 'Aceptada'), ('EP', 'En proceso'), ('RE', 'Rechazada')], default='EP', max_length=2)),
                ('privilege', models.CharField(choices=[('DC', 'Director de Carrera'), ('SA', 'Secretario Académico'), ('PR', 'Profesor')], default='PR', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Minute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thematic', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=100)),
                ('document', models.FileField(blank=True, null=True, upload_to='Minuta/')),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('AC', 'Aceptada'), ('EP', 'En proceso'), ('RE', 'Rechazada')], default='EP', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='RefuseMinute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.CharField(max_length=500)),
                ('minute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minutas.Minute')),
                ('userprofile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='retro_auth.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='minute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minutas.Minute'),
        ),
        migrations.AddField(
            model_name='member',
            name='userprofile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='retro_auth.UserProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='refuseminute',
            unique_together={('userprofile', 'minute')},
        ),
        migrations.AlterUniqueTogether(
            name='member',
            unique_together={('userprofile', 'minute')},
        ),
    ]
