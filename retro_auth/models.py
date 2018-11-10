# -*- coding: utf-8 -*-
from django.db import models
from retro_auth.defines import *
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User,null=True,default=None,on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, default="Sin Rut")
    umbral = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return "%s Rut: %s Umbral: %s" % (self.user, self.rut, self.umbral)