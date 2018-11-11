from django.shortcuts import render
from retro_auth.models  import *
from retro.models import *
import datetime

# Create your views here.

def auditorias(request):
    # mydate = datetime.datetime.now()
    return render(request, "auditorias/auditorias.html", {"umbral":UserProfile.objects.all(), "date":Post.objects.all(), "now": datetime.datetime.now()})

def is_past_due(request):
    pass
