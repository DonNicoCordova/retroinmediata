# -*- coding: utf-8 -*-
from django import forms
from .models import Thread

class ThreadForms(forms.ModelForm):
    class Meta:
        model = Thread
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}
        fields = ('name',)
