# -*- coding: utf-8 -*-
from django.db import models
from retro_auth.defines import *
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User,null=True,default=None,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,default="Sin Nombre")
    api_pk = models.CharField(max_length=4,default="NoPK")
    user_type = models.CharField(max_length=2,choices=USER_TYPE_CHOICES,default=USER_TYPE_DEFAULT)
    carreer = models.CharField(max_length=200,default="Sin Carrera")
    rut = models.CharField(max_length=12, default="Sin Rut")
    
    def __str__(self):
        return self.name