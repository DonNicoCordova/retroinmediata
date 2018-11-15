from django.shortcuts import render
from django.shortcuts import redirect
from retro_auth.models  import *
from retro.models import *
from auditorias.forms import edit_umbral
from auditorias.models import *
import datetime

def coincidencia(request):
    data = {}
    lista = []
    lista2= []
    aux=[]
    repetido = []
    
    #se traen los post y se pasan a mayuscula para poder comparar
    for x in Post.objects.all():
        lista.append(x.title.upper())
    
    # keywords_2 sera el post recibido
    keywords_2 = "buena los cabros".upper()
    key3 = keywords_2.split(" ")

    # agrega las preguntas a una lista
    for i in lista:
        lista2.append(i.split(" "))
        
    #compara las palabras del nuevo post con las preguntas de todos los post 
    # en vase a un porcentaje mayor a 65% de coincidencia
    # agregar filtro de preguntas de un hilo
    
    for palubria in lista2:
        repetido = []
        aux=[]
        for v in key3:
            aux.append(str(v))
            if len(palubria) > 1:
                for b in palubria:
                    if v == b:
                        repetido.append(b)

            elif len(palubria)==1 and palubria == aux:
                print("ya hay un tema parecido: ",palubria)
                
        porcentaje1 = 100*len(repetido)/len(key3) #66.6%
        print(porcentaje1)

        if porcentaje1 > 65:
            # data para html para mostrar alerta de coincidencia
            return(True)
            data['mensaje'] = 'similar'
            print("Similar a",palubria)
        else:
            return(False)
        
    return render(request, "auditorias/auditorias.html",{"umbral":UserProfile.objects.all(),"date":Post.objects.all()})

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
#
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
