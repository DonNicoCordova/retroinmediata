from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import MinutasForm
from minutas.models import *

# Create your views here.

def minutas(request):
    pass

def crear_minuta(request):
    permisos = UserProfile.objects.get(user=request.user)
    if permisos.usertype_set.all()[0].dcareer or permisos.usertype_set.all()[0].sacademic:

        if request.method == 'POST':
            form = MinutasForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect(reverse('crear_minuta')+"?ok")
        else:
            form = MinutasForm()
        return render(request, "minutas/_minutas.html", {'form':form})
    else:
        return redirect('minutas')
"""   
def crear_minuta(request):
    minutas_form = MinutasForm()

    if request.method == "POST":
        minutas_form = MinutasForm(data=request.POST)
        form = 
        if minutas_form.is_valid():
            pregunta = Minute(thematic = minutas_form.cleaned_data['them'],
                                document= minutas_form.cleaned_data['docu'],
                               address = minutas_form.cleaned_data['addr'])
            pregunta.save()
            #Todo bien
            return redirect(reverse('crear_minuta')+"?ok")

    return render(request, "minutas/_minutas.html", {'form':minutas_form})
"""
