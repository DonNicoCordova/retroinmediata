from django.contrib import admin
from .models import AnswerReport, AnswerReportUser,notification
# Register your models here.

admin.site.register(AnswerReport)
admin.site.register(AnswerReportUser)
admin.site.register(notification)