from django import forms
from auditorias.models import ForoAudit
from retro_auth.models import UserProfile
from alertas.forms import AnswerReport


class edit_umbral(forms.ModelForm):
    def clean_umbral(self):
        data = self.cleaned_data['umbral']
        if data < 1:
            raise forms.ValidationError(('Umbral invalido, porfavor elegir entre 1 y 15'))
        if data >= 16:
            raise forms.ValidationError(('Umbral invalido, porfavor elegir entre 1 y 15'))
        return data

    class Meta:
        model = UserProfile
        fields = ['umbral']


class ForoAuditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ForoAuditForm, self).__init__(*args, **kwargs)
        self.fields['alert'] = forms.ChoiceField(choices=[(x.pk, 'No Responde - Generada por: ' + x.answerreportuser.student.user.first_name + ' ' + x.answerreportuser.student.user.last_name +
                                                           ' al profesor ' + x.answerreportuser.teacher.user.first_name + ' ' + x.answerreportuser.teacher.user.last_name)
                                                          for x in AnswerReport.objects.filter(answerreportuser__director=self.request.user.userprofile)
                                                 .exclude(pk__in=AnswerReport.objects.filter(foroaudit__director=self.request.user.userprofile))],
                                                 widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = ForoAudit
        fields = ('alert',)
