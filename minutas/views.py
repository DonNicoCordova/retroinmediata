from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import MinutasForm, RefuseMinutes
from minutas.models import *
from retro_auth.models import *
from django.http import JsonResponse
from alertas.models import AlertMinute
# Create your views here.

def minutas(request):
    minuta = Minute.objects.all()
    data = {}
    data["object_all"] = minuta
    data["form"] = RefuseMinutes()
    if request.method == "POST":
        data['form'] = RefuseMinutes(request.POST)


        if data['form'].is_valid():
            # aca el formulario valido
            minuta = Minute.objects.get(pk=request.POST["pk"])

            obj = data['form'].save(commit = False)
            obj.minute = minuta
            userprofiles = UserProfile.objects.get(user = request.user)
            obj.userprofile = userprofiles
            obj.save()

            return JsonResponse({'message': 'ok'})

    else:
        print("holi")
        template = "minutas/listar_minutas.html"
        return render(request, template, data)
    template = "minutas/listar_minutas.html"
    return render(request, template, data)

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
