# -*- coding: utf-8 -*-
from django.db import models
from retro_auth.defines import *
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,null=True,default=None,on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, default="Sin Rut")
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    is_sacademic = models.BooleanField(default=False)
    is_dcareer = models.BooleanField(default=False)

    umbral = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return "%s %s" % (self.user.first_name,self.user.last_name)