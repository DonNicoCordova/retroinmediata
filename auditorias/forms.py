from django import forms
from auditorias.models import ForoAudit
from retro_auth.models import UserProfile

class edit_umbral(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['umbral']
        
class ForoAuditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ForoAuditForm, self).__init__(*args, **kwargs)
        self.fields['teacher'] = forms.ModelChoiceField(queryset=UserProfile.objects.filter(is_teacher = True), required=True)
    class Meta:
        print("hola")
        model = ForoAudit
        fields = ('teacher',)