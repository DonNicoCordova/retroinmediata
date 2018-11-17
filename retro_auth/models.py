# -*- coding: utf-8 -*-
from django.db import models
from retro_auth.defines import *
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,null=True, default=None, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, default="Sin Rut")
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    is_sacademic = models.BooleanField(default=False)
    is_dcareer = models.BooleanField(default=False)
    umbral = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(15)])
    
    def __str__(self):
        return "%s Rut: %s Umbral: %s" % (self.user, self.rut, self.umbral)