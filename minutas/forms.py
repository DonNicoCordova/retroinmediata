from django import forms
from minutas.models import *

class MinutasForm(forms.ModelForm):
    class Meta:
        model = Minute
        fields = ['thematic', 'address','document']

class RefuseMinutes(forms.ModelForm):
    class Meta:
        model = RefuseMinute
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs={"class": "bonita", "id":"description"})
        }
