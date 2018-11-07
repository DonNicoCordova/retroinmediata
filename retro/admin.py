from django.contrib import admin
from django import forms
from .models import Subject,Section,Post,Comment

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'


class SubjectAdmin(admin.ModelAdmin):
    form = SubjectForm
    list_display = ['api_pk','name']

admin.site.register(Subject, SubjectAdmin)

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'


class SectionAdmin(admin.ModelAdmin):
    form = SectionForm
    list_display = ['section_type','api_pk','teacher','subject']
    list_filter = ['subject','section_type','teacher']
    search_fields = ['nrc']

admin.site.register(Section, SectionAdmin)
# Register your models here.
