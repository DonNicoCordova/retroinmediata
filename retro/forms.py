# -*- coding: utf-8 -*-
from django import forms
from .models import Thread, Comment, CommentArchive, Post


class ThreadForms(forms.ModelForm):
    class Meta:
        model = Thread
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}
        fields = ('name',)


class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'description': forms.Textarea(attrs={'class': 'form-control'})}
        fields = ('title', 'description')


class post_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['description']


class post_form_document(forms.ModelForm):
    class Meta:
        model = CommentArchive
        fields = ['document']

