# -*- coding: utf-8 -*-
from django import forms
from .models import Thread, Comment, CommentArchive


class ThreadForms(forms.ModelForm):
    class Meta:
        model = Thread
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}
        fields = ('name',)


class post_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['description']


class post_form_document(forms.ModelForm):
    class Meta:
        model = CommentArchive
        fields = ['document']
