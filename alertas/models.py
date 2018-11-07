# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from retro_auth.models import UserProfile

# Create your models here.


class AnswerReport(models.Model):
    description = models.CharField(max_length=500)
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Reporte: %s con fecha %s" % (self.description, self.publish_date)


class AnswerReportUser(models.Model):
    report = models.OneToOneField('AnswerReport', on_delete=models.CASCADE)
    student = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='student_report')
    teacher = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='teacher_report')

    class Meta:
        unique_together = (('report', 'student', 'teacher'),)

    def __str__(self):
        return "Reporte: %s con fecha %s studiante %s %s al profesor %s %s" % (self.report.description, self.report.publish_date, self.student.user.first_name, self.student.user.last_name, self.teacher.user.first_name, self.teacher.user.last_name)