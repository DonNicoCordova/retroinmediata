from django import forms
from auditorias.models import ForoAudit
from retro_auth.models import UserProfile

class edit_umbral(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['umbral']
        
class ForoAuditForm(forms.ModelForm):
    class Meta:
        model = ForoAudit
        fields = ('teacher',)