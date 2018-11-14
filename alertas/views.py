from django.shortcuts import render
from alertas.forms import *
from retro_auth.models  import *
from retro.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from retro_auth.models import UserProfile
from django.contrib import messages

# Create your views here.
def alerta(request):
    data = {}
    data["request"] = request
    if request.method == "POST":
        data['form2'] = Alerta2Form(request.POST)
        data['form'] = AlertaForm(request.POST)

        if data['form'].is_valid() and data['form2'].is_valid():
            aux = data['form2'].save()
            # aca el formulario valido
            aux2 = data['form'].save(commit=False)
            aux2.report = aux
            aux2.student = request.user.userprofile
            aux2.save()

            return HttpResponseRedirect(reverse('alerta'))

    else:
        data['form'] = AlertaForm()
        data['form2'] = Alerta2Form()
    template_name = 'alertas.html'
    return render(request, template_name, data)