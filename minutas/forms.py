from django import forms
from minutas.models import *

class MinutasForm(forms.ModelForm):
    class Meta:
        model = Minute
        fields = ['thematic', 'address','document']


