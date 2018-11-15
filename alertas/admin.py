from django.contrib import admin
from .models import AnswerReport, AnswerReportUser, Alerta, AlertMinute
# Register your models here.

admin.site.register(AnswerReport)
admin.site.register(AnswerReportUser)
admin.site.register(Alerta)
admin.site.register(AlertMinute)