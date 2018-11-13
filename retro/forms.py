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


class edit_postForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Ingresa el título'}),
                   'description': forms.Textarea(attrs={'class': 'form-control',
                                                        'placeholder': 'Ingresa la descripción'}),
                   'last_mod': forms.DateTimeInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Ingresa la fecha'})}
        fields = ['title', 'description', 'last_mod']


class create_postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']
