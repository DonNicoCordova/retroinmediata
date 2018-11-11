# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from retro_auth.models import UserProfile
# Create your models here.


class Meeting(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=True)
    publish_date = models.DateTimeField(default=timezone.now)
    time = models.PositiveIntegerField()

    def __str__(self):
        return "%s %s creó la reunión %s" % (self.userprofile.user.first_name, self.userprofile.user.last_name, self.name)


class Minute(models.Model):
    thematic = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    address = models.CharField(max_length=100)
    publish_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=2,
        choices=(
            ('AC', 'Aceptada'),
            ('EP', 'En proceso'),
            ('RE', 'Rechazada')
        ),
        default='EP',
    )

    def __str__(self):
        return "Minuta: %s" % (self.thematic)

class Member(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    minute = models.ForeignKey('Minute', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=2,
        choices=(
            ('AC', 'Aceptada'),
            ('EP', 'En proceso'),
            ('RE', 'Rechazada')
        ),
        default='EP',
    )
    privilege = models.CharField(
        max_length=2,
        choices=(
            ('DC', 'Director de Carrera'),
            ('SA', 'Secretario Académico'),
            ('PR', 'Profesor')
        ),
        default='PR',
    )

    class Meta:
        unique_together = (('userprofile', 'minute'),)

    def __str__(self):
        return "Miembro %s %s (%s) de la Minuta: %s con voto: %s" % (self.userprofile.user.first_name, self.userprofile.user.last_name, self.get_privilege_display(), self.minute.thematic, self.get_status_display())


class RefuseMinute(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    minute = models.ForeignKey('Minute', on_delete=models.CASCADE)
    publish_date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=500)

    class Meta:
        unique_together = (('userprofile', 'minute'),)

    def __str__(self):
        return "El miembro %s %s rechazó la minuta %s por: %s" % (self.userprofile.user.first_name, self.userprofile.user.last_name, self.minute.thematic, self.description)