from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import MinutasForm, RefuseMinutes
from minutas.models import *
from retro_auth.models import *
from django.http import JsonResponse
from alertas.models import *
from retro.views import *
from django.core.exceptions import ValidationError
from alertas.models import AlertMinute
# Create your views here.

def minutas(request):
    minuta = Minute.objects.all()
    data = {}
    data["object_all"] = minuta
    data["form"] = RefuseMinutes()
    userprofiles = UserProfile.objects.get(user = request.user)
    if userprofiles.student == True:
        redirect('minutas')
    if request.method == "POST":
        data['form'] = RefuseMinutes(request.POST)


        if data['form'].is_valid():
            # aca el formulario valido
            minuta = Minute.objects.get(pk=request.POST["pk"])

            obj = data['form'].save(commit = False)
            obj.minute = minuta
            obj.userprofile = userprofiles
            obj.save()
    else:
        data['AlertMinute'] = AlertMinute.objects.all()
        print(data['AlertMinute'])
        template = "minutas/listar_minutas.html"
        return render(request, template, data)
    template = "minutas/listar_minutas.html"

    return render(request, template, data)

def edit_minute(request, pk):
    data = {}
    data["type"] = 1
    if request.POST:
        formMinute = MinutasForm(request.POST, request.FILES, instance=Minute.objects.get(pk=pk))
        if formMinute.is_valid():
            minuta_editada = formMinute.save()
            profile = UserProfile.objects.get(user=request.user)
            new_member = Member(userprofile = profile, minute=minuta_editada)
            new_member.save()
            participantes = minuta_editada.member_set.all().values_list('userprofile', flat=True)
            for x in participantes:
                    AlertMinute.objects.create(minutes=minuta_editada, user_id=x)
            return redirect('minutas')
    else:
        data['form'] = MinutasForm(instance=Minute.objects.get(pk=pk))
    template_name = 'minutas/edit_minuta.html'
    return render(request, template_name, data)

def crear_minuta(request):
    privilegio = UserProfile.objects.get(user=request.user)
    #if privilegio.is_dcareer or privilegio.is_sacademic:

    if request.method == 'POST':
        form = MinutasForm(request.POST, request.FILES)
        if form.is_valid():
            minuta_creada = form.save()
            #esta parte no comprendo
            Member.objects.create(userprofile_id=1, minute=minuta_creada)
            #se cae con esto
            #Member.objects.create(userprofile_id=2, minute=minuta_creada)
            #
            participantes = minuta_creada.member_set.all().values_list('userprofile', flat=True)
            for x in participantes:
                    AlertMinute.objects.create(minutes=minuta_creada, user_id=x)
            return redirect(reverse('crear_minuta')+"?ok")
    else:
        form = MinutasForm()
    return render(request, "minutas/_minutas.html", {'form':form, 'minuta': Minute.objects.all(), 'alertas': AlertMinute.objects.filter(user=request.user.userprofile)})
