# Generated by Django 2.0.9 on 2018-11-07 04:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('retro_auth', '0002_auto_20181107_0042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Sin Carrera', max_length=200)),
                ('status', models.BooleanField(default=True)),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='retro_auth.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='CareerSubjectSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retro.Career')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_mod', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(default=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='retro_auth.UserProfile')),
                ('parent', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='retro.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='CommentArchive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='Foro/Comment/%Y/%m/%d/')),
                ('comment', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='retro.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='CommentRanking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retro.Comment')),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retro_auth.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_mod', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(default=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='retro_auth.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='PostFollower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retro.Post')),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retro_auth.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='PostRanking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retro.Post')),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retro_auth.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nrc', models.CharField(default='NoNRC', max_length=6)),
                ('status', models.BooleanField(default=True)),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='retro_auth.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retro.Section')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retro_auth.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='No Name', max_length=100)),
                ('subject_code', models.CharField(default='No Code', max_length=40)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(default=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retro.Section')),
            ],
        ),
        migrations.CreateModel(
            name='ThreadFollower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retro.Thread')),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retro_auth.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='ThreadRanking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retro.Thread')),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retro_auth.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Threshold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.PositiveIntegerField()),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retro_auth.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.BooleanField()),
                ('student', models.BooleanField()),
                ('sacademic', models.BooleanField()),
                ('dcareer', models.BooleanField()),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retro_auth.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retro.Thread'),
        ),
        migrations.AddField(
            model_name='careersubjectsection',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retro.Section'),
        ),
        migrations.AddField(
            model_name='careersubjectsection',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retro.Subject'),
        ),
        migrations.AlterUniqueTogether(
            name='threadranking',
            unique_together={('userprofile', 'thread')},
        ),
        migrations.AlterUniqueTogether(
            name='threadfollower',
            unique_together={('thread', 'userprofile')},
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('student', 'section')},
        ),
        migrations.AlterUniqueTogether(
            name='postranking',
            unique_together={('userprofile', 'post')},
        ),
        migrations.AlterUniqueTogether(
            name='postfollower',
            unique_together={('post', 'userprofile')},
        ),
        migrations.AlterUniqueTogether(
            name='commentranking',
            unique_together={('userprofile', 'comment')},
        ),
        migrations.AlterUniqueTogether(
            name='careersubjectsection',
            unique_together={('career', 'subject', 'section')},
        ),
    ]
