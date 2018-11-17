from django import template
from retro.models import Student, Section, Post
from alertas.models import Alerta, AlertMinute, AnswerReportUser
from datetime import datetime, timedelta

register = template.Library()

@register.filter
def PrivilegeCreateThread(request, sectionpk):
    if Student.objects.filter(student=request.user.userprofile, section_id=sectionpk).exists():
        return True
    if Section.objects.filter(pk=sectionpk, teacher=request.user.userprofile).exists():
        return True
    return False


@register.filter
def loadAlert(request):
    alert = Alerta.objects.filter(student_question=request.user.userprofile, status=True)
    # alert_minute = AlertMinute.objects.filter(user=request.user.userprofile, status=True)
    message = []
    for x in alert:
        message.append(('La pregunta <b>' + x.post.title + '</b> ha sido contestada por <b>' + x.student_answerd.user.first_name + " " + x.student_answerd.user.last_name + "</b>", x.publish_date))

    # for x in alert_minute:
    #     message.append(('La pregunta ' + x.title + ' ha sido contestada por ' + x.student_report_answer))

    if request.user.userprofile.is_teacher:
        umbral = request.user.userprofile.umbral
        list_post_no_comment = Post.objects.filter(thread__section__teacher=request.user.userprofile,
                                                   publish_date__lt=datetime.now() - timedelta(days=umbral))
        for x in list_post_no_comment:
            if not x.comment_set.filter(author=request.user.userprofile).exists():
                message.append(('La pregunta <b>' + x.title + '</b> ha sido superado tu umbral de respuesta', x.publish_date))
        umbral -= 1
        list_post_to_comment = Post.objects.filter(thread__section__teacher=request.user.userprofile,
                                                   publish_date__lt=datetime.now() - timedelta(days=umbral))
        for x in list_post_to_comment:
            if not x.comment_set.filter(author=request.user.userprofile).exists():
                message.append(('La pregunta <b>' + x.title + '</b> está a punto de superar tu umbral de respuesta', x.publish_date))
    if request.user.userprofile.is_dcareer:
        list_alert_post = AnswerReportUser.objects.filter(director=request.user.userprofile)
        for x in list_alert_post:
            message.append((x.report.description, x.report.publish_date))
    message.sort(key=lambda x: x[1], reverse=True)
    return message
