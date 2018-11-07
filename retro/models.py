# -*- coding: utf-8 -*-
from django.db import models
from retro_auth.models import UserProfile
from django.utils import timezone
from retro.defines import *

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100, default="No Name")
    subject_code = models.CharField(max_length=40,default="No Code")
    api_pk = models.CharField(max_length=4,default="NoPK")
    def __str__(self):
        return self.name

class Section(models.Model):
    section_type = models.CharField(max_length=2,choices=SECTION_TYPE_CHOICES,default=SECTION_TYPE_DEFAULT)
    api_pk = models.CharField(max_length=4,default="NoPK")
    teacher = models.ForeignKey(UserProfile,blank=True,null=True,on_delete=models.SET_NULL)
    schedule = models.CharField(max_length=100,default="Sin Horario")
    students = models.ManyToManyField(UserProfile,related_name="students",blank=True)
    subject = models.ForeignKey(Subject,blank=True,null=True,on_delete=models.SET_NULL)
    nrc = models.CharField(max_length=6,default="NoNRC")
    def __str__(self):
        return self.subject.name

class Post(models.Model):
    section = models.ForeignKey(Section,blank=True,default=None,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,default="")
    description = models.CharField(max_length=500,default="")
    author = models.ForeignKey(UserProfile,blank=True,null=True,on_delete=models.SET_NULL)
    publish_date = models.DateTimeField(default=timezone.now)
    last_mod = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return unicode(self.title, 'utf-8')

class Comment(models.Model):
    parent = models.ForeignKey("Comment",blank=True,default=None,on_delete=models.CASCADE)
    description = models.CharField(max_length=500,default="")
    author = models.ForeignKey(UserProfile,blank=True,null=True,on_delete=models.SET_NULL)
    publish_date = models.DateTimeField(default=timezone.now)
    last_mod = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return unicode(self.author.name, 'utf-8')