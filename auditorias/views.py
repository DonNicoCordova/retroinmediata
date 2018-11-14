from django.shortcuts import render
from retro_auth.models  import *
from retro.models import *
import datetime
from auditorias.models import *


# Create your views here
def auditorias(request):
    pass

def historial_auditorias(request):
    template_name = "auditorias/_auditorias.html"
    data = {}
    data['auditoria'] = ForoAudit.objects.all()
     
    return render(request, template_name, data)
    
def buscar_auditorias(request):
    template_name = "auditorias/_auditorias2.html"
    data = {}
    data['auditorias'] = ForoAudit.objects.all()
    
    return render(request, template_name, data)
