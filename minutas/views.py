from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import MinutasForm
from minutas.models import *

# Create your views here.

def minutas(request):
    pass
    
def crear_minuta(request):
    minutas_form = MinutasForm()

    if request.method == "POST":
        minutas_form = MinutasForm(data=request.POST)
        if minutas_form.is_valid():
            pregunta = Minute(thematic = minutas_form.cleaned_data['them'],
                               description = minutas_form.cleaned_data['desc'],
                               address = minutas_form.cleaned_data['addr'])
            pregunta.save()
            #Todo bien
            return redirect(reverse('crear_minuta')+"?ok")

    return render(request, "minutas/_minutas.html", {'form':minutas_form})