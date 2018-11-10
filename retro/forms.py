from django.forms import ModelForm
from retro.models import *
from django import forms


class post_form(ModelForm):
    class Meta:
        model = Comment
        fields = ['description']
class post_form_document(ModelForm):
    class Meta:
        model = CommentArchive
        fields = ['document']
