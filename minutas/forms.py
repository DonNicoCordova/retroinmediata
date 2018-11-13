from django import forms

class MinutasForm(forms.Form):
    #thematic
    them = forms.CharField(label="Tematica", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe la tematica'}
    
    ), min_length=3, max_length=100)
    #description
    desc = forms.CharField(label="Descripcion", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Descripcion'}
    
    ),min_length=3, max_length=100)
    #adress
    addr = forms.CharField(label="Direccion", required=True, widget=forms.Textarea(
        attrs={'class':'form-control','rows': 3, 'placeholder':'Direccion'}
    ), min_length=10, max_length=100)

