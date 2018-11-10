from django.shortcuts import render
from retro_auth.models  import *

# Create your views here.

def auditorias(request):
    return render(request, "auditorias/auditorias.html", {"umbral":UserProfile.objects.all()})
