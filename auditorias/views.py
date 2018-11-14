from django.shortcuts import render
from django.shortcuts import redirect
from retro_auth.models  import *
from retro.models import *
from auditorias.forms import edit_umbral
import datetime

# Create your views here.

def auditorias(request):
    user = UserProfile.objects.get(user=request.user)
    return render(request, "auditorias/auditorias.html", {"umbral":UserProfile.objects.all(), "date":Post.objects.all(), "now": datetime.datetime.now(), "My_umbral": user})

def edit_Umbral(request):
    data = {}
    data["umbral"] = UserProfile.objects.all()
    data["date"] = Post.objects.all()
    data["now"] = datetime.datetime.now()
    umbral = UserProfile.objects.get(user=request.user)
    # teacher=UserProfile.objects.all()
    if umbral.is_teacher:
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
    else:
        return redirect('auditorias')


def auditorias_aut(request):
    post = Post.objects.all()
    for x in post:
        print (x)
        comment = Comment.objects.all()
        print(comment)
    # data = {}
    # for i in comment:
    #     data['first_name'] = i.author.user.first_name
    #     data['last_name'] = i.author.user.last_name
    #     data['rut'] = i.author.rut
    #     print (data['rut'])
