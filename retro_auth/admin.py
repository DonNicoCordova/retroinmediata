from django.contrib import admin
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileAdmin(admin.ModelAdmin):
    form = UserProfileForm
    list_display = ['user','name','api_pk','user_type','carreer','rut']

admin.site.register(UserProfile, UserProfileAdmin)

# Register your models here.
