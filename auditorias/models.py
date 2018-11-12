# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from retro_auth.models import UserProfile
from alertas.models import AnswerReport


# Create your models here.

class ForoAudit(models.Model):
    director = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='director_audit_foro')
    student = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='student_audit_foro')
    teacher = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='teacher_audit_foro')
    alert = models.OneToOneField(AnswerReport, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = (('director', 'student', 'teacher'),)

    def __str__(self):
        return "El director %s %s creó una auditoría a través de una alerta %s enviada por el alumno %s %s al profesor %s %s" % \
               (self.director.user.first_name, self.director.user.last_name, self.alert.description, self.student.user.first_name, self.student.user.last_name,
                self.teacher.user.first_name, self.teacher.user.last_name,)


class MinutesAudit(models.Model):
    director = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='director_audit_minute')
    userprofile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='userprofile_audit_minute')
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "El director %s %s creó una auditoría de minutas al usuario %s %s" % \
               (self.director.user.first_name, self.director.user.last_name,
                self.userprofile.user.first_name, self.userprofile.user.last_name)