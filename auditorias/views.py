from django.shortcuts import render
from django.shortcuts import redirect
from retro_auth.models  import *
from retro.models import *
from auditorias.forms import edit_umbral
import datetime

# Create your views here.

def auditorias(request):
    # mydate = datetime.datetime.now()
    user = UserProfile.objects.get(user=request.user)
    return render(request, "auditorias/auditorias.html", {"umbral":UserProfile.objects.all(), "date":Post.objects.all(), "now": datetime.datetime.now(), "My_umbral": user})

def edit_Umbral(request):
    data = {}
    data["umbral"] = UserProfile.objects.all()
    data["date"] = Post.objects.all()
    data["now"] = datetime.datetime.now()
    umbral = UserProfile.objects.get(user=request.user)
    if request.method == 'GET':
        form = edit_umbral(instance=umbral)
    else:
        form = edit_umbral(request.POST,instance=umbral)
        if form.is_valid():
            form.save()
            return redirect('auditorias')
        return render(request, 'auditorias/edit_umbral.html', data)
    data['form'] = form
    return render(request, 'auditorias/edit_umbral.html', data)
    