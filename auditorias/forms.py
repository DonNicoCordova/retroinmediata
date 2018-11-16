from django import forms
from retro_auth.models import UserProfile

class edit_umbral(forms.ModelForm):
    def clean_umbral(self):
        data = self.cleaned_data['umbral']
        print (data)
        #Check date is not in past.
        if data < 1:
            print (data)
            raise forms.ValidationError(('Umbral invalido, porfavor elegir entre 1 y 15'))

        #Check date is in range librarian allowed to change (+4 weeks).
        if data >= 16:
            print (data)
            raise forms.ValidationError(('Umbral invalido, porfavor elegir entre 1 y 15'))

        # Remember to always return the cleaned data.
        return data
    class Meta:
        model = UserProfile
        fields = ['umbral']
        widgets = {'umbral': forms.NumberInput(attrs = {'width': '30'})}
