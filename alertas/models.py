# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from retro_auth.models import UserProfile
from retro.models import Post
from minutas.models import Minute
# Create your models here.


class AnswerReport(models.Model):
    description = models.CharField(max_length=500)
    publish_date = models.DateTimeField(default=timezone.now)

    def createReport(self, student, teacher, director):
        return AnswerReportUser.objects.create(report=self, student=student, teacher=teacher, director=director)

    def __str__(self):
        return "Reporte: %s con fecha %s" % (self.description, self.publish_date)


class AnswerReportUser(models.Model):
    report = models.OneToOneField('AnswerReport', on_delete=models.CASCADE)
    student = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='student_report')
    teacher = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='teacher_report')
    director = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='director_report')
    status = models.BooleanField(default=True)
    class Meta:
        unique_together = (('report', 'student', 'teacher'),)

    def __str__(self):
        return "Reporte: %s con fecha %s studiante %s %s al profesor %s %s" % (self.report.description, self.report.publish_date, self.student.user.first_name, self.student.user.last_name, self.teacher.user.first_name, self.teacher.user.last_name)


class Alerta(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    student_question = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='student_report_question')
    student_answerd = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='student_report_answer')
    publish_date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)
    #hilo = funcion(retorna si es hilo True, si no False )


    # def __str__(self):
    #Arreglamos esta funcion para que aparezca el nombre y el rut del usuario BIEN
        # return 'El usuario %s respondio a %s (que hizo la pregunta)' % (self.user_ans.user,self.user_ask.user )

class AlertMinute(models.Model):
    minutes = models.ForeignKey(Minute, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)

    # def __str__(self):
    #     return 'El usuario %s modifico la minuta %s ' % (self.user ,self.minutes.thematic)