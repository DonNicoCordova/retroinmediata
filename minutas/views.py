from django.shortcuts import render, redirect
from .forms import MinutasForm, RefuseMinutes
from minutas.models import *
from retro.views import *

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
            form.save()
            return redirect(reverse('crear_minuta')+"?ok")
    else:
        form = MinutasForm()
    return render(request, "minutas/_minutas.html", {'form':form})