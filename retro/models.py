# -*- coding: utf-8 -*-
from django.db import models
from retro_auth.models import UserProfile
from django.utils import timezone
from retro.defines import *
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Threshold(models.Model):
    teacher = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    time = models.PositiveIntegerField()

    def __str__(self):
        return "%s %s con umbral de: %s" % (self.teacher.user.first_name, self.teacher.user.last_name, self.time)


class UserType(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    teacher = models.BooleanField()
    student = models.BooleanField()
    sacademic = models.BooleanField()
    dcareer = models.BooleanField()

    def __str__(self):
        return "%s %s es: Profesor: %s, Estudiante: %s, S.Académico: %s, D.Carrera: %s" % (self.userprofile.user.first_name, self.userprofile.user.last_name, self.teacher, self.student, self.sacademic, self.dcareer)


class Career(models.Model):
    director = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, default="Sin Carrera")
    status = models.BooleanField(default=True)

    def __str__(self):
        return "%s director: %s %s" % (self.name, self.director.user.first_name, self.director.user.last_name)


class CareerSubjectSection(models.Model):
    career = models.ForeignKey('Career', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('career', 'subject', 'section'),)

    def __str__(self):
        return "%s sección %s, está en la carrera de %s" % (self.subject.name, self.section.nrc, self.career.name)


class Subject(models.Model):
    name = models.CharField(max_length=100, default="No Name")
    subject_code = models.CharField(max_length=40,default="No Code")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Section(models.Model):
    teacher = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.SET_NULL)
    nrc = models.CharField(max_length=6, default="NoNRC")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nrc


class Student(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('student', 'section'),)


class Thread(models.Model):
    name = models.CharField(max_length=100)
    section = models.ForeignKey('Section', on_delete=models.CASCADE)
    publish_date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)

    def __str__(self):
        return "Pregunta '%s' a la seccion %s" % (self.name, self.section.nrc)


class ThreadRanking(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    thread = models.ForeignKey('Thread', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    class Meta:
        unique_together = (('userprofile', 'thread'),)

    def __str__(self):
        return "El usuario '%s %s' evaluó el hilo %s con %s" % (self.userprofile.user.first_name, self.userprofile.user.last_name, self.thread.name, self.rating)

class ThreadFollower(models.Model):
    thread = models.ForeignKey('Thread', on_delete=models.CASCADE)
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('thread', 'userprofile'),)

    def __str__(self):
        return "El usuario '%s %s' sigue el hilo %s" % (self.userprofile.user.first_name, self.userprofile.user.last_name, self.thread.name)


class Post(models.Model):
    thread = models.ForeignKey('Thread', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    publish_date = models.DateTimeField(default=timezone.now)
    last_mod = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)

    def __str__(self):
        return 'El usuario %s %s en el hilo %s preguntó %s' % (self.author.user.first_name, self.author.user.last_name, self.thread.name, self.description)


class PostFollower(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('post', 'userprofile'),)

    def __str__(self):
        return "El usuario '%s %s' sigue el la pregunta %s" % (self.userprofile.user.first_name, self.userprofile.user.last_name, self.post.description)


class PostRanking(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    class Meta:
        unique_together = (('userprofile', 'post'),)

    def __str__(self):
        return "El usuario '%s %s' evaluó la pregunta %s con %s" % (self.userprofile.user.first_name, self.userprofile.user.last_name, self.post.description, self.rating)


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=500)
    author = models.ForeignKey(UserProfile,on_delete=models.SET_NULL, null=True)
    publish_date = models.DateTimeField(default=timezone.now)
    last_mod = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)

    def __str__(self):
        return "el usuario %s %s comentó %s en la publicación %s" % (self.author.user.first_name, self.author.user.last_name, self.description, self.post.description)


class CommentArchive(models.Model):
    comment = models.ForeignKey("Comment", blank=True, default=None, on_delete=models.CASCADE)
    document = models.FileField(upload_to='Foro/Comment/%Y/%m/%d/')

    def __str__(self):
        return "el comentario %s tiene como archivo %s" % (self.comment.description, self.document.url)


class CommentRanking(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    class Meta:
        unique_together = (('userprofile', 'comment'),)

    def __str__(self):
        return "El usuario '%s %s' evaluó el comentario %s con %s" % (self.userprofile.user.first_name, self.userprofile.user.last_name, self.comment.description, self.rating)