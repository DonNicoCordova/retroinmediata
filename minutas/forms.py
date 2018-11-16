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

