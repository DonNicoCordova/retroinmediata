from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import MinutasForm
from minutas.models import *
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from retro.views import *
from django.core.exceptions import ValidationError

# Create your views here.

def minutas(request):
    pass

def crear_minuta(request):
    privilegio = UserProfile.objects.get(user=request.user)
    if privilegio.is_dcareer or privilegio.is_sacademic:

        if request.method == 'POST':
            form = MinutasForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect(reverse('crear_minuta')+"?ok")
        else:
            form = MinutasForm()
        return render(request, "minutas/_minutas.html", {'form':form})
    else:
        return redirect('index')


