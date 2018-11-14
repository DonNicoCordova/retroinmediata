from django import forms
from retro_auth.models import UserProfile

class edit_umbral(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['umbral']