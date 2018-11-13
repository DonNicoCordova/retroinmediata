from django.forms import ModelForm
from alertas.models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AlertaForm(ModelForm):
    
    class Meta:
        model = AnswerReportUser
        fields = ['report','student','teacher']