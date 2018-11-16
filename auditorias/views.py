from django.shortcuts import render
from django.shortcuts import redirect
from retro_auth.models  import *
from retro.models import *
from auditorias.forms import edit_umbral
from auditorias.models import *
import datetime


def auditorias(request):
    pass
#    # solo no funciona cuando no a comentado nadie o solo el profe
#    docentes = UserProfile.objects.filter(is_teacher=True)
#    print(docentes)
#    for docente in docentes:
#        no_contestadas = []
#        secciones = docente.section_set.all()
#        for post in Post.objects.filter(threadsectionteacher=docente):
#            if post.comment_set.filter(author=docente).exists():
#                pass
#            else:
#                no_contestadas.append(post)

#    return render(request, "auditorias/audi2.html", data)


def historial_auditorias(request):
    data = {}
    data['auditoria'] = ForoAudit.objects.all()
    template_name = "auditorias/_auditorias.html"
    return render(request, template_name, data)

def buscar_auditorias(request):
    template_name = "auditorias/_auditorias2.html"
    data = {}
    data['auditorias'] = ForoAudit.objects.all()

    return render(request, template_name, data)

def edit_Umbral(request):
    data = {}
    data["umbral"] = UserProfile.objects.all()
    data["date"] = Post.objects.all()
    data["now"] = datetime.datetime.now()
    umbral = UserProfile.objects.get(user=request.user)
    # teacher=UserProfile.objects.all()
    if umbral.is_teacher == True:
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
        return redirect('edit_umbral.html')


def auditorias_aut(request):
    post = Post.objects.all()
    for x in post:
        print (x)
        comment = Comment.objects.all()
        print(comment)
        return redirect('../edit_umbral.html')
    # data = {}
    # for i in comment:
    #     data['first_name'] = i.author.user.first_name
    #     data['last_name'] = i.author.user.last_name
    #     data['rut'] = i.author.rut
    #     print (data['rut'])
