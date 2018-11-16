from django import forms
from minutas.models import *
from django.core.exceptions import ValidationError


class MinutasForm(forms.Form):
    #Funcion para limitar el tamaño del archivo que se subira
    def filee(value):
        import os 
        ext = os.path.splitext(value.name)[1]
        limit = 2 * 1024 * 1024
        valid_extensions = ['.pdf','.doc','.docx','.pptx','.xlsx']
        if value.size > limit:
            raise ValidationError('Archivo muy pesado. Maximo 2 MB.')
        if not ext in valid_extensions:
            raise ValidationError(u'Archivo no soportado solo pdf, doc, docx')


    thematic = forms.CharField(max_length=50)
    address = forms.CharField(max_length=100)
    document = forms.FileField(required=False, validators=[filee])





"""
class MinutasForm(forms.ModelForm):
    def file_size(value): # add this to some file where you can import it from
        limit = 2 * 1024 * 1024
        if value.size > limit:
            raise ValidationError('File too large. Size should not exceed 2 MiB.')

    class Meta:
        model = Minute
        fields = ['thematic', 'address','document']
        document = forms.FileField(required=False, validators=[file_size])
"""
